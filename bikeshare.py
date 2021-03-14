#change apply
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "CITY_DATA = { 'chicago': 'chicago.csv',\n",
    "              'new york city': 'new_york_city.csv',\n",
    "              'washington': 'washington.csv' }\n",
    "\n",
    "def get_filters():\n",
    "    \"\"\"\n",
    "    Asks user to specify a city, month, and day to analyze.\n",
    "\n",
    "    Returns:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    \"\"\"\n",
    "    print('Hello! Let\\'s explore some US bikeshare data!')\n",
    "    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs\n",
    "    city= input(\"Enter city name between three cities of new york city, washington and chicago: \").lower()\n",
    "    while city not in ['new york city', 'washington', 'chicago']:\n",
    "        city = input(\"you entered an invalid city! Please enter a city from the list: \").lower()\n",
    "    # TO DO: get user input for month (all, january, february, ... , june)\n",
    "    month=input(\"Please enter month name\").lower()\n",
    "    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)\n",
    "    day=input(\"Please enter name of day of the week\")\n",
    "    print('-'*40)\n",
    "    return city, month, day\n",
    "\n",
    "\n",
    "def load_data(city, month, day):\n",
    "    \"\"\"\n",
    "    Loads data for the specified city and filters by month and day if applicable.\n",
    "\n",
    "    Args:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    Returns:\n",
    "        df - Pandas DataFrame containing city data filtered by month and day\n",
    "    \"\"\"\n",
    "    df = pd.read_csv(\"{}.csv\".format(city.replace(\" \",\"_\")))\n",
    "\n",
    "    # Convert the Start and End Time columns to datetime\n",
    "    df['Start Time'] = pd.to_datetime(df['Start Time'])\n",
    "    df['End Time'] = pd.to_datetime(df['End Time'])\n",
    "\n",
    "    # extract month and day of week from Start Time to create new columns\n",
    "    df['month'] = df['Start Time'].dt.month\n",
    "    df['day_of_week'] = df['Start Time'].dt.weekday_name\n",
    "  \n",
    "    # filter by month if applicable\n",
    "    if month != 'all':\n",
    "        # use the index of the months list to get the corresponding int\n",
    "        months = ['january', 'february', 'march', 'april', 'may', 'june']\n",
    "        month = months.index(month) + 1\n",
    "\n",
    "        # filter by month to create the new dataframe\n",
    "        df = df[df['month'] == month]\n",
    "\n",
    "    # filter by day of week if applicable\n",
    "    if day != 'all':\n",
    "        # filter by day of week to create the new dataframe\n",
    "        df = df[df['day_of_week'] == day.title()]\n",
    "    return df\n",
    "\n",
    "\n",
    "def time_stats(df):\n",
    "    \"\"\"Displays statistics on the most frequent times of travel.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Frequent Times of Travel...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # TO DO: display the most comon month\n",
    "    print(\"The most common month is: {}\".format(str(df['month'].mode().value[0])))\n",
    "           \n",
    "        \n",
    "    # TO DO: display the most common day of week\n",
    "    print(\"The most common month is: {}\".format(str(df['month'].mode().value[0])))\n",
    "\n",
    "    # TO DO: display the most common start hour\n",
    "    df['start hour'] = df['Start Time'].dt.hour\n",
    "    print(\"The most common start hour is: {}\".format(str(df['start_hour'].mode().value[0])))\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "def station_stats(df):\n",
    "    \"\"\"Displays statistics on the most popular stations and trip.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Popular Stations and Trip...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # TO DO: display most commonly used start station\n",
    "    print(\"The most common used start station is: {} \".format(df['Start Station'].mode().value[0]))\n",
    "\n",
    "    # TO DO: display most commonly used end station\n",
    "    print(\"The most common used end station is: {} \".format(df['End Station'].mode().value[0]))\n",
    "\n",
    "\n",
    "    # TO DO: display most frequent combination of start station and end station trip\n",
    "    df['Combination'] = df['Start Station']+ \" \" + df['End Station']\n",
    "    print(\"The most frequent combination of start station and end station trip is: {} \".format(df['Combination'].mode().value[0]))\n",
    "\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def trip_duration_stats(df):\n",
    "    \"\"\"Displays statistics on the total and average trip duration.\"\"\"\n",
    "\n",
    "    print('\\nCalculating Trip Duration...\\n')\n",
    "    start_time = time.time()\n",
    "    df['Trip duration'] = df['End Time']-df['Start Time']\n",
    "    # TO DO: display total travel time\n",
    "    print(\"The total travel time is: {}\".format(str(df['duration'].sum())))\n",
    "\n",
    "    # TO DO: display mean travel time\n",
    "    print(\"The mean travel time is: {}\".format(str(df['duration'].mean())))\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def user_stats(df):\n",
    "    \"\"\"Displays statistics on bikeshare users.\"\"\"\n",
    "\n",
    "    print('\\nCalculating User Stats...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # TO DO: Display counts of user types\n",
    "    print(\"The user types are: {}\".format((df['User Type'].Value_counts())))\n",
    "\n",
    "    # TO DO: Display counts of gender\n",
    "    if city != 'washington':\n",
    "        print(\"The counts of gender are: {}\".format(df['Gender'].value_counts()))\n",
    "\n",
    "    # TO DO: Display earliest, most recent, and most common year of birth\n",
    "    print(\"The earliest year of birth: {}\".format(str(int(df['Birth Year'].min()))))\n",
    "    print(\"The most recent year of birth: {}\".format(str(int(df['Birth Year'].max()))))\n",
    "    print(\"The most comon year of birth: {}\".format(str(int(df['Birth Year'].mode().value[0]))))\n",
    "    \n",
    " \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def main():\n",
    "    while True:\n",
    "        city, month, day = get_filters()\n",
    "        df = load_data(city, month, day)\n",
    "\n",
    "        time_stats(df)\n",
    "        station_stats(df)\n",
    "        trip_duration_stats(df)\n",
    "        user_stats(df)\n",
    "\n",
    "        restart = input('\\nWould you like to restart? Enter yes or no.\\n')\n",
    "        if restart.lower() != 'yes':\n",
    "            break\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "\tmain()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
