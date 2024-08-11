# import os
# from os import rename
# from os.path import splitext, exists, join
# import sys
# import time
# import logging
# import watchdog
# from watchdog.observers import Observer
# from watchdog.events import LoggingEventHandler
# from shutil import move


# source_dir = "C:\\Users\\patel\\Downloads"
# dest_dir_images = "C:\\Users\\patel\\Desktop\\Downloded Images"
# dest_dir_videos = "C:\\Users\\patel\\Desktop\\Downloded videos"
# video_extensions = [".mp4",".mov",".mpv"]
# image_extensions = [".jpeg",".jpg",".png"]

# def move_file(dest, entry, name):
#     if exists(f"{dest}/{name}"):
#         unique_name = make_unique(dest, name)
#         oldName = join(dest, name)
#         newName = join(dest, unique_name)
#         rename(oldName, newName)
#     move(entry, dest)

# def make_unique(dest, name):
#     filename, extension = splitext(name)
#     counter = 1
#     # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
#     while exists(f"{dest}/{name}"):
#         name = f"{filename}({str(counter)}){extension}"
#         counter += 1

#     return name


# class MoverHandler(LoggingEventHandler):
   
#     def on_modified(self, event):
#         with os.listdir(source_dir) as entries:
#             for entry in entries:
#                 name = entry.name
#           
#                 self.check_video_files(entry, name)
#                 self.check_image_files(entry, name)
#                

#     def check_video_files(self, entry, name):  
#         for video_extension in video_extensions:
#             if name.endswith(video_extension) or name.endswith(video_extension.upper()):
#                 move_file(dest_dir_videos, entry, name)
#                 logging.info(f"Moved video file: {name}")

#     def check_image_files(self, entry, name):  
#         for image_extension in image_extensions:
#             if name.endswith(image_extension) or name.endswith(image_extension.upper()):
#                 move_file(dest_dir_images, entry, name)
#                 logging.info(f"Moved image file: {name}")
            
    


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = "C:\\Users\\patel\\Downloads"
#     event_handler = MoverHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()


import os
from os import rename
from os.path import splitext, exists, join
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from shutil import move

source_dir = "C:\\Users\\patel\\Downloads"
dest_dir_images = "C:\\Users\\patel\\Desktop\\Downloded Images"
dest_dir_videos = "C:\\Users\\patel\\Desktop\\Downloaded videos"
video_extensions = [".mp4", ".mov", ".mpv"]
image_extensions = [".jpeg", ".jpg", ".png"]

def move_file(dest, entry, name):
    if exists(join(dest, name)):
        unique_name = make_unique(dest, name)
        entry = join(dest, name)  # Update entry to the correct path
    move(entry, dest)

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(join(dest, name)):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

class MoverHandler(LoggingEventHandler):
    def on_modified(self, event):
        for entry in os.listdir(source_dir):
            entry_path = join(source_dir, entry)
            if os.path.isfile(entry_path):
                self.check_video_files(entry_path, entry)
                self.check_image_files(entry_path, entry)

    def check_video_files(self, entry, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_videos, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_images, entry, name)
                logging.info(f"Moved image file: {name}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
