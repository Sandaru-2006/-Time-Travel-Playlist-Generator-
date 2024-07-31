Time Travel Playlist Generator 🕰️🎧

This project creates a Spotify playlist of the top 100 Billboard hits from any chosen date. It combines web scraping with the Spotify API to generate a nostalgic musical experience.

Features

Date-Specific Playlists: Fetches the top 100 Billboard songs for any input date.
Web Scraping: Uses BeautifulSoup to scrape song titles from the Billboard website.
Spotify Integration: Searches for the songs on Spotify and creates a playlist.

Tech Stack

Python: The core programming language used.
BeautifulSoup: For web scraping Billboard data.
Spotify API: To search for songs and create playlists.
Requests: For making HTTP requests.

How It Works

Input Date:
The user inputs a date in the format YYYY-MM-DD.
Web Scraping:
The script scrapes the Billboard website for the top 100 songs on that date.
Spotify Search:
Searches for each song on Spotify.
Playlist Creation:
Creates a private playlist on Spotify with the found songs.

Usage

Clone the repository:
git clone https://github.com/yourusername/time-travel-playlist-generator.git

Install the required libraries:
pip install -r requirements.txt

Set up your environment variables for Spotify API:
SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET
USER_ID

Run the script:
python main.py

Configuration
Spotify API: Ensure your Spotify API credentials are set up correctly.
Billboard Scraping: Make sure the date format is YYYY-MM-DD.
