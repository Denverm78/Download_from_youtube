from fileinput import filename
from PyQt6.QtCore import QThread, pyqtSignal
from pytube import YouTube

# url = 'https://www.youtube.com/watch?v=teEcuWCtySk'


def getNameFile(link):
        global myVideo
        global filename
        global myLink
        myLink = link
        myVideo = YouTube(myLink)
        filename = myVideo.title
        return filename
        
class Downloader(QThread):

    setTotalProgress = pyqtSignal(int)
    setCurrentProgress = pyqtSignal(int)
    succeeded = pyqtSignal()

    def __init__(self, url, filename):
        super().__init__()
        self._url = url
        self._filename = filename

    def progress(self, streams, chunk: bytes, bytes_remaining: int):
        total_size = myVideo.streams.get_highest_resolution().filesize
        last_size = total_size - bytes_remaining
        down_progress = int(last_size/total_size*100)
        self.setCurrentProgress.emit(down_progress)

    def run(self):
        myVideo = YouTube(myLink, on_progress_callback=self.progress)      
        myStreams = myVideo.streams.filter(file_extension = "mp4") 
        myStreams.first().download()
        self.succeeded.emit()
