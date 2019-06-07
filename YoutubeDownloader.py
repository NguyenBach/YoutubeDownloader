from pytube import YouTube as Downloader
from Youtube import Youtube


class YoutubeDownloader:
    def __init__(self, api_key):
        self.youtube = Youtube(api_key)
        return

    def download(self, video_id, save_path):
        video_url = self.youtube.get_video_url(video_id)
        downloader = Downloader(video_url)
        downloader.register_on_complete_callback(self.download_complete_action)
        downloader.register_on_progress_callback(self.download_on_progress_action)
        downloader.streams.filter(progressive=True, file_extension='mp4') \
            .order_by('resolution').desc().first().download(output_path=save_path)

    def download_channel(self, channel_id, number_video,save_path):
        videos = self.youtube.get_chanel_video(channel_id,number_video)
        for video in videos:
            video_id = video['id']['videoId']
            self.download(video_id,save_path)

    def download_complete_action(self, stream, file_handle):
        print(' download completd')

    def download_on_progress_action(self, stream, chunk, file_handle, bytes_remaining):
        print(bytes_remaining)
