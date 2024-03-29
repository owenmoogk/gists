import spotipy
from bs4 import BeautifulSoup
import requests
from icecream import ic
import os
from mutagen.easyid3 import EasyID3
from dotenv import load_dotenv
load_dotenv()


class Spotify:

	def authenticate_spotify(self):
		sp = spotipy.Spotify(
			auth_manager=spotipy.SpotifyOAuth(
				scope="playlist-modify-private",
				redirect_uri="http://example.com",
				client_id=os.getenv("CLIENT_ID"),
				client_secret=os.getenv("CLIENT_SECRET"),
				show_dialog=True,
				cache_path="token.txt"
			)
		)
		self.user_id = sp.current_user()["id"]
		self.sp = sp

	def getSong(self, title, artist):
		result = self.sp.search(q=f"track:{title} artist:{artist}", type='track')
		# sortedResults = sorted(result["tracks"]["items"], key=lambda x: x["popularity"], reverse=True)
		sortedResults = result["tracks"]["items"]
		return sortedResults[0] if len(sortedResults) > 0 else None

	def getSongs(self, array):
		spotifySongs = []
		for title, artist in array:
			song = self.getSong(title, artist)
			if not song or song["name"] != title or song["artists"][0]["name"] != artist:
				with open("test.txt", 'a+') as file:
					file.seek(0, 2)
					file.write('\n' + title + " - " + artist)
			if song:
				spotifySongs.append(song["uri"])
			else:
				print(title, "--", artist)

		return spotifySongs

		
	def spotify_create_play_list(self, songList):
		play_list = self.sp.user_playlist_create(self.user_id, "My favourite Playlist", public=False, collaborative=False, description="")
		for song in songList:
			self.sp.playlist_add_items(play_list['id'], [song], None)


spotify = Spotify()
spotify.authenticate_spotify()

MUSIC_PATH = r"C:\Users\owenm\Music\music\Music on Devices"
songs_info = []

for file_name in os.listdir(MUSIC_PATH):
	if file_name.endswith(".mp3"):  # Considering only MP3 files
		file_path = os.path.join(MUSIC_PATH, file_name)
		try:
			audio = EasyID3(file_path)
			song_name = file_name.split(".mp3")[0]
			artist = audio['artist'][0] if 'artist' in audio else 'Unknown Artist'
			songs_info.append((song_name, artist))
		except Exception as e:
			print(f"Error processing file {file_name}: {e}")

spotifySongs = spotify.getSongs(songs_info)
spotify.spotify_create_play_list(spotifySongs)