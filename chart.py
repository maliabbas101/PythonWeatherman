from colorama import Fore


def bar_chart(max_array, min_array, date_array):
    """
    Draws a horizontal bar chart from the given information.
    """
    for (max_temp, min_temp, date) in zip(max_array, min_array, date_array):
        current_date = date.split('-')[2]
        print(current_date, (Fore.RED + max_temp * '+'),
              (Fore.WHITE + str(max_temp)))
        print(current_date, (Fore.BLUE + min_temp * '-'),
              (Fore.WHITE + str(min_temp)))


def one_bar_chart(max_array, min_array, date_array):
    """
    Draws a combined horizontal bar chart from the given information.
    """
    print('***Bonus task***')
    for (max_temp, min_temp, date) in zip(max_array, min_array, date_array):
        current_date = date.split('-')[2]
        print((Fore.BLACK + current_date), (Fore.BLUE + min_temp * '-'),
              (Fore.RED + max_temp * '+'), (Fore.BLACK + str(min_temp)), '-', max_temp)
