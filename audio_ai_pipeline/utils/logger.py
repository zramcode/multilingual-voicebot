import datetime

class Logger:
    @staticmethod
    def log(message : str):
      print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {message}")