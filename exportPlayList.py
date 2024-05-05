import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict

def get_spotify_client(client_id, client_secret):
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_playlist_tracks(spotify_client, playlist_url):
    playlist = spotify_client.playlist(playlist_url)
    tracks = playlist['tracks']
    return tracks

def get_songs_by_artist(tracks):
    songs_by_artist = defaultdict(list)
    while tracks:
        for item in tracks['items']:
            track = item['track']
            artist = track['artists'][0]['name']
            songs_by_artist[artist].append(track['name'])

        if tracks['next']:
            tracks = sp.next(tracks)
        else:
            tracks = None
    return songs_by_artist

def write_songs_to_file(songs_by_artist, filename):
    with open(filename, 'w') as f:
        for artist, songs in songs_by_artist.items():
            for song in songs:
                f.write(f"{artist} : {song}\n")

def main():
    client_id = "client_id"
    client_secret = "client_secret"
    playlist_url = "playlist_url"
    filename = 'filename.txt'

    spotify_client = get_spotify_client(client_id, client_secret)
    tracks = get_playlist_tracks(spotify_client, playlist_url)
    songs_by_artist = get_songs_by_artist(tracks)
    write_songs_to_file(songs_by_artist, filename)

if __name__ == "__main__":
    main()