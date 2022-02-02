#!/usr/bin/env python
# coding: utf-8

# In[8]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': './Downloads/chicago.csv',
              'new york city': './Downloads/new_york_city.csv',
              'washington': './Downloads/washington.csv' }


def user_input(x, y):
    while x.lower() not in y:
        x = input('"Invalid input" please re-enter the answer again.\n')
        if x.lower() in y:
            break

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
    cities = ['chicago', 'new york city', 'washington']
    user_input(city, cities)
            
    # get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to filter - January, February, March, April, May, June, or "all" to apply no month filter?\n')
    month_s = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    user_input(month, month_s)
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = (input('Which day would you like to filter - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or "all" to apply no day filter?\n')).title()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    user_input(day, days)
    
    print('-'*40)
    return city.lower(), month.lower(), day.title()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day] 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Common Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)
    
    # find the most common day name
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', popular_day)

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour 
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %.3f seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' - to - ' + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('Most Common Trip:', popular_trip)

    print("\nThis took %.3f seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()/(60*60*24)
    print("Total Travel Time %.3f Days" % total_travel_time)
    
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print("Average Travel Time %.3f Minutes" % mean_travel_time)
    
    print("\nThis took %.3f seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_type_counts)

    # Display counts of gender    
    gender_counts = df['Gender'].value_counts()
    print('\nCounts of Gender:\n', gender_counts)

    # Display earliest, most recent, and most common year of birth
    birth_year_min = df['Birth Year'].min()
    print('\nEarliest year of birth:', int(birth_year_min))
    birth_year_max = df['Birth Year'].max()
    print('Most recent year of birth:', int(birth_year_max))
    popular_birth_year = df['Birth Year'].mode()[0]
    print('Most common year of birth:', int(popular_birth_year))

    print("\nThis took %.3f seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_w(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_type_counts)
    
    # Display counts of gender
    print('\nThere are no stats for user gender in Washington.')
    
    # Display earliest, most recent, and most common year of birth
    print('\nThere are no stats for user year of birth in Washington.')
    
    print("\nThis took %.3f seconds." % (time.time() - start_time))
    print('-'*40)

    
def see_raw_data(df):
    see_raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    i = 0
    yes_or_no = ['yes', 'no']
    user_input(see_raw_data, yes_or_no)
    while see_raw_data.lower() == 'yes':
        print(df[i : i+5])
        see_raw_data = input('\nWould you like to see more 5 lines of raw data? Enter yes or no.\n')
        i += 5
        if i >= len(df):
            print('\nThere is no more raw data to display.\n')
            break
            
        user_input(see_raw_data, yes_or_no)
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        
        if city == 'washington':
            user_stats_w(df)
        else:
            user_stats(df)

        see_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        yes_or_no = ['yes', 'no']
        user_input(restart, yes_or_no)
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

