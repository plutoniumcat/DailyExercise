import os
from main import open_log_file

def test_open_log_file():
    open_log_file()
    assert os.path.exists("log.csv")