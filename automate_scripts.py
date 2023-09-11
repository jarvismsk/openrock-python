import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

# Path to the directory containing user_response.txt
directory_to_watch = os.path.dirname(__file__)

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("user_response.txt"):
            print("user_response.txt has been modified. Running scripts...")
            # Run stockcode.py and capture the output
            stockcode_output = subprocess.run(["python", "stockcode.py"], text=True, capture_output=True)
            print("Output of stockcode.py:")
            print(stockcode_output.stdout)
            
            # Run ml.py and capture the output
            ml_output = subprocess.run(["python", "ml.py"], text=True, capture_output=True)
            print("Output of ml.py:")
            print(ml_output.stdout)
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
