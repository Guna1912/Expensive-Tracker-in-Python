from datetime import datetime
from colorama import Style
print()
print(' '*30,f'{Style.BRIGHT}EXPENSIVE TRACKER{Style.RESET_ALL}')
print()
expensive_data = {}
while True:
    print()
    print(f'{Style.BRIGHT}Select option{Style.RESET_ALL}')
    print()
    print('1.Add Transaction\n2.View Transactions\n3.Search Transaction by Date\n4.Exit')
    print()
    while True:
        select = input('Enter an option: ')
        print()
        if select.isdigit():
            break
        else:
            print()
            print('Enter a digit between 1 - 4.')
            print()
    if select == '1':
        while True:
            category = input('Enter category you spent amount on: ')
            print()
            amount = input(f'Enter amount in Rs you spent on {category}: ')
            if amount.isdigit():
                print()
                confirm_amount = input(f'Do you confirm you spent {amount} Rs on {category} (yes/no): ').capitalize()
                print()
                if confirm_amount == 'Yes':
                    break
                elif confirm_amount == 'No':
                    continue     
                else:
                    print('Invalid Input.')
                    print()
            else:
                print('Enter Valid Amount.')
                print()
        while True:
            date = input('Enter date of expensive in YYYY-MM-DD (Leave empty for Today): ')
            print()
            if not date:
                date_expensive = datetime.today().strftime('%Y-%m-%d')
                break
            try:
                datetime.strptime(date, '%Y-%m-%d')
                date_expensive = date
                break
            except ValueError:
                print()
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                print()
        if date_expensive in expensive_data:
            expensive_data[date_expensive]+=[category,amount]
        else:
            expensive_data[date_expensive]=[category,amount]
        print()
        print(f'Transaction of {category} and {amount}Rs added Succesfully.')
        print()
    elif select == '2':
        if len(expensive_data) > 0:
            print()
            print(' '*23,f'{Style.BRIGHT}Transactions{Style.RESET_ALL}',' '*7)
            print('-'*55)
            print(' '*6,f'{Style.BRIGHT}Date{Style.RESET_ALL}',' '*13,f'{Style.BRIGHT}Category{Style.RESET_ALL}',' '*10,f'{Style.BRIGHT}Amount{Style.RESET_ALL}')
            print('-'*55)
            count_exp = 1
            for i in expensive_data:
                print(count_exp,' ',i,' '*(10-len(i)),end='')
                inc = 10
                cnt = 0
                for j in range(0,len(expensive_data[i]),2):
                    if cnt == 1:
                        inc+=15
                    print(' '*inc,expensive_data[i][j],' '*(18-len(expensive_data[i][j])),expensive_data[i][j+1],' '*7)
                    cnt+=1
                count_exp+=1
                print()
        else:
            print('No Transactions Found. Add Transactions to Show.')
            print()
    elif select == '3':
        while True:
            print()
            search_date = input('Enter date of expensive in YYYY-MM-DD (Leave empty for Today): ')
            print()
            if not search_date:
                search_date = datetime.today().strftime('%Y-%m-%d')
                break
            try:
                datetime.strptime(search_date, '%Y-%m-%d')
                search_date = search_date
                break
            except ValueError:
                print()
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                print()
        if search_date in expensive_data:
            print()
            print(' '*8,f'{Style.BRIGHT}Transactions in {search_date}{Style.RESET_ALL}')
            print('-'*40)
            print(' '*8,f'{Style.BRIGHT}Category{Style.RESET_ALL}',' '*11,f'{Style.BRIGHT}Amount{Style.RESET_ALL}')
            print('-'*40)
            print()
            total = 0
            for i in expensive_data:
                if i == search_date:
                    for x in range(0,len(expensive_data[i]),2):
                        print(' '*8,expensive_data[i][x],' '*(19-len(expensive_data[i][x])),expensive_data[i][x+1])
                        total+=int(expensive_data[i][x+1])
            print()
            print()
            print(' ',f'Total Expenses on {search_date} is {total}')
            print()
            print('-'*40)
            print()
        else:
            print(f'No Transaction Found on {search_date}')
        print()
    elif select == '4':
        break
    else:
        print('Please selct an option between 1 - 4.')