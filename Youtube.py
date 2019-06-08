import googleapiclient.discovery
import googleapiclient.errors
from pytube import YouTube


class Youtube:
    def __init__(self, api_key):
        api_service_name = "youtube"
        api_version = "v3"
        self.youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=api_key)

    def get_chanel_video(self, channel_id, max_result):
        request = self.youtube.search().list(
            part='snippet',
            channelId=channel_id,
            maxResults=max_result
        )
        response = request.execute()
        return response['items']

    def get_video_url(self, id):
        return 'https://www.youtube.com/watch?v=' + id

    def get_video_detail(self, video_id):
        request = self.youtube.videos().list(
            part='snippet',
            id=video_id
        )
        return request.execute()['items']

    def get_playlist_video(self, playlist_id, max_video):
        request = self.youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=max_video
        )
        response = request.execute()
        return response['items']

    def get_video_caption_info(self, video_id):
        request = self.youtube.captions().list(
            part='snippet',
            videoId=video_id
        )
        return request.execute()['items']

    def get_video_caption(self, video_id):
        url = self.get_video_url(video_id)
        pytube = YouTube(url)
        caption = pytube.captions.get_by_language_code('en').generate_srt_captions()
        return caption
