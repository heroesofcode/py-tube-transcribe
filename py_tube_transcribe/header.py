from rich.progress import track
from time import sleep

class Header:

    def info(self):
        self.progress_data()

    def progress_data(self):
        for _ in track(range(100), description='[green]Processing data'):
            sleep(0.03)