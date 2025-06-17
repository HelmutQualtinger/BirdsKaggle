import pandas as pd
import plotly.express as px
from plotly.offline import plot
import webbrowser
from pathlib import Path
import os
import socketserver

# ——— your preamble & data prep ———
df = pd.read_csv('bird_migration.csv')
all_data = pd.concat([
    df[df.bird_name=='Eric'],
    df[df.bird_name=='Sanne'],
    df[df.bird_name=='Nico'],
])
all_data['date_time'] = pd.to_datetime(all_data['date_time'])
all_data['hour'] = all_data['date_time'].dt.hour

# ——— figure 1: map ———
fig1 = px.line_mapbox(
    all_data,
    lat='latitude', lon='longitude',
    color='bird_name',
    hover_data=['date_time'],
    mapbox_style='open-street-map',
    zoom=2,
    width=1400,   # increased width
    height=800,   # increased height
    title="Bird Migration Tracks"
)
fig1.update_traces(mode='markers+lines', marker_size=10)

# ——— figure 2: bar chart ———
avg_speed = (
    all_data
    .groupby(['bird_name','hour'])['speed_2d']
    .mean()
    .reset_index()
)
fig2 = px.bar(
    avg_speed,
    x='hour', y='speed_2d',
    color='bird_name',
    barmode='group',
    labels={'hour': 'Hour', 'speed_2d': 'Avg Speed (m/s)'},
    title='Average Speed by Hour'
)

# ——— embed both in one HTML ———
div1 = plot(fig1, include_plotlyjs=False, output_type='div')
div2 = plot(fig2, include_plotlyjs=False, output_type='div')

# figure 3: average speed by bird and day
avg_speed_day = (
    all_data
    .assign(date=all_data['date_time'].dt.date)
    .groupby(['bird_name', 'date'])['speed_2d']
    .mean()
    .reset_index()
)
fig3 = px.bar(
    avg_speed_day,
    x='date', y='speed_2d',
    color='bird_name',
    barmode='group',
    opacity=1.0,
    color_discrete_sequence=px.colors.qualitative.Vivid,
    labels={'date': 'Date', 'speed_2d': 'Avg Speed (m/s)'},
    title='Average Speed by Day'
)

# remove background and set grid lines to grey
fig3.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white'
)
fig3.update_xaxes(showgrid=True, gridcolor='grey')
fig3.update_yaxes(showgrid=True, gridcolor='grey')
div3 = plot(fig3, include_plotlyjs=False, output_type='div')

html = f"""
<html>
    <head>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <title>Birds Dashboard</title>
    </head>
    <body>
        <h1>Bird Migration Dashboard</h1>
        {div1}
        <hr/>
        {div2}
        <hr/>
        {div3}
    </body>
</html>
"""
import http.server

# write the HTML out to a file
output_path = Path(__file__).parent / "dashboard.html"
output_path.write_text(html)

# serve the directory containing the dashboard
os.chdir(output_path.parent)
PORT = 8888
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at http://localhost:{PORT}/{output_path.name}")
    httpd.serve_forever()