from pytube import Playlist

link = input("Enter the link of the playlist : ")

p = Playlist(link)
# p = yt = YouTube(link)

# print(p.get_videos())

print(f'Downloading: {p.title}')

for video in p.videos:
    video.streams.filter(res="720p").first().download('./Video')

# for url in p.video_urls[:3]:
#  print(url)