import pandas
import csv
from datetime import date, datetime, timedelta
import constants


def generate_history(daysweek, weeks):
    history = []
    for i in range(weeks):
        history += daysweek
    return history


def generate_alternate_history():
    history = []
    for i in range(35):
        history.append(1)
        history.append(0)
    return history


def generate_empty_history():
    history = []
    for i in range(70):
        history.append(0)
    return history


def create_test_log():
    print("Creating test log...")
    # Get column headers
    header_list = ["DATE"] + constants.EXERCISE_LIST
    dataframe = pandas.DataFrame(columns=header_list)
    # Get list of dates
    date_list = []
    for i in reversed(range(70)):
        workout_date = (datetime.today() - timedelta(days=i)).date()
        date_list.append(workout_date)
    dataframe["DATE"] = date_list
    # Generate history for each exercise
    # 12 weeks of 7 days per week
    aerobics_history = generate_history([1,1,1,1,1,1,1], 10)
    dataframe["aerobics"] = aerobics_history
    # 10 weeks of 6 days per week
    cycling_history = generate_history([1,1,1,1,1,1,0], 10)
    dataframe["cycling"] = cycling_history
    # 8 weeks of 5 days per week
    dancing_history = generate_history([1,1,1,1,1,0,0], 10)
    dataframe["dancing"] = dancing_history
    # 6 weeks of 4 days per week
    plank_history = generate_history([1,1,1,1,0,0,0], 10)
    dataframe["plank"] = plank_history
    # 5 weeks of 3 days per week
    pushup_history = generate_history([1,1,1,0,0,0,0], 10)
    dataframe["push up"] = pushup_history
    # 4 weeks of 2 days per week beginning at 10mins and increasing 5 mins/week to 30mins
    running_history = generate_history([1,1,0,0,0,0,0], 10)
    dataframe["running"] = running_history
    # 3 weeks of 1 days per week beginning at 10mins and increasing 2 mins/week to 16mins
    stretching_history = generate_history([1,0,0,0,0,0,0], 10)
    dataframe["stretching"] = stretching_history
    # 50 days of every second day beginning at 10 mins and increasing by 1min/workout to 60mins
    swimming_history = generate_alternate_history()
    dataframe["swimming"] = swimming_history
    # Empty history for all other exercises
    empty_history = generate_empty_history()
    for i in range(20):
        if i < 8:
            pass
        else:
            dataframe[constants.EXERCISE_LIST[i]] = empty_history
    dataframe.to_csv("test_log.csv", index=False)


def create_test_streakconditions():
    print("Creating streak conditions...")
    conditions = {}
    for i in range(7):
        conditions[constants.EXERCISE_LIST[i]] = i
    conditions["swimming"] = 8
    for i in range(9, 20):
        conditions[constants.EXERCISE_LIST[i]] = 0
    with open("test_streakconditions.csv", "w+") as outfile:
        writer = csv.writer(outfile)
        for row in conditions.items():
            writer.writerow(row)


def generate_test_files():
    create_test_log()
    create_test_streakconditions()
    print("Test files created")


generate_test_files()