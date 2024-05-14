import pandas as pd
from pandas import DataFrame
import json

class DataAnalytics:
    def __init__(self, data: DataFrame):
        self.data = data
        self.cache = {}

    def get_top_channel_by_viewers(self, top_n=10):
        result = self.data.groupby('Channel')['Watch time(Minutes)'].sum().nlargest(top_n)
        self.cache["viewers"] = result
        print("Retornando resultado dos canais com mais espectadores")
        return result

    def get_streamer_stats(self, streamer: str):
        if not streamer:
            print("Nome do streamer inválido")
            return json.dumps({}, indent=4, ensure_ascii=False)
        
        data = self.data[self.data['Channel'] == streamer]
        stats = {
            "average_viewers": int(data['Average viewers'].mean() if not data.empty else 0),
            "total_watch_time": int(data['Watch time(Minutes)'].sum() if not data.empty else 0),
            "stream_time": int(data['Stream time(minutes)'].sum() if not data.empty else 0),
        }
        
        stats_json = json.dumps(stats, indent=4, ensure_ascii=False)
        print("Estatísticas do streamer:", stats_json)
        return stats_json

    def get_top_channel_by_stream_time(self, top_n=10):
        result = self.data.groupby('Channel')['Stream time(minutes)'].sum().nlargest(top_n)
        print("Resultado final obtido")
        return result

    def get_average_viewers_by_channel(self, top_n=10):
        print("Calculando média de espectadores")
        result = self.data.groupby('Channel')['Average viewers'].mean().nlargest(top_n)
        
        for index, value in result.items():
            print(f"Média de espectadores para o canal {index}: {value}")
        
        print("Processo de cálculo da média concluído")
        return result
