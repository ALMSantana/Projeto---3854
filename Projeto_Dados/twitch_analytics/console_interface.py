from .data_analytics import dataanalytics
from .data_loader import DataLoader
from .data_visualizer import DataVisualizer

class ConsoleInterface:
    def __init__(self, data_loader : DataLoader, analytics : dataanalytics, visualizer : DataVisualizer):
        self.data_loader = data_loader
        self.analytics = analytics
        self.visualizer = visualizer

    def run(self):
        while True:
            print("\nOpções:")
            print("1. Mostrar o top de canais por espectadores")
            print("2. Mostrar estatísticas de um streamer")
            print("3. Mostrar canais com mais tempo de transmissão")
            print("4. Mostrar a média de espectadores por canal")
            print("5. Sair")
            choice = input("Digite sua escolha: ")

            if choice == '1':
                self.visualizer.plot_top_channel_by_viewers()
                print("Gráfico gerado.")
            elif choice == '2':
                streamer_name = input("Digite o nome do streamer: ")
                stats = self.analytics.getStreamerStats(streamer_name)
                print("Estatísticas do Streamer:", stats)
            elif choice == '3':
                self.visualizer.plot_top_channel_by_stream_time()
                print("Gráfico gerado.")
            elif choice == '4':
                self.visualizer.plot_average_viewers_by_channel()
                print("Gráfico gerado.")
            elif choice == '5':
                print("Saindo do programa.")
                break
            else:
                print("Escolha inválida. Por favor, tente novamente.")