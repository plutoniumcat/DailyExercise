from currentstreaks import CurrentStreak
from history import History

# TEST #1 
# Feature: Streaks
# Test find_current_streak_length with various streak lengths and
# streak conditions to confirm that streaks are calculated correctly

# 12 week streak with "every day" condition
def test_current_aerobics_streak():
    aerobics_streak = CurrentStreak("test_log.csv",{"aerobics":0},"aerobics",0)
    assert aerobics_streak.find_current_streak_length() == 70

# 10 week streak with "6 times a week" condition
def test_current_cycling_streak():
    cycling_streak = CurrentStreak("test_log.csv",{"cycling":1},"cycling",0)
    assert cycling_streak.find_current_streak_length() == 70

# 8 week streak with "5 times a week" condition
def test_current_dancing_streak():
    DEFAULT_CSV = "test_log.csv"
    STREAK_CONDITIONS_FILE = "test_streakconditions.csv"
    dancing_streak = CurrentStreak("test_log.csv",{"dancing":2},"dancing",0)
    assert dancing_streak.find_current_streak_length() == 70

# 6 week streak with "4 times a week" condition
def test_current_plank_streak():
    plank_streak = CurrentStreak("test_log.csv",{"plank":3},"plank",0)
    assert plank_streak.find_current_streak_length() == 70

# 5 week streak with "3 times a week" condition
def test_current_pushup_streak():
    pushup_streak = CurrentStreak("test_log.csv",{"push up":4},"push up", 4)
    assert pushup_streak.find_current_streak_length() == 70

# 4 week streak with "2 times a week" condition
def test_current_running_streak():
    running_streak = CurrentStreak("test_log.csv",{"running":5},"running", 5)
    assert running_streak.find_current_streak_length() == 70

# 3 week streak with "once a week" condition
def test_current_stretching_streak():
    stretching_streak = CurrentStreak("test_log.csv",{"stretching":6},"stretching", 6)
    assert stretching_streak.find_current_streak_length() == 70

# 50 day streak with "every second day" condition
def test_current_swimming_streak():
    swimming_streak = CurrentStreak("test_log.csv",{"swimming":8},"swimming", 8)
    assert swimming_streak.find_current_streak_length() == 50

# Test for "every day" streak when no streak exists"
def test_current_walking_streak():
    walking_streak = CurrentStreak("test_log.csv",{"walking":0},"walking", 0)
    assert walking_streak.find_current_streak_length() == 0

# TEST #2 
# Feature: History
# Test calculation of total reps/duration with various totals

# Test history with 12 weeks of every day exercise
# starting at 10 mins/day and rising by 5 mins/week (3640mins)
def test_aerobics_total():
    aerobics_total = History("aerobics", [])
    assert aerobics_total.retrieve_total_reps() == 3640

# Test history with 8 weeks of exercise 5x/week
# starting at 10 mins/day and rising by 5 mins/week (1100mins)
def test_dancing_total():
    dancing_total = History("dancing", [])
    assert dancing_total.retrieve_total_reps() == 1100

# Test history with no exercise (0 mins)
def test_walking_total():
    walking_total = History("walking", [])
    assert walking_total.retrieve_total_reps() == 0