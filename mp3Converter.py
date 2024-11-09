import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable
from pytube.innertube import _default_clients
from pytube import cipher
import re
from moviepy.editor import AudioFileClip
import os

# client version settings

_default_clients["ANDROID"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["ANDROID_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"]["context"]["client"]["clientVersion"] = "6.41"
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


def get_throttling_function_name(js: str) -> str:
    function_patterns = [
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
    ]
    for pattern in function_patterns:
        regex = re.compile(pattern)
        function_match = regex.search(js)
        if function_match:
            if len(function_match.groups()) == 1:
                return function_match.group(1)
            idx = function_match.group(2)
            if idx:
                idx = idx.strip("[]")
                array = re.search(
                    r'var {nfunc}\s*=\s*(\[.+?\]);'.format(
                        nfunc=re.escape(function_match.group(1))),
                    js
                )
                if array:
                    array = array.group(1).strip("[]").split(",")
                    array = [x.strip() for x in array]
                    return array[int(idx)]
    raise RegexMatchError(
        caller="get_throttling_function_name", pattern="multiple"
    )


cipher.get_throttling_function_name = get_throttling_function_name


# Download logic

def start_download():
    youtube_link = link.get()
    print(f"URL entered: {youtube_link}")
    try:
        youtube_object = YouTube(youtube_link)
        print(f"Video Title: {youtube_object.title}")
        audio_stream = youtube_object.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download()

        # Convert to mp3 using moviepy
        audio_clip = AudioFileClip(audio_file)
        mp3_file = os.path.splitext(audio_file)[0] + ".mp3"
        audio_clip.write_audiofile(mp3_file)
        audio_clip.close()

        # Remove the original audio file
        os.remove(audio_file)

        print("Download and conversion to MP3 complete!")
    except (Exception, VideoUnavailable, RegexMatchError) as e:
        print(f"Error: {e}")


# GUI Appearance
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("Dark")

# Application window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader")

# UI
title = customtkinter.CTkLabel(app, text="Enter YouTube URL")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

app.mainloop()
