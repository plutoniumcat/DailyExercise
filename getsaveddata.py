import csv
from datetime import datetime
import pandas
from constants import DEFAULT_CSV

def get_log_dates():
    log = pandas.read_csv(DEFAULT_CSV)
    log_dates = log["DATE"].tolist()
    return log_dates

def get_last_log_date():
    log_dates = get_log_dates()
    if len(log_dates) == 0:
        return 0
    last_log_date = log_dates[-1]
    return last_log_date

def determine_log_age(log_date):
    date = datetime.strptime(log_date, "%Y-%m-%d")
    today = datetime.today()
    return abs((date - today).days)

def get_longest_streak_dict():
    dataframe = pandas.read_csv("longest_streak.csv", header=None, index_col=0).squeeze("columns")
    streak_dict = dataframe.to_dict()
    return streak_dict