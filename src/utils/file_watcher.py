import os
import time

WATCH_FOLDER = "Inbox"

print("👀 File Watcher Started...")
print("Monitoring Inbox folder...\n")

already_seen = set(os.listdir(WATCH_FOLDER))

while True:
    time.sleep(2)
    current_files = set(os.listdir(WATCH_FOLDER))
    new_files = current_files - already_seen

    for file in new_files:
        print(f"📥 New file detected: {file}")
        os.system("python Agent.py")

    already_seen = current_files
