def age():
    sec_or_year = input("Choose seconds(s) or years(y)? ")
    if sec_or_year == 's':
        # convert seconds to years
        user_value = input("Enter The no. of seconds youve lived ")
        print("You have lived for {} years".format(int(user_value)/60/60/24/365))
    elif sec_or_year == 'y':
        # convert years to sec
        user_value = input("Enter The no. of Years you've lived ")
        print("You have lived for {} seconds".format(int(user_value) * 60 * 60 * 24 * 365))

age()