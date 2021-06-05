from pytube import Playlist

link = input("Saisie le lien de la playlist : ")

playlist = Playlist(link)

# print("Number of videos for downloads: " + len(playlist.videos_urls))

for video in playlist.videos:
  video.streams.first().download('./Video')
  print("download Done!!!")