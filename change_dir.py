from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[1].lower() == "mp4" or extension[1].lower() == "avi"):
                file = folder_track + "/" +filename
                new_path = video_folder_dest + "/" + filename
                os.rename(file, new_path)


folder_track = '/Users/katya/Downloads'
video_folder_dest = '/Users/katya/Downloads/video'

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
