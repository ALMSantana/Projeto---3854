import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)

    def get_data(self):
        return self.data