from currentstreaks import CurrentStreak
from history import History

# TEST #1 
# Feature: Streaks
# Test find_current_streak_length with various streak lengths and
# streak conditions to confirm that streaks are calculated correctly


# 70 day streak with "every day" condition
def test_current_aerobics_streak():
    aerobics_streak = CurrentStreak("test_log.csv",{"aerobics":0},"aerobics",0)
    assert aerobics_streak.find_current_streak_length() == 70


# 70 day streak with "3 times a week" condition
def test_current_pushup_streak():
    pushup_streak = CurrentStreak("test_log.csv",{"push up":4},"push up", 4)
    assert pushup_streak.find_current_streak_length() == 70


# 70 day streak with "once a week" condition
def test_current_stretching_streak():
    stretching_streak = CurrentStreak("test_log.csv",{"stretching":6},"stretching", 6)
    assert stretching_streak.find_current_streak_length() == 70


# 70 day streak with "every second day" condition
def test_current_swimming_streak():
    swimming_streak = CurrentStreak("test_log.csv",{"swimming":8},"swimming", 8)
    assert swimming_streak.find_current_streak_length() == 70


# Test for "every day" streak when no streak exists"
def test_current_walking_streak():
    walking_streak = CurrentStreak("test_log.csv",{"walking":0},"walking", 0)
    assert walking_streak.find_current_streak_length() == 0


# TEST #2 
# Feature: History
# Test calculation of total reps/duration with various totals


# Test with 1 min per day every day for 70 days
def test_aerobics_total():
    aerobics_total = History("test_log.csv", "aerobics", [])
    aerobics_total.set_history()
    assert aerobics_total.retrieve_total_reps() == 70


# Test with 1 min per day 5 times a week for 10 weeks
def test_dancing_total():
    dancing_total = History("test_log.csv", "dancing", [])
    dancing_total.set_history()
    assert dancing_total.retrieve_total_reps() == 50


# Test history with no exercise (0 mins)
def test_walking_total():
    walking_total = History("test_log.csv", "walking", [])
    walking_total.set_history()
    assert walking_total.retrieve_total_reps() == 0