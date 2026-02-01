class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)

    def print_logs(self):
        if len(self.logs) == 0:
            print("No logs.")
            return

        print("===== LOGS =====")
        for i in range(len(self.logs)):
            print(f"{i + 1}. {self.logs[i]}")
        print("================")

    def save_to_file(self, filename="log.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for log in self.logs:
                f.write(log + "\n")
