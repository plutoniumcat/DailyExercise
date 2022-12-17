from constants import DEFAULT_CSV, LONGEST_STREAK_FILE, STREAK_CONDITIONS_FILE
from generate_test_files import generate_test_files
from currentstreaks import CurrentStreak
from history import History

# Change log files to test files for the duration of the tests

def change_to_test_files():
    DEFAULT_CSV = "test_log.csv"
    LONGEST_STREAK_FILE = "test_longeststreak.csv"
    STREAK_CONDITIONS_FILE = "test_streakconditions.csv"

# TEST #1 
# Feature: Streaks
# Test find_current_streak_length with various streak lengths and
# streak conditions to confirm that streaks are calculated correctly

# 12 week streak with "every day" condition
def test_current_aerobics_streak():
    aerobics_streak = CurrentStreak("aerobics", 0)
    assert aerobics_streak.find_current_streak_length() == 84

# 10 week streak with "6 times a week" condition
def test_current_cycling_streak():
    cycling_streak = CurrentStreak("cycling", 1)
    assert cycling_streak.find_current_streak_length() == 70

# 8 week streak with "5 times a week" condition
def test_current_dancing_streak():
    dancing_streak = CurrentStreak("dancing", 2)
    assert dancing_streak.find_current_streak_length() == 56

# 6 week streak with "4 times a week" condition
def test_current_plank_streak():
    plank_streak = CurrentStreak("plank", 3)
    assert plank_streak.find_current_streak_length() == 42

# 5 week streak with "3 times a week" condition
def test_current_pushup_streak():
    pushup_streak = CurrentStreak("push up", 4)
    assert pushup_streak.find_current_streak_length() == 35

# 4 week streak with "2 times a week" condition
def test_current_running_streak():
    running_streak = CurrentStreak("running", 5)
    assert running_streak.find_current_streak_length() == 28

# 3 week streak with "once a week" condition
def test_current_stretching_streak():
    stretching_streak = CurrentStreak("stretching", 6)
    assert stretching_streak.find_current_streak_length() == 21

# 50 day streak with "every second day" condition
def test_current_swimming_streak():
    swimming_streak = CurrentStreak("swimming", 8)
    assert swimming_streak.find_current_streak_length() == 50

# Test for "every day" streak when no streak exists"
def test_current_walking_streak():
    walking_streak = CurrentStreak("walking", 0)
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

# generate_test_files()
change_to_test_files()
test_current_aerobics_streak()
test_current_cycling_streak()
test_current_dancing_streak()
test_current_plank_streak()
test_current_pushup_streak()
test_current_running_streak()
test_current_stretching_streak()
test_current_swimming_streak()
test_current_walking_streak()
test_aerobics_total()
test_dancing_total()
test_walking_total()