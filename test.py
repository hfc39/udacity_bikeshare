import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    month_list = ['january', 'february','march','april','may', 'june','all']
    while month not in month_list:
        try:
            month = input('Please put in the right month: all, january, february, ... , june...etc.\n').lower()
        except month in month_list:
            return month
            break

    day = input('Pick a day from below: all, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday...etc.)\n').lower()
    day_list = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']

    while day not in day_list:
        try:
            day = input('Please put in the right day.\n')
        except day in day_list:
            return day


    print('-'*40)
    print('You\'ve chose the city of {}, with the month of {}, and day of {}'.format(city, month,day))
    return city, month, day

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
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    x = df['month'].mode()[0]
    month_name = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June'}
    print('The most common month: {}'.format(month_name[x]))
    # display the most common day of week
    print('The most common day of week: {}'.format(df['day'].mode()[0]))
    # display the most common start hour
    print('The most common start hour: {}'.format(df['hour'].mode()[0]))
    # display the least start hour
    least = df['hour'].value_counts().tail(1)
    print(type(least))
    print(least[0])
    #print('The least starting hour: {}'.format(df['hour'].value_counts().tail(1)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def print_data(df):
    row_start = 0
    row_end = 5
    while True:
        intention = input('Would you like to see 5 rows of the data you requested?\nPlease enter yes or no.\n').lower()
        if intention in ['yes','y','yup']:
            print(df.iloc[row_start:row_end])
            row_start +=5
            row_end +=5

        else:
            break

def main():
    city, month, day = get_filters()
    df = load_data(city, month, day)
    time_stats(df)
    print_data(df)



main()
