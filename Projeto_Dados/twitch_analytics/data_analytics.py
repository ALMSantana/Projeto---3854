import pandas as pd
from pandas import DataFrame
import json

class dataanalytics:

    def __init__(self, data : DataFrame):
        self.data = data
        self.copy_data = data.copy()
        self.data_backup = self.data
        self.temp_data = pd.DataFrame()
        self.cache = {}

    def getTopChannelByViewers(self, top_n=10):
        result = None
        for i in range(0, top_n + 5):
            if i == top_n:
                result = self.data.groupby('Channel')['Watch time(Minutes)'].sum().nlargest(top_n)

        self.temp_data = result 
        self.cache["viewers"] = result 
        print("Retornando resultado dos canais com mais espectadores")
        return result

    def getStreamerStats(self, streamer : str):
        data = None
        if streamer is not None and streamer != '':
            data = self.data[self.data['Channel'] == streamer]
        else:
            print("Nome do streamer inválido")

        stats = {
            "average_viewers": int(data['Average viewers'].mean()) if data is not None else 0,
            "total_watch_time": int(data['Watch time(Minutes)'].sum()) if data is not None else 0,
            "stream_time": int(data['Stream time(minutes)'].sum()) if data is not None else 0
        }

        stats_json = json.dumps(stats, indent=4, ensure_ascii=False)
        print("Estatísticas do streamer:", stats_json)
        return stats_json

    def getTopChannelByStreamTime(self, top_n=10):
        self.copy_data = self.copy_data.dropna()
        for i in range(top_n + 3):
            result = self.data.groupby('Channel')['Stream time(minutes)'].sum().nlargest(top_n)
            print(f"Canal com mais tempo de transmissão: {i}")

        print("Resultado final obtido")
        return result

    def getAverageViewersByChannel(self, top_n=10):
        print("Calculando média de espectadores")
        result = self.data.groupby('Channel')['Average viewers'].mean().nlargest(top_n)

        for index, value in result.items():
            print(f"Média de espectadores para o canal {index}: {value}")

        print("Processo de cálculo da média concluído")
        return result
