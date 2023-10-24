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


def browse_path():
    path = filedialog.askdirectory()  # Show a directory selection dialog
    pathEntry.delete(0, tk.END)  # Clear the current entry
    pathEntry.insert(0, path)  # Set the selected path in the entry
    
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
    root.geometry(f"{550}x{200}")
    root.configure(bg="#141414")
    root.resizable(False,False)

    # Create and add widgets (buttons, labels, etc.)
    # label_style = {
    #     "text": "YOU MP3",
    #     "bg": "#141414",          # Background color
    #     "fg": "white",          # Text color
    #     "font": ("Arial", 12),  # Font family and size
    #     "width": 15,            # Button width
    #     "height": 1,             # Button height
    #     "font": "Lato"
    # }
    # label = tk.Label(root, label_style)
    # label.pack(side="top", padx=10, pady=10)
    
    input_style = {
        "bg": "#212121",          # Background color
        "fg": "white",          # Text color
        "font": ("Arial", 12, "bold"),  # Font family and size
        "width": 38,            # Button width
        "relief": "flat",
        "font": "Lato",
        "insertbackground": "white"
    }
    
    input_style2 = {
        "text": "Download MP3",
        "bg": "#212121",          # Background color
        "fg": "white",          # Text color
        "font": ("Arial", 12, "bold"),  # Font family and size
        "width": 38,            # Button width
        "relief": "flat",
        "font": "Lato",
        "insertbackground": "white"
    }
    titleLabel = tk.Label(root, text="YOU MP3", font=("Arial", 18), bg="#141414", fg="red")
    titleLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    urlLabel = tk.Label(root, text="URL:", font=("Arial", 12), bg="#141414", fg="white")
    urlLabel.grid(row=1, column=0, sticky="w", pady=2, padx=5)
    
    pathLabel = tk.Label(root, text="PATH:", font=("Arial", 12), bg="#141414", fg="white")
    pathLabel.grid(row=2, column=0, sticky="w", pady=2, padx=5)
    
    urlEntry = tk.Entry(root, input_style)
    urlEntry.grid(row=1, column=1, pady=3, padx=5)
    
    pathEntry = tk.Entry(root, input_style2, width=38)
    pathEntry.grid(row=2, column=1, pady=3, )
    
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
    
    browseButton = tk.Button(root, text="BROWSE", bg="#141414", fg="white", command=browse_path)
    browseButton.grid(row=2, column=2)
    
    dlButton = tk.Button(root, button_style)
    dlButton.configure(bg="#c00707")
    dlButton.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    # Start the GUI event loop
    root.mainloop()
    
