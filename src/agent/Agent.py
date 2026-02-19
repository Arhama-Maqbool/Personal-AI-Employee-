import os
import time
from datetime import datetime

BASE_PATH = "D:/AI-EMPLOYEE"
TASK_FILE = os.path.join(BASE_PATH, "TASKS.md")
LOG_FOLDER = os.path.join(BASE_PATH, "LOGS")

def log_action(message):
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_FOLDER, f"{today}.log")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")

def process_tasks():
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "Status: PENDING" in content:
        print("⚡ Processing Pending Task...")
        log_action("Processing pending task.")

        # Demo: mark first PENDING as COMPLETED
        updated_content = content.replace("Status: PENDING", "Status: COMPLETED", 1)

        with open(TASK_FILE, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print("✅ Task marked as COMPLETED.")
        log_action("Task marked as COMPLETED.")

    else:
        print("✅ No pending tasks found.")
        log_action("No pending tasks found.")

def agent_loop():
    print("🚀 Digital FTE v1 is running...\n")

    while True:
        process_tasks()
        time.sleep(20)  # 20 seconds for demo

if __name__ == "__main__":
    agent_loop()
