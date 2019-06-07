
import googleapiclient.discovery
import googleapiclient.errors




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
