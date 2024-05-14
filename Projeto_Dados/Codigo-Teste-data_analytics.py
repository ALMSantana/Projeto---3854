import pytest
import json
import pandas as pd
from twitch_analytics.data_analytics import dataanalytics

@pytest.fixture
def sample_data():
    data = {
        'Channel': ['Streamer1', 'Streamer2', 'Streamer1', 'Streamer3'],
        'Average viewers': [100, 150, 200, 250],
        'Watch time(Minutes)': [1000, 1500, 2000, 2500],
        'Stream time(minutes)': [10, 15, 20, 25]
    }
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def analytics_object(sample_data):
    return dataanalytics(sample_data)

def test_getStreamerStats_success(analytics_object):
    result = analytics_object.getStreamerStats('Streamer1')
    expected_json = {
        "average_viewers": 150,  # Média de 100 e 200
        "total_watch_time": 3000,  # Soma de 1000 e 2000
        "stream_time": 30  # Soma de 10 e 20
    }
    assert json.loads(result) == expected_json

def test_getStreamerStats_nonexistent(analytics_object):
    result = analytics_object.getStreamerStats('NonExistentStreamer')
    expected_json = {
        "average_viewers": 0,
        "total_watch_time": 0,
        "stream_time": 0
    }
    assert json.loads(result) == expected_json

def test_getStreamerStats_empty(analytics_object):
    result = analytics_object.getStreamerStats('')
    expected_json = {
        "average_viewers": 0,
        "total_watch_time": 0,
        "stream_time": 0
    }
    assert json.loads(result) == expected_json
