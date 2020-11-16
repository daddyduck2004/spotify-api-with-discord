import requests

class Spotify:
    def __init__(self, discord_token):
        self.discord_token = discord_token
        self.reissueAccessToken(discord_token=discord_token, appNo=0)

    def reissueAccessToken(self, discord_token: str, appNo: int = 0):
        response = requests.get(url="https://discord.com/api/v8/users/@me/connections", headers={"authorization": discord_token}).json()
        self.spotifyAppId = [app for app in response if app["type"] == "spotify"][appNo]["id"]
        response = requests.get(url=f"https://discord.com/api/v8/users/@me/connections/spotify/{self.spotifyAppId}/access-token", headers={"authorization": discord_token})
        self.access_token = response.json()["access_token"]

    def getDevices(self):
        url = "https://api.spotify.com/v1/me/player/devices"
        response = requests.get(url=url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def pause(self):
        url = "https://api.spotify.com/v1/me/player/pause"
        response = requests.put(url=url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def next(self):
        url = "https://api.spotify.com/v1/me/player/next"
        response = requests.post(url=url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def previous(self):
        url = "https://api.spotify.com/v1/me/player/previous"
        response = requests.post(url=url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response

    def play(self, track, device_id):
        url = f"https://api.spotify.com/v1/me/player/play?device_id={device_id}"
        data = {
            "uris": [f"spotify:track:{track}"]
        }
        response = requests.put(url=url, headers={"Authorization": f"Bearer {self.access_token}"}, json=data)
        return response

    def getCurrentPlaying(self):
        url = "https://api.spotify.com/v1/me/player/currently-playing"
        response = requests.get(url=url, headers={"Authorization": f"Bearer {self.access_token}"})
        return response
