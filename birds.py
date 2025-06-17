import pandas as pd
import plotly.express as px
from plotly.offline import plot
import webbrowser
from pathlib import Path
import os
import socketserver
from PyPDF2 import PdfMerger

# ——— your preamble & data prep ———
df = pd.read_csv('bird_migration.csv')
all_data = pd.concat([
    df[df.bird_name=='Eric'],
    df[df.bird_name=='Sanne'],
    df[df.bird_name=='Nico'],
])
# extract the YYYY-MM-DD HH:MM:SS prefix and parse it, coercing any bad entries to NaT
all_data['date_time'] = pd.to_datetime(
    all_data['date_time']
        .str.extract(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')[0],
    format='%Y-%m-%d %H:%M:%S',
    errors='coerce'
)
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

# Speichere alle drei Plots in einem einzigen mehrseitigen PDF
# Benötigt: kaleido und PyPDF2
#   pip install -U kaleido PyPDF2

# 1) Einzelseiten erzeugen
tmp_files = []
for fig, fname in zip(
    (fig1, fig2, fig3),
    ("page1.pdf", "page2.pdf", "page3.pdf")
):
    fig.write_image(fname, format="pdf", engine="kaleido")
    tmp_files.append(fname)

# 2) Mehrseitiges PDF zusammenführen
merger = PdfMerger()
for f in tmp_files:
    merger.append(f)
output_pdf = "AllBirdPlots.pdf"
merger.write(output_pdf)
merger.close()

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