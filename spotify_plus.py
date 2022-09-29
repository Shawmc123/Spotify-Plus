import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import itertools

# Scope controls what permissions I need for the associated Spotify account
scope = "ugc-image-upload, user-modify-playback-state, user-read-playback-state, user-read-currently-playing, " \
        "user-follow-modify, user-follow-read, user-read-recently-played, user-read-playback-position, user-top-read, " \
        "playlist-read-collaborative, playlist-modify-public, playlist-read-private, playlist-modify-private, " \
        "app-remote-control, streaming, user-read-email, user-read-private, user-library-modify, user-library-read "
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


# Given a list of song queues, it will queue one song from each of the lists at a time
# This allows people to queue up all their songs without having one person's songs play at once before another person's
def create_queue(initial_songs_list):
    # Separates all the songs by comma
    songs = [i.split(',') for i in initial_songs_list]
    for i in range(len(songs)):
        for j in range(len(songs)):
            try:
                song_id = sp.search(q='track:' + songs[j][i], type='track')['tracks']['items'][0]['id']
                sp.add_to_queue(song_id)
            except IndexError:
                continue


# Really like the artist you're listening to? This will queue another song in your playlist by the current artist
# TODO: Error when its your liked songs, so in this case use the users library
def queue_same_artist():
    currently_playing = sp.currently_playing()
    current_song = sp.current_user_playing_track()['item']['uri']
    current_playlist = currently_playing['context']['uri']
    current_artist = currently_playing['item']['artists'][0]['uri']
    tracks = get_playlist_tracks(current_playlist)
    playlist_dict = {}

    for item in tracks:
        playlist_dict[item['track']['uri']] = item['track']['artists'][0]['uri']

    available_songs = [i for i, j in playlist_dict.items() if j == current_artist]
    available_songs.remove(current_song)

    if available_songs:
        sp.add_to_queue(available_songs[random.randint(0, len(available_songs) - 1)])
    else:
        print("There is only one song by this artist and you're listening to it!")


# Returns the playlist tracks, including albums and artists
def get_playlist_tracks(playlist_id):
    results = sp.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


# Returns a list of the recently played track uris
def get_recent_tracks(amount):
    recently_played = sp.current_user_recently_played(limit=amount)['items']
    track_uris = []
    for i in range(len(recently_played)):
        track_uris.append(recently_played[i]['track']['uri'])
    return track_uris


# Creates a playlist based on the last 5 songs you listened to
def current_mood_playlist():
    track_uris = get_recent_tracks(5)
    recommendations = sp.recommendations(seed_tracks=track_uris)['tracks']
    recommendation_uris = []
    for i in recommendations:
        recommendation_uris.append(i['uri'])
    sp.playlist_add_items('spotify:playlist:4XNejf2Zjyy6cm7nie3NPq', recommendation_uris)


# Not finished, but should give you a graph of the features of your last x songs
# Limit of 100
def make_graph(amount):
    track_uris = get_recent_tracks(amount)
    for item in track_uris:
        track_uris.append(item['track']['uri'])
    print(track_uris)
    stats = sp.audio_features(track_uris[:100])
    print(len(stats))

    audio_features = []
    for stat in ['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']:
        entry = stat + ': '
        total = 0
        for song in stats:
            total += song[stat]
            print(song[stat], total)
        audio_features.append(entry + str(total/amount))
    print(audio_features)



if __name__ == '__main__':
    #create_queue(['Never gonna give you up, tubthumping', 'blinding lights, long hard times to come', 'sweet child of mine, thunderstruck'])
    queue_same_artist()
    #current_mood_playlist()
    #make_graph(20)

