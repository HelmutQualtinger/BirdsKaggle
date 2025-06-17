# Bird Migration Analysis

Dieses Projekt analysiert und visualisiert Vogelmigrationsdaten von drei Vögeln (Eric, Nico und Sanne) mit verschiedenen interaktiven Dashboards und Karten.

## Dateien im Projekt

- [`bird_migration.csv`](bird_migration.csv) - Hauptdatensatz mit Migrationsdaten aller drei Vögel
- [`birds.py`](birds.py) - Hauptskript für interaktives Dashboard mit Plotly
- [`birds2.py`](birds2.py) - Skript zur Erstellung einer Folium-Karte mit Flugrouten
- [`birds.ipynb`](birds.ipynb) - Jupyter Notebook für Datenanalyse und Geschwindigkeitsverteilungen
- [`birds_dashboard.html`](birds_dashboard.html) - Generiertes Dashboard (Output von birds.py)
- [`all_birds_routes.html`](all_birds_routes.html) - Generierte Karte (Output von birds2.py)
- [`dashboard.html`](dashboard.html) - Alternative Dashboard-Version

## Hauptfunktionen

### 1. Interaktives Dashboard ([`birds.py`](birds.py))

Das Hauptskript erstellt ein umfassendes Dashboard mit drei Visualisierungen:

- **Migrationskarte**: Interaktive Karte mit den Flugrouten aller drei Vögel
- **Geschwindigkeit nach Stunde**: Balkendiagramm der durchschnittlichen Geschwindigkeit pro Tagesstunde
- **Geschwindigkeit nach Tag**: Tägliche Durchschnittsgeschwindigkeiten über die Zeit

```bash
python birds.py
```

Das Skript:
- Lädt die Daten aus [`bird_migration.csv`](bird_migration.csv)
- Erstellt drei interaktive Plotly-Visualisierungen
- Generiert eine HTML-Datei mit allen Plots
- Startet einen lokalen Webserver auf Port 8888

### 2. Flugrouten-Karte ([`birds2.py`](birds2.py))

Erstellt eine interaktive Folium-Karte mit den kompletten Flugrouten:

```bash
python birds2.py
```

Features:
- Verschiedene Farben für jeden Vogel (Eric: blau, Sanne: orange, Nico: rot)
- Interaktive Polylinien mit Hover-Effekten
- Automatisches Anpassen der Kartenansicht an alle Datenpunkte

### 3. Datenanalyse ([`birds.ipynb`](birds.ipynb))

Jupyter Notebook für detaillierte Analyse:
- Geschwindigkeitsverteilungen für jeden Vogel
- Statistische Auswertungen (Mittelwert, Maximum)
- Histogramme und Vergleichsplots

## Datenstruktur

Die [`bird_migration.csv`](bird_migration.csv) enthält folgende Spalten:

| Spalte | Beschreibung |
|--------|-------------|
| `altitude` | Höhe in Metern |
| `date_time` | Zeitstempel der Messung |
| `device_info_serial` | Geräte-ID (851 für alle Messungen) |
| `direction` | Flugrichtung in Grad |
| `latitude` | Breitengrad |
| `longitude` | Längengrad |
| `speed_2d` | 2D-Geschwindigkeit in m/s |
| `bird_name` | Name des Vogels (Eric, Nico, Sanne) |

## Geschwindigkeitsstatistiken

Aus der Analyse ergeben sich folgende Durchschnittswerte:

- **Eric**: Durchschnitt 2.30 m/s, Maximum 63.49 m/s
- **Nico**: Durchschnitt 2.91 m/s, Maximum 48.38 m/s  
- **Sanne**: Durchschnitt 2.45 m/s, Maximum 57.20 m/s

## Voraussetzungen

```bash
pip install pandas plotly folium matplotlib
```

## Verwendung

1. **Dashboard starten**:
   ```bash
   python birds.py
   ```
   Öffnet Browser auf `http://localhost:8888/dashboard.html`

2. **Karte generieren**:
   ```bash
   python birds2.py
   ```
   Erstellt `all_birds_routes.html`

3. **Notebook öffnen**:
   ```bash
   jupyter notebook birds.ipynb
   ```

## Ausgabedateien

- [`dashboard.html`](dashboard.html) - Interaktives Dashboard mit allen Plots
- [`all_birds_routes.html`](all_birds_routes.html) - Interaktive Karte mit Flugrouten
- [`birds_dashboard.html`](birds_dashboard.html) - Alternative Dashboard-Version

## Datenquelle

Die Migrationsdaten stammen aus einem Kaggle-Dataset und umfassen GPS-Messungen von drei Vögeln über mehrere Monate im Jahr 2013.

---

# Analisi della Migrazione degli Uccelli

Questo progetto analizza e visualizza i dati di migrazione di tre uccelli (Eric, Nico e Sanne) con diversi dashboard interattivi e mappe.

## File del Progetto

- [`bird_migration.csv`](bird_migration.csv) - Dataset principale con i dati di migrazione di tutti e tre gli uccelli
- [`birds.py`](birds.py) - Script principale per dashboard interattivo con Plotly
- [`birds2.py`](birds2.py) - Script per creare una mappa Folium con le rotte di volo
- [`birds.ipynb`](birds.ipynb) - Jupyter Notebook per analisi dei dati e distribuzioni di velocità
- [`birds_dashboard.html`](birds_dashboard.html) - Dashboard generato (output di birds.py)
- [`all_birds_routes.html`](all_birds_routes.html) - Mappa generata (output di birds2.py)
- [`dashboard.html`](dashboard.html) - Versione alternativa del dashboard

## Funzionalità Principali

### 1. Dashboard Interattivo ([`birds.py`](birds.py))

Lo script principale crea un dashboard completo con tre visualizzazioni:

- **Mappa di migrazione**: Mappa interattiva con le rotte di volo di tutti e tre gli uccelli
- **Velocità per ora**: Grafico a barre della velocità media per ora del giorno
- **Velocità per giorno**: Velocità medie giornaliere nel tempo

```bash
python birds.py
```

Lo script:
- Carica i dati da [`bird_migration.csv`](bird_migration.csv)
- Crea tre visualizzazioni interattive Plotly
- Genera un file HTML con tutti i grafici
- Avvia un server web locale sulla porta 8888

### 2. Mappa delle Rotte di Volo ([`birds2.py`](birds2.py))

Crea una mappa interattiva Folium con le rotte di volo complete:

```bash
python birds2.py
```

Caratteristiche:
- Colori diversi per ogni uccello (Eric: blu, Sanne: arancione, Nico: rosso)
- Polilinee interattive con effetti hover
- Adattamento automatico della vista mappa a tutti i punti dati

### 3. Analisi dei Dati ([`birds.ipynb`](birds.ipynb))

Jupyter Notebook per analisi dettagliata:
- Distribuzioni di velocità per ogni uccello
- Valutazioni statistiche (media, massimo)
- Istogrammi e grafici comparativi

## Struttura dei Dati

Il file [`bird_migration.csv`](bird_migration.csv) contiene le seguenti colonne:

| Colonna | Descrizione |
|---------|-------------|
| `altitude` | Altitudine in metri |
| `date_time` | Timestamp della misurazione |
| `device_info_serial` | ID dispositivo (851 per tutte le misurazioni) |
| `direction` | Direzione di volo in gradi |
| `latitude` | Latitudine |
| `longitude` | Longitudine |
| `speed_2d` | Velocità 2D in m/s |
| `bird_name` | Nome dell'uccello (Eric, Nico, Sanne) |

## Statistiche di Velocità

Dall'analisi risultano i seguenti valori medi:

- **Eric**: Media 2.30 m/s, Massimo 63.49 m/s
- **Nico**: Media 2.91 m/s, Massimo 48.38 m/s  
- **Sanne**: Media 2.45 m/s, Massimo 57.20 m/s

## Prerequisiti

```bash
pip install pandas plotly folium matplotlib
```

## Utilizzo

1. **Avviare il dashboard**:
   ```bash
   python birds.py
   ```
   Apre il browser su `http://localhost:8888/dashboard.html`

2. **Generare la mappa**:
   ```bash
   python birds2.py
   ```
   Crea `all_birds_routes.html`

3. **Aprire il notebook**:
   ```bash
   jupyter notebook birds.ipynb
   ```

## File di Output

- [`dashboard.html`](dashboard.html) - Dashboard interattivo con tutti i grafici
- [`all_birds_routes.html`](all_birds_routes.html) - Mappa interattiva con le rotte di volo
- [`birds_dashboard.html`](birds_dashboard.html) - Versione alternativa del dashboard

## Fonte dei Dati

I dati di migrazione provengono da un dataset Kaggle e includono misurazioni GPS di tre uccelli per diversi mesi nel 2013.