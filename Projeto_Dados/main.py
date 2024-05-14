from twitch_analytics import DataLoader, dataanalytics, DataVisualizer, ConsoleInterface

def main():
    filepath = './Projeto_Dados/base_dados/twitchdata-update.csv'
    data_loader = DataLoader(filepath)
    analytics = dataanalytics(data_loader.get_data())
    visualizer = DataVisualizer(analytics)
    console_interface = ConsoleInterface(data_loader, analytics, visualizer)
    console_interface.run()

if __name__ == "__main__":
    main()