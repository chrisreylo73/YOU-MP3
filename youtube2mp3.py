from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import tkinter as tk
from tkinter import filedialog

# Function to download a video from a given URL
def download_youtube_video(url, video_folder_path):
    yt = YouTube(url)
    videoTitle = yt.title
    stream = yt.streams.filter(only_audio=False, file_extension='mp4').first()
    stream.download(video_folder_path)
    return videoTitle

# Function to extract audio from a video
def extract_audio(input_path, output_audio_path):
    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path, codec="mp3")
    audio.close()
    video.close()

# Function to delete a video file
def delete_video(video_path):
    try:
        os.remove(video_path)
    except OSError as e:
        print(f"Error removing file: {e}")

# Function to browse and set the selected path in the path entry field
def browse_path():
    path = filedialog.askdirectory()  # Show a directory selection dialog
    pathEntry.delete(0, tk.END)  # Clear the current entry
    pathEntry.insert(0, path)  # Set the selected path in the entry

# Function to start the download process
def start():
    print("starting")
    youtube_url = urlEntry.get()
    output_audio_path = pathEntry.get()
    video_folder_path = "./Videos"
    videoTitle = download_youtube_video(youtube_url, video_folder_path)
    print(output_audio_path)
    output_audio_path = f"{output_audio_path}/{videoTitle}.mp3"
    print(output_audio_path)
    extract_audio(f"{video_folder_path}/{videoTitle}.mp4", output_audio_path)
    delete_video(f"{video_folder_path}/{videoTitle}.mp4")

if __name__ == "__main__":
    
    # GUI Interface 
    root = tk.Tk()
    root.title("YOU MP3")
    root.geometry(f"{480}x{180}")
    root.configure(bg="#141414")
    root.resizable(False, False)

    titleLabel = tk.Label(root, text="YOU-MP3", font=("Lato", 18, "bold"), bg="#141414", fg="red")
    titleLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    urlLabel = tk.Label(root, text="URL:", font=("Lato", 10), bg="#141414", fg="white")
    urlLabel.grid(row=1, column=0, sticky="w", pady=2, padx=5)

    pathLabel = tk.Label(root, text="PATH:", font=("Lato", 10), bg="#141414", fg="white")
    pathLabel.grid(row=2, column=0, sticky="w", pady=2, padx=5)

    urlEntry = tk.Entry(root, font=("Lato", 10), width="50", relief="flat", bg="#212121", fg="white", insertbackground="white")
    urlEntry.grid(row=1, column=1, pady=3, padx=5)

    pathEntry = tk.Entry(root, font=("Lato", 10), width="50", relief="flat", bg="#212121", fg="white", insertbackground="white")
    pathEntry.grid(row=2, column=1, pady=3)

    browseButton = tk.Button(root, text="BROWSE", bg="#212121", fg="white", relief="flat", command=browse_path)
    browseButton.grid(row=2, column=2)

    dlButton = tk.Button(root, text="Download MP3", bg="#b3261e", fg="white", font=("Lato", 10, "bold"), width=13, relief="flat", command=start)
    dlButton.grid(row=3, column=0, columnspan=2, padx=10, pady=30)

    root.mainloop()
