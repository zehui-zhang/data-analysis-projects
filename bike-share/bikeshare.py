import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days =  ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    
    #get user input for city (chicago, new york city, washington). 
    #Use a while loop to handle invalid inputs.
    while True:
        city = input("Which city(s) would you like to analyze: {},{} or {}? ".format(*CITY_DATA.keys())).strip().lower()
        if city in CITY_DATA.keys():
            print("The city you will analyze is: {}\n".format(city.title()))
            break
        else:
            print("Sorry, that was not one of our cities. Please try again.")

    #get user input for month (all, january, february, ... , june)
    #use a while loop to handle invalid inputs.
    while True:
        month = input("Which month(s) would you like to analyze? All, {}, {}, {}, {}, {}, {}?: ".format(*months)).strip().lower()
        if month == "all":
            print("You are going to analyze all months.")
            break
        if month != "all":
            if month in months:
                print("The month you will analyze is: {}\n".format(month.title()))
                break
            else:
                print("Please input the correct content.\n")
        else:
            print("Please input the correct content.\n")

    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day(s) would you like to analyze? all, {}, {}, {}, {}, {}, {}, {}?: ".format(*days)).strip().lower()
        if day == "all":
            print("You are going to analyze all days.")
            break
        if day != "all":
            if day in days:
                print("The day you will analyze is : {}\n".format(day.title()))
                break
            else:
                print("Please input the correct content.")
        else:
            print("Please input the correct content.")

    print('-'*40)
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
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'],yearfirst=True)
    
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.day_name

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['week_day'] == day.title()]
    print(df['month'])
    print(df['week_day'])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    popular_month = df['month'].mode()
    print(popular_month)
    # print('The most common month is {}.\n'.format(months[popular_month]).title())

    # TO DO: display the most common day of week
    popular_day = df['week_day'].mode()[0]
    print('The most popular day is {}.\n'.format(popular_day).title())

    # TO DO: display the most common start hour
    
    popular_hour = df['hours'].dt.hour.mode()[0]
    print('\nThe most popular hour is {}.\n'.format(popular_hour))

    print("\nThis took %.2f seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is {}.\n'.format(popular_start))

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is {}.\n'.format(popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trips'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trips'].mode()[0]
    print('\nThe most frequent combination of start station and end station is {}.\n'.format(popular_trip))

    print("\nThis took %.2f seconds." % (time.time() - start_time))
    print('-'*40)
    
   
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # TO DO: display total travel time
    df['Travel Time'] = (df['End Time'] - df['Start Time']).dt.seconds / 60.0
    total_trip = df['Travel Time'].sum()
    print('\nThe total travel time is {} minutes.\n'.format(total_trip))

    # TO DO: display mean travel time
    avg_trip = df['Travel Time'].mean()
    print('\nThe mean travel time is {} minutes.\n'.format(avg_trip))
    
    print("\nThis took %.2f seconds." % (time.time() - start_time))
    print('-'*40)
    


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    genders = df['Gender'].value_counts()
    print(genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = int(df['Birth Year'].min())
    most_recent = int(df['Birth Year'].max())
    most_common = int(df['Birth Year'].mode()[0])
    print('\nThe earliest year of birth is {}. The most recent year of birth is {}. The most common year of birth is {}.'.format(earliest,most_recent,most_common))

    print("\nThis took %.2f seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #Displays statistics on the most frequent times of travel.
        time_stats(df)

        #Displays statistics on the most popular stations and trip.
        station_stats(df)

        #Displays statistics on the total and average trip duration.
        trip_duration_stats(df)

        #Displays statistics on bikeshare users.
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes': #if input is not 'yes'
            break #terminate the loop


if __name__ == "__main__":
	main()
