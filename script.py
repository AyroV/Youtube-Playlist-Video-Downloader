from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
import os

#FILES WILL BE DOWNLOADED WHERE THE SCRIPT IS RUN AT IN TERMINAL

print("1 - Download a Video From Youtube")
print("2 - Download a Playlist From Youtube")
operation_type_1 = input("Choice: ")

print("Do you want to convert it/them to mp3? (Y\\N)")
operation_type_2 = input("Choice: ")

if(operation_type_2.capitalize() != "Y" and operation_type_2.capitalize() != "N"):
    print("Wrong Input, Terminating...")
    exit()

if(operation_type_1 == "1"):
    video_link = input("Video Link: ")
    try:
        video = YouTube(video_link)
    except:
        print("Wrong Input. Terminating...")
        exit()

    try:
        mp4_file = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    except:
        print("Something is wrong with the video, it is probably unavailable. Terminating...")
        exit()
    if(operation_type_2.capitalize() == "Y"):
        mp3_file = mp4_file.split('\\')[-1].split('.')[0] + ".mp3"

        videoClip = VideoFileClip(mp4_file)
        audioClip = videoClip.audio

        audioClip.write_audiofile(mp3_file)
        audioClip.close()
        videoClip.close()

        choice = input("Do you want to remove 'EVERY'.mp4 file in this directory? (Y\\N): ")
        if(choice.capitalize() == "Y"):
        dir_name = os.path.dirname(os.path.realpath(__file__))
        test = os.listdir(dir_name)
        for item in test:
            if item.endswith(".mp4"):
                os.remove(os.path.join(dir_name, item))
        
        else:
            print("Wrong input, no files were removed.")
            exit()

elif(operation_type_1 == "2"):
    playlist_link = input("Playlist Link: ")
    try:
        playlist = Playlist(playlist_link)
    except:
        print("Wrong Input. Terminating...")
        exit()

    for video in playlist.videos:
        try:
            mp4_file = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        except Exception as e:
            print("Something is wrong with the video, it is probably unavailable. Skipping this video.")
            print(e)
            print()
            continue
        if(operation_type_2.capitalize() == "Y"):
            mp3_file = mp4_file.split('\\')[-1].split('.')[0] + ".mp3"

            videoClip = VideoFileClip(mp4_file)
            audioClip = videoClip.audio

            audioClip.write_audiofile(mp3_file)
            audioClip.close()
            videoClip.close()

    choice = input("Do you want to remove 'EVERY'.mp4 file in this directory? (Y\\N): ")
    if(choice.capitalize() == "Y"):
    dir_name = os.path.dirname(os.path.realpath(__file__))
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".mp4"):
            os.remove(os.path.join(dir_name, item))

    else:
        print("Wrong input, no files were removed.")
        exit()

else:
    print("Wrong Input. Terminating...")
    exit()
