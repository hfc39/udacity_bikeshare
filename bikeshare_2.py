import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    month = 'all'
    day = 'all'
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
    city_list = ['chicago','new york','washington']
    while city not in city_list:
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        try:
            city = input('Please choose from Chicago, New York and Washington.\n').lower()
        except city in city_list:
            return city
            break

    month = input('Please enter a month from below: January, February, March, April, May, June,or all.\n').lower()
    month_list = ['january', 'february','march','april','may', 'june','jan','feb','mar','apr','jun','all']
    while month not in month_list:
        try:
            month = input('Please put in the right month: all, january, february, ... , june...etc.\n').lower()
        except month in month_list:
            return month
            break

    day = int(input('Which day? Please type your response as an integer (e.g,. 0=all,1=Sunday,2=Monday...etc.)\n'))
    day_list = range(0,8)
    while day not in day_list:
        try:
            day = int(input('Please put in the right day.\n'))
        except day in day_list:
            return day


    print('-'*40)
    print('You\'ve chose the city of {}, with the month of {}, and day of {}'.format(city, month,day))

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
