from pytube import YouTube as Downloader
from Youtube import Youtube
from queue import Queue
from threading import Thread
import time


class YoutubeDownloader:
    def __init__(self, api_key):
        self.youtube = Youtube(api_key)
        return

    def download(self, video_id, save_path, filename):
        video_url = self.youtube.get_video_url(video_id)
        downloader = Downloader(video_url)
        downloader.register_on_complete_callback(self.download_complete_action)
        downloader.register_on_progress_callback(self.download_on_progress_action)
        stream = downloader.streams.filter(progressive=True, file_extension='mp4') \
            .order_by('resolution').desc().first()
        stream.download(output_path=save_path, filename=filename)
        return stream

    def download_queue(self, queue):
        while not queue.empty():
            download_info = queue.get()
            try:
                self.download(download_info['video_id'], download_info['save_path'], download_info['filename'])
            except:
                queue.put(download_info)
            time.sleep(10)
            queue.task_done()

    def download_channel(self, channel_id, number_video, save_path, num_threads=2):
        videos = self.youtube.get_chanel_video(channel_id, number_video)
        queue = Queue(number_video)
        for video in videos:
            download_info = {
                "video_id": video['id']['videoId'],
                "save_path": save_path,
                "filename": video['snippet']['title']
            }
            queue.put(download_info)
        for i in range(num_threads):
            worker = Thread(name='', target=self.download_queue, args=(queue,))
            worker.setDaemon(True)
            worker.start()

        queue.join()

    def download_playlist(self, playlist_id, save_path, number_video, num_threads=3):
        videos = self.youtube.get_playlist_video(playlist_id, number_video)
        queue = Queue(number_video)
        for video in videos:
            download_info = {
                "video_id": video['id']['videoId'],
                "save_path": save_path,
                "filename": video['snippet']['title']
            }
            queue.put(download_info)
        for i in range(num_threads):
            worker = Thread(name='', target=self.download_queue, args=(queue,))
            worker.setDaemon(True)
            worker.start()
        queue.join()

    def download_complete_action(self, stream, file_handle):
        print(' download completd')

    def download_on_progress_action(self, stream, chunk, file_handle, bytes_remaining):
        print('.')
