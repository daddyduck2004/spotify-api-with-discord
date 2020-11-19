from spotify import Spotify

client = Spotify("discord_token") #discord token connected to spotify.

player = client.getCurrentPlaying().json()
songName = player["item"]["name"]
songDuration = player["item"]["duration_ms"] / 1000 #return in ms and convert to second.
songProgress = player["progress_ms"] / 1000 #return in ms and convert to second.
