import os.path
from main import *

def test_log_file_exists():
    assert os.path.exists("log.csv")

def test_todays_workout_input(monkeypatch):
    
    def mock_todays_input():
        return "push-up 20"
    monkeypatch.setattr(input, mock_todays_input)
    assert split_input[0] == "push-up"
    assert split_input[1] == "20"
