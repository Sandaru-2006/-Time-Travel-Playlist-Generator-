from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "7daf8bd8b26c4ecc9b2a2224f2429921"
SPOTIFY_CLIENT_SECRET = "6d8f1658327b4d228d29fda7c8f4b606"
USER_ID = "Sandaru Perera"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'lxml')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": SPOTIFY_CLIENT_ID,
    "client_secret": SPOTIFY_CLIENT_SECRET
}

response = requests.post(url="https://accounts.spotify.com/api/token", headers=headers, data=data)
access_token = response.json()["access_token"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:4304/auth/spotify/callback",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USER_ID,
    )
)
user_id = sp.current_user()["id"]


playlist = sp.user_playlist_create(user=user_id, name=f"Top 100 hits on {date}", public=False,
                                   description="My first programmatic playlist, yooo!")
playlist_id = playlist['id']
track_uris = []  # Initialize an empty list to store track URIs

for song in song_names:  # Iterate over the list of song names scraped from Billboard
    result = sp.search(q=f"track:{song}", type="track", limit=1)  # Search for the song on Spotify, limiting to one result
    try:
        track_uris.append(result['tracks']['items'][0]['uri'])  # Try to append the URI of the found track to the list
    except IndexError:
        print(f"Track '{song}' not found on Spotify. Skipping.")  # Print a message if the track is not found

# Check if any tracks were found
if track_uris:
    sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)  # Add the tracks to the playlist
    print("Playlist created successfully!")  # Confirm the creation of the playlist
else:
    print("No tracks found to add to the playlist.")  # Indicate that no tracks were found
