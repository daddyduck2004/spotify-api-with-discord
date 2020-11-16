from spotify import Spotify

client = Spotify("discord_token") #discord token connected to spotify.

player = client.getCurrentPlaying().json()
songName = player["item"]["name"]
songDuration = player["item"]["duration_ms"] / 1000 #return in ms but multiply 1000 to get second.
songProgress = player["progress_ms"] / 1000 #return in ms but multiply 1000 to get second.
