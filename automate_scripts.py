import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import run
from flask import Flask  # Import Flask

# Path to the directory containing user_response.txt
directory_to_watch = os.path.join(os.path.dirname(__file__))
app = Flask(__name__)  # Create a Flask app

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("user_response.txt"):
            print("user_response.txt has been modified. Running scripts...")
            run(["python", "stockcode.py"])
            run(["python", "ml.py"])
            print("Scripts executed.")

if __name__ == "__main__":
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

