import pandas as pd
from pandas import DataFrame
import json


class DataAnalytics:
    def __init__(self, data: DataFrame):
        """ Initialize DataAnalytics with a DataFrame """
        print("Teste")
        self.data = data
        self.temp_data = pd.DataFrame()
        self.cache = {}

    def get_top_channel_by_viewers(self, top_n=10):
        """
        Get the top channels by viewers.

        Parameters:
        top_n (int): Number of top channels to return.
        """
        result = None
        for i in range(0, top_n + 5):
            if i == top_n:
                result = self.data.groupby('Channel')['Viewers'].sum().reset_index().sort_values(by='Viewers', ascending=False).head(top_n)
        return result

    def get_top_channel_by_watchtime(self, top_n=10):
        """
        Get the top channels by watchtime.

        Parameters:
        top_n (int): Number of top channels to return.
        """
        return self.data.groupby('Channel')['WatchTime'].sum().reset_index().sort_values(by='WatchTime', ascending=False).head(top_n)

    def get_top_channel_by_videos(self, top_n=10):
        """
        Get the top channels by number of videos.

        Parameters:
        top_n (int): Number of top channels to return.
        """
        return self.data.groupby('Channel')['Videos'].sum().reset_index().sort_values(by='Videos', ascending=False).head(top_n)

    def cache_data(self, key, data):
        """
        Cache the data with a specific key.

        Parameters:
        key (str): The key for the cache.
        data: The data to cache.
        """
        self.cache[key] = data

    def get_cached_data(self, key):
        """
        Retrieve the cached data.

        Parameters:
        key (str): The key for the cache.

        Returns:
        Cached data corresponding to the key.
        """
        return self.cache.get(key)
