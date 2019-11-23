def get_month():
        while True:
            month = input('Which month? January, February, March, April, May,or June?\n').lower()
            month_list = ['january', 'february','march','april','may', 'june','jan','feb','mar','apr','jun']
            if month not in month_list:
                print('Please put in the right month.')
                continue
            else:
                return month


get_month()
