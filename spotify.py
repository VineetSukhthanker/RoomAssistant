import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

# Shows playing devices
res = sp.devices()
pprint(res)

sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])
