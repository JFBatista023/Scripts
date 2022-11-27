from sys import argv
from pathlib import Path
from pytube import YouTube

link = argv[1]
path = Path(argv[2])

yt = YouTube(link)
try:
    yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(output_path=path)
    print("Video downloaded successfully!")
except:
    print("Something went wrong! Check the link and file destination path.")

    
