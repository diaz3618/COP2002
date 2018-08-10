#!/usr/bin/env python3
from datetime import datetime, timedelta

def main():
    print("Arrival Time Estimator")
    io()

def io():
    again = True
    while again == True:
        departure_date = str(input("Estimated date of departure (YYYY-MM-DD): "))
        departure_time = str(input("Estimated time of departure (HH:MM AM/PM): "))
        miles = int(input("Enter miles: "))
        mph = int(input("Enter miles per hour: "))

        estimator(departure_date, departure_time.upper(), miles, mph)
    
        ask = input("Continue? (y/n): ")
        if ask.lower() == "n":
            print("\nBye!")
            again = False
        if ask.lower() == "y":
            print("\n")
    
def estimator(dep_date, dep_time, miles, mph):
    hrs = miles // mph
    mins = miles % mph
    flight_time = timedelta(hours = hrs, minutes = mins)
    _depDate = dep_date + " " + dep_time
    datetime_dep = datetime.strptime(_depDate, "%Y-%m-%d %I:%M %p")
    arrival_datetime = datetime_dep + flight_time

    print("\nEstimated travel time")
    print("Hours: " + str(hrs) + "\nMinutes: " + str(mins))
    print("Estimated date of arrival: " + str(dep_date) + "\nEstimated time of arrival: " + str(arrival_datetime.strftime("%I:%M %p")) + "\n")

if __name__ == "__main__":
    main()
