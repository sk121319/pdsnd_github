#!/usr/bin/env python
# coding: utf-8
# welcome
# In[ ]:


import time
import pandas as pd
import numpy as np
import calendar
import datetime

#load local file: chicago,new_york_city, washinton
CITY_DATA = {'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv'}

#Index by month
month_index = {"january", "february", "march", "april", "may", "june"}

#Index by day
day_index = {"saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"}

#Ask for user's name
name = input("Please enter your name")

#Different meeting word depending different time period
current_time = datetime.datetime.now()
current_time.hour
if current_time.hour < 12:
    print('Goede morgen' + ' ' + name + ' :)' )
elif 12 <= current_time.hour < 18:
    print('Goede middag' + ' ' + name + ' :)')
else:
    print('Goede avond' + ' ' + name + ' :)')

#Explore the US bike data:
def get_filters():

#A greeting:
    print("Halo"+" "+name+"!"+" "+"Let\'s explore some US bikeshare data!")

#Ask user which city want to see:
    city = str(input("which city's data do you want to see : chicago, new york city, washington? ")).lower()
    while city not in CITY_DATA.keys():
        print( "There is a typo, please select city: chicago, new york city, washington.")
        city = str(input()).lower()
#Ask user which kind of date type want to see:
    month = input("which month do you want to see :january, february, march, april, may, june or enter [all] for no filter:\n").lower()
    while month not in month != "all":
        month = input("There is a typoe, please select :january, february, march, april, may, june or [all] for no filter:\n").lower()

#Ask use which day want to see:
    day = input("which day do you want to see : monday, tuesday, wednesday, thursday, friday, saturday, sunday or enter [all] for no filter:\n").lower()
    while day not in day != "all":
        day = input("There is a typo, please select: monday, tuesday, wednesday, thursday, friday, saturday, sunday or [all] for no filter:\n").lower()
    
    print('-'*40)
    return city, month, day

#Load the file:
def load_data(city, month, day):


    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
#Filter by month:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]
#Create df by month:

    if day != 'all':
#Filter by day:
        df = df[df['day_of_week'] == day.title()]
#Create dy by day:

    return df

#1 Popular times of travel:

def time_stats(df, month, day):

    start_time = time.time()

    if month == 'all':
        
#1.1 Most common month:
        print('most common month:', df['month'].mode()[0])

    if day == 'all':

#1.2 Most common day of week:
        print('most common day of week:', df['day_of_week'].mode()[0])

    df['hour'] = df['Start Time'].dt.hour
    
#1.3 Most common hour of day: 
    print('most common hour of day:', df['hour'].mode()[0])

#Display spent time:
    print("Spend %s seconds." % (time.time() - start_time))
    print('-'*40)


#2 Popular stations and trip:

def station_stats(df):

    print("Please wait a minute,system is calculating...")
    start_time = time.time()

#2.1 Most common start station:
    print('most common start station:', df['Start Station'].mode()[0])

#2.2 Most common end station:
    print('most common end station:', df['End Station'].mode()[0])

#2.3 Most common trip from start to end:
    most_trip = df.groupby(['Start Station', 'End Station'])['Trip Duration'].agg(
        'count').sort_values(ascending=False).head(1).to_string()
    print("most common trip from start to end: \n", most_trip)

#Display spent time:
    print("Spend %s seconds." % (time.time() - start_time))
    print('-'*40)


#3 Trip duration:

def trip_duration_stats(df):

#System is calculation:
    print("Please wait a minute,system is calculating...")
    start_time = time.time()

#3.1 Total travel time:
    print('Total Travel time: ', df['Trip Duration'].sum())

#3.2 Average travel time:
    print('Average Travel time:', df['Trip Duration'].mean())

#Display spent time:
    print("Spend %s seconds." % (time.time() - start_time))
    print('-'*40)


    
#4 User info:

def user_stats(df, city):

#System is calculation:
    print("Please wait a minute,system is calculating...")
    start_time = time.time()

#4.1 Counts of each user type
    print("Counts of each user type : ",
          df['User Type'].value_counts().to_string())
    
#4.2 Counts of each gender (data available for new_york_city and chicago)
    if city == 'new york city' or city == 'chicago':
        
        print("Counts of each gender ",
              df['Gender'].value_counts().to_string())

#4.2 Earliest,most recent,most common year of birth(data available for new_york_cit and chicago)
        print("Earliest birth year: ", df['Birth Year'].min())
        print("Most recent year: ", df['Birth Year'].max())
        print("Most common year: ", df['Birth Year'].mode()[0])

#Display spent time:
    print("Spend %s seconds" % (time.time() - start_time))
    print('-'*40)

#Show 5 rows of data and more
def show_raw_data(df):
    next_flag = input("would you like to see raw data? please type (yes or no)? ").lower()
    start_loc = 0
    while (next_flag != "no"):
        print(df[start_loc:start_loc+5])
        next_flag = input("5 more data? please type (yes or no)? ").lower()
        start_loc += 5

#Restart Program
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_raw_data(df)

        restart = input("would you like to restart? please type (yes or no)? ")
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()


# In[ ]:
# finish




