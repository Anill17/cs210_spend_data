# Spotify Listening Insights Analysis

## Overview

This project focuses on analyzing Spotify listening history to uncover patterns and preferences in music consumption. By exploring detailed data such as streaming history, playlists, and user library, the goal is to gain insights into the user's musical habits and trends over time.

## Author

This project is conducted by **Anıl Sümer Topaloğlu** as part of an individual exploration of personal Spotify data.

## Motivation

Music plays a significant role in our daily lives. Through this project, I aim to:
- Understand my listening habits, such as most-listened-to artists, songs, and genres.
- Identify trends in my listening patterns, including time of day and seasonal preferences.
- Gain insights into how my music preferences have evolved over time.

## Data Source

The dataset is sourced from Spotify’s personal data export. The files are structured JSON files provided by Spotify, containing information about streaming history, playlists, library contents, and more.

### Key Files:
1. **Streaming History**:
   - Files: `StreamingHistory_music_*.json`, `StreamingHistory_podcast_0.json`
   - Contains detailed logs of music and podcast streaming with timestamps.
2. **User Library**:
   - File: `YourLibrary.json`
   - Contains information about saved tracks, albums, and playlists.
3. **Search History**:
   - File: `SearchQueries.json`
   - Logs of Spotify searches performed by the user.

*Note*: The data is stored locally in the `spotify_data` directory.

## Objectives

The primary objectives of this project are:
- **Top Artists and Songs**: Identify the most-played artists, albums, and tracks.
- **Listening Patterns**: Analyze listening habits based on time of day, days of the week, and months of the year.
- **Playlist Insights**: Explore trends and themes within personal playlists.
- **Genre Analysis**: Categorize songs by genre and assess their popularity over time.

## Data Processing Steps

1. **Data Extraction**:
   - Load and parse JSON files from the `spotify_data` folder using Python.
   - Extract relevant information such as track names, artists, genres, and timestamps.

2. **Data Cleaning**:
   - Remove duplicate entries and clean up inconsistencies in artist or track names.
   - Standardize timestamp formats for easier analysis.

3. **Data Integration**:
   - Combine data from multiple JSON files to create a unified dataset for analysis.

4. **Analysis Preparation**:
   - Create derived columns for day of the week, hour, and month based on timestamps.
   - Aggregate listening metrics (e.g., play count by artist, track, and genre).

## Tools and Libraries

- **Python**: Main programming language.
- **Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `matplotlib` and `seaborn`: For data visualization.
  - `json`: For parsing JSON files.

## Analysis & Visualization


## Findings


## Directory Structure


## Installation and Setup

1. **Clone the Repository**
    ```bash
    git clone xxx
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd spotify-insights-analysis
    ```

3. **Install Required Python Libraries**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Data Parsing Script**
    ```bash
    python scripts/parse_spotify_data.py
    ```

5. **Open the Analysis Notebook**
    ```bash
    jupyter notebook notebooks/analysis.ipynb
    ```


## Conclusion


---

