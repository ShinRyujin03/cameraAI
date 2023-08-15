import time

class BacklogSaver:
    def __init__(self):
        self.backlog = []

    def add_to_backlog(self, log_message):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.backlog.append(f"[{timestamp}] {log_message}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for entry in self.backlog:
                file.write(entry + '\n')

    def clear_backlog(self):
        self.backlog = []

# Create an instance of BacklogSaver
backlog_saver = BacklogSaver()
