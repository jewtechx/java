import pytube
from sys import argv

link = argv[1]

yt = pytube.YouTube(link)

print(f"title: {yt.title}")
print(f"author: {yt.author}")

yd = yt.streams.get_lowest_resolution()
yd.download('/Users/JewTech - X/Music/Works/Python/pytube')