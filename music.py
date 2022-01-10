import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="0bf85a16f6994a499457a25e3bdf9dba",
                                                           client_secret="b2eedcad22cb40cdae84ff4357016ab6"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
