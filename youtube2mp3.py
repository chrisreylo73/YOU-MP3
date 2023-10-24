import time
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import tkinter as tk
from tkinter import filedialog


def download_youtube_video(url, video_folder_path):
    yt = YouTube(url)
    videoTitle = yt.title
    stream = yt.streams.filter(only_audio=False, file_extension='mp4').first()
    stream.download(video_folder_path);
    return videoTitle

def extract_audio(input_path, output_audio_path):
    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path, codec="mp3")
    audio.close()
    video.close()

def delete_video(video_path):
    try:
        os.remove(video_path)
    except OSError as e:
        print(f"Error removing file: {e}")
      
if __name__ == "__main__":
    # home = "https://www.youtube.com/watch?v=iB3K1f7CFbo"
    # youtube_url = home
    # video_folder_path = "./Videos"
    # videoTitle = download_youtube_video(youtube_url, video_folder_path)
    # output_audio_path = f"./Audio/{videoTitle}.mp3"
    # extract_audio(f"{video_folder_path}/{videoTitle}.mp4", output_audio_path)
    # delete_video(f"{video_folder_path}/{videoTitle}.mp4")
    root = tk.Tk()
    root.title("YOU MP3")
    root.geometry(f"{500}x{200}")
    root.configure(bg="#141414")

    # Create and add widgets (buttons, labels, etc.)
    label_style = {
        "text": "YOU MP3",
        "bg": "#141414",          # Background color
        "fg": "white",          # Text color
        "font": ("Arial", 12),  # Font family and size
        "width": 15,            # Button width
        "height": 1,             # Button height
        "font": "Lato"
    }
    label = tk.Label(root, label_style)
    label.pack(side="top", padx=10, pady=10)
    button_style = {
        "text": "Download MP3",
        "bg": "#c00707",          # Background color
        "fg": "white",          # Text color
        "font": ("Arial", 12),  # Font family and size
        "width": 15,            # Button width
        "height": 1,             # Button height
        "relief": "flat",
        "font": "Lato"
        
    }
    button = tk.Button(root, **button_style)
    button.configure(bg="#c00707")
    button.pack()

    # Start the GUI event loop
    root.mainloop()
    
