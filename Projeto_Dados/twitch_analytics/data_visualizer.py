import matplotlib.pyplot as plt
from .data_analytics import dataanalytics

class DataVisualizer:
    def __init__(self, analytics : dataanalytics):
        self.analytics = analytics

    def plot_top_channel_by_viewers(self, top_n=10):
        data = self.analytics.getTopChannelByViewers(top_n)
        plt.figure(figsize=(10, 8))
        data.plot(kind='bar', color='blue')
        plt.title('Top Canais por Tempo de Visualização')
        plt.xlabel('Canal')
        plt.ylabel('Tempo de Visualização (Minutos)')
        plt.savefig('./Projeto_Dados/data_view/top_channel_by_viewers.png', bbox_inches='tight')
        plt.show()

    def plot_top_channel_by_stream_time(self, top_n=10):
        data = self.analytics.getTopChannelByStreamTime(top_n)
        plt.figure(figsize=(10, 8))
        data.plot(kind='bar', color='green')
        plt.title('Canals com Mais Tempo de Transmissão')
        plt.xlabel('Canal')
        plt.ylabel('Tempo de Transmissão (Minutos)')
        plt.savefig('./Projeto_Dados/data_view/top_channel_by_stream_time.png', bbox_inches='tight')
        plt.show()

    def plot_average_viewers_by_channel(self, top_n=10):
        data = self.analytics.getAverageViewersByChannel(top_n)
        plt.figure(figsize=(10, 8))
        data.plot(kind='bar', color='red')
        plt.title('Média de Espectadores por Canal')
        plt.xlabel('Canal')
        plt.ylabel('Média de Espectadores')
        plt.savefig('./Projeto_Dados/data_view/average_viewers_by_channel.png', bbox_inches='tight')
        plt.show()