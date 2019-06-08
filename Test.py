from YoutubeDownloader import YoutubeDownloader
from Youtube import Youtube
from pytube import YouTube as ABC
API = 'AIzaSyD298lx0cwZkpw8syTGoxC4Fs9ed08zbCw'

downloader = Youtube(API)
# video = downloader.download_video_caption('CeOadxT7kPA','en')
# print(video)
# downloader.download_channel('UCAuUUnT6oDeKwE6v1NGQxug',10,'/home/bachnguyen/Pictures/test',4)
# downloader.download('neCmEbI2VWg','/home/bachnguyen/Documents','test')
abc = ABC('https://www.youtube.com/watch?v=iBa9EoEbb38')
caption = abc.captions.get_by_language_code('en').generate_srt_captions()

f = open("test.srt", "a")
f.write(caption)
f.close()
