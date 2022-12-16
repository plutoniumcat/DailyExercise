import pandas
import csv
from datetime import date, datetime, timedelta
import constants

def generate_history(daysweek, weeks, increase):
    history = []
    reps = 10
    for i in range(100 - (weeks * 7)):
        history.append(0)
    for i in range(weeks):
        reps += increase
        for i in range(daysweek):
            history.append(reps)
        for i in range(7 - daysweek):
            history.append(0)
    return history

def generate_alternate_history(length, increase):
    history = []
    mins = 10
    for i in range(100 - length):
        history.append(0)
    for i in range(length//2):
        mins += increase
        history.append(mins)
        history.append(0)
    return history

def generate_empty_history():
    history = []
    for i in range(100):
        history.append(0)
    return history

def create_test_log():
    print("Creating test log...")
    # Get column headers
    header_list = ["DATE"] + constants.EXERCISE_LIST
    dataframe = pandas.DataFrame(columns=header_list)
    # Get list of dates
    date_list = []
    for i in reversed(range(100)):
        workout_date = (datetime.today() - timedelta(days=i)).date()
        date_list.append(workout_date)
    dataframe["DATE"] = date_list
    # Generate history for each exercise
    # 12 weeks of 7 days per week beginning at 10mins and increasing 5 mins/week to 70mins
    aerobics_history = generate_history(7, 12, 5)
    dataframe["aerobics"] = aerobics_history
    # 10 weeks of 6 days per week beginning at 10mins and increasing 5 mins/week to 60mins
    cycling_history = generate_history(6, 10, 5)
    dataframe["cycling"] = cycling_history
    # 8 weeks of 5 days per week beginning at 10mins and increasing 5 mins/week to 50mins
    dancing_history = generate_history(5, 8, 5)
    dataframe["dancing"] = dancing_history
    # 6 weeks of 4 days per week beginning at 10mins and increasing 1 mins/week to 16mins
    plank_history = generate_history(4, 6, 1)
    dataframe["plank"] = plank_history
    # 5 weeks of 3 days per week beginning at 10reps and increasing 5 reps/week to 35reps
    pushup_history = generate_history(3, 5, 5)
    dataframe["push up"] = pushup_history
    # 4 weeks of 2 days per week beginning at 10mins and increasing 5 mins/week to 30mins
    running_history = generate_history(2, 4, 5)
    dataframe["running"] = running_history
    # 3 weeks of 1 days per week beginning at 10mins and increasing 2 mins/week to 16mins
    stretching_history = generate_history(1, 3, 2)
    dataframe["stretching"] = stretching_history
    # 50 days of every second day beginning at 10 mins and increasing by 1min/workout to 60mins
    swimming_history = generate_alternate_history(10, 1)
    dataframe["swimming"] = swimming_history
    # Empty history for all other exercises
    empty_history = generate_empty_history()
    for i in range(20):
        if i < 8:
            pass
        else:
            dataframe[constants.EXERCISE_LIST[i]] = empty_history
    dataframe.to_csv("test_log.csv", index=False)

def create_test_longeststreak():
    print("Creating streak record...")
    streakdict = {}
    x = 0
    for exercise in constants.EXERCISE_LIST:
        x += 10
        streakdict[exercise] = x
    with open("test_longeststreak.csv", "w+") as outfile:
        writer = csv.writer(outfile)
        for row in streakdict.items():
            writer.writerow(row)

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

def create_test_files():
    create_test_log()
    create_test_longeststreak()
    create_test_streakconditions()
    print("Test files created")

create_test_files()