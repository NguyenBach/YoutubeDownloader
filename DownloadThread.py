from threading import Thread


class DownloadThread(Thread):

    def __init__(self, thread_name, downloader):
        super().__init__()
        self.thread_name = thread_name
        self.downloader = downloader

    def run(self):
        print('Start download' + self.thread_name)
        self.downloader.download()
