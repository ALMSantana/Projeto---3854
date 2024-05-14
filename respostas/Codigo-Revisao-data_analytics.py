
import pandas as pd
import json

class DataAnalytics:

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def get_top_channel_by_viewers(self, top_n=10):
        """
        Retorna os top_n canais por watch time (em minutos).
        """
        result = self.data.groupby('Channel')['Watch time(Minutes)'].sum().nlargest(top_n)
        print("Retornando resultado dos canais com mais espectadores")
        return result

    def get_streamer_stats(self, streamer: str):
        """
        Retorna as estatísticas do streamer no formato JSON.
        """
        data = None
        if streamer:
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

    def get_top_channel_by_stream_time(self, top_n=10):
        """
        Retorna os top_n canais por tempo de transmissão (em minutos).
        """
        result = self.data.groupby('Channel')['Stream time(minutes)'].sum().nlargest(top_n)
        print("Resultado final obtido")
        return result

    def get_average_viewers_by_channel(self, top_n=10):
        """
        Retorna a média de espectadores dos top_n canais.
        """
        result = self.data.groupby('Channel')['Average viewers'].mean().nlargest(top_n)
        print("Calculando média de espectadores")
        return result
