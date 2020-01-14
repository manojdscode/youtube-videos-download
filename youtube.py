#python script to download videos automatically

#Importing necessary library
import pytube


url= 'Put the full url here'

video = pytube.Youtube(url)
youtube = video.streams.first()
youtube.Download(r'Put the address where you want to store the video.')