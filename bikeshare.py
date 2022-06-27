def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Where, would you like to explore?\n Cities ranging betweeen Chicago, New York City and Washington!\n').lower()
        if city in City_Range:
            break
        else:
            print('Opps!!! This city is not covered by Bikeshare\n')
            continue
        
        
    #Get user to pick whether to filter by a specific month or not
    Month_Array = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug' 'sep', 'oct', 'nov', 'dec']

    while True:
        month = input("Which month, do you want to analize.\n Hint:- \n Enter 'all' or enter the first 3 letters of the month you are analizing, i.e jan for Junuary.\n").lower()
        if month == 'all':
            print('\n Ready! Get the data for all months.\n')
            break
        elif month in Month_Array:
            print(('\n Ready! Get the data for {} month.\n').format(month.title()))
            break
        else:
            print('Opps!!! This is not the first 3 letters of any month.\n')
            continue

    #Get user to pick whether to filter by a specific day or not
    while True:
        day = input("Which day of the week would you like to explore?\n Hint:\n Enter day name in full or enter 'all' if you want explore all days.\n").lower()
        if day == 'all':
            print('\nLets get the data for everyday.')
            break
        elif day in Day_Array:
            print('\nLets get the data for {}.'.format(day.title()))
            break
        else:
            print('Opps!!! The day you entered is invalid')
            continue
            
   
    return city, month, day
   