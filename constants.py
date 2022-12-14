from getsaveddata import *

MAIN_MENU_ITEMS = 4
STREAK_MENU_ITEMS = 3

DEFAULT_CSV = "test_log.csv"
EXERCISE_FILE = "exerciselist.csv"
EXERCISE_DICT = get_exercise_dict()
EXERCISE_LIST = list(EXERCISE_DICT.keys())
STREAK_CONDITIONS = get_streak_conditions()