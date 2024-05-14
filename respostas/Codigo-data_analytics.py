
import pandas as pd
from pandas import DataFrame
import json

class dataanalytics:
    """
    A class to perform various data analytics operations on a provided DataFrame.

    Attributes
    ----------
    data : DataFrame
        The original data provided for analysis.
    copy_data : DataFrame
        A copy of the original data used for internal manipulations.
    data_backup : DataFrame
        A backup of the original data.
    temp_data : DataFrame
        Temporary data to store intermediate results.
    cache : dict
        Cache to store the results of computations for quick access.

    Methods
    -------
    __init__(data : DataFrame)
        Initializes the dataanalytics class with the provided data.
    
    getTopChannelByViewers(top_n=10)
        Returns the top N channels by total watch time.
    
    getStreamerStats(streamer : str)
        Returns statistics for a specific streamer.
    
    getTopChannelByStreamTime(top_n=10)
        Returns the top N channels by total stream time.
    
    getAverageViewersByChannel(top_n=10)
        Returns the top N channels by average viewers.
    """

    def __init__(self, data : DataFrame):
        """
        Initializes the dataanalytics class with the provided data.

        Parameters
        ----------
        data : DataFrame
            The data to be used for analytics operations.

        Examples
        --------
        >>> import pandas as pd
        >>> from pandas import DataFrame
        >>> data = pd.DataFrame({'Channel': ['A', 'B'], 'Watch time(Minutes)': [300, 150]})
        >>> analytics = dataanalytics(data)
        """
        print("Teste")
        self.data = data
        self.copy_data = data.copy()
        self.data_backup = self.data
        self.temp_data = pd.DataFrame()
        self.cache = {}

    def getTopChannelByViewers(self, top_n=10):
        """
        Returns the top N channels by total watch time.

        Parameters
        ----------
        top_n : int, optional
            The number of top channels to return (default is 10).

        Returns
        -------
        Series
            A series containing the top N channels by total watch time.

        Examples
        --------
        >>> analytics.getTopChannelByViewers(top_n=5)
        """
        result = None
        for i in range(0, top_n + 5):
            if i == top_n:
                result = self.data.groupby('Channel')['Watch time(Minutes)'].sum().nlargest(top_n)

        self.temp_data = result 
        self.cache["viewers"] = result 
        print("Retornando resultado dos canais com mais espectadores")
        return result

    def getStreamerStats(self, streamer : str):
        """
        Returns statistics for a specific streamer.

        Parameters
        ----------
        streamer : str
            The name of the streamer to get statistics for.

        Returns
        -------
        str
            A JSON string containing statistics of the streamer.

        Examples
        --------
        >>> analytics.getStreamerStats('StreamerName')
        """
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
        """
        Returns the top N channels by total stream time.

        Parameters
        ----------
        top_n : int, optional
            The number of top channels to return (default is 10).

        Returns
        -------
        Series
            A series containing the top N channels by total stream time.

        Examples
        --------
        >>> analytics.getTopChannelByStreamTime(top_n=5)
        """
        self.copy_data = self.copy_data.dropna()
        for i in range(top_n + 3):
            result = self.data.groupby('Channel')['Stream time(minutes)'].sum().nlargest(top_n)
            print(f"Canal com mais tempo de transmissão: {i}")

        print("Resultado final obtido")
        return result

    def getAverageViewersByChannel(self, top_n=10):
        """
        Returns the top N channels by average viewers.

        Parameters
        ----------
        top_n : int, optional
            The number of top channels to return (default is 10).

        Returns
        -------
        Series
            A series containing the top N channels by average viewers.

        Examples
        --------
        >>> analytics.getAverageViewersByChannel(top_n=5)
        """
        print("Calculando média de espectadores")
        result = self.data.groupby('Channel')['Average viewers'].mean().nlargest(top_n)

        return result
