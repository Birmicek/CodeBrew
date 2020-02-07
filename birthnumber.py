import sys
import random

def convert_birth_format(birth):
    num = birth.split('/')
    if len(num) != 2:
        print('You provided invalid birth number!')
        print('Reason: there has to be 2 digits separated by / like this example: 980612/2356')
        return None

    birth_date = num[0]
    check_sum = num[1]

    #check num of birth date
    if len(birth_date) != 6:
        print('You provided invalid birth number!')
        print('Reason: your birth date has to have 6 digits')
        return None

    #check num behind / 3 OR 4
    if len(check_sum) != 3 and len(check_sum) != 4:
        print('You provided invalid check sum!')
        print('Reason: the check sum has to have 3 or 4 digits')
        return None

    if int(birth_date + check_sum) % 11 != 0:    #int(str(birth_date) + str(check_sum)) % 11 != 0:
        print('You provided invalid birth number!')
        print('Reason: your whole birth number has to be divisible by 11')
        return None

    #split birth_date on 3 nums
    birth_date_year = int(birth_date[:2])
    birth_date_month = int(birth_date[2:4])
    birth_date_day = int(birth_date[4:6])

    if birth_date_day not in range(1,32):
        print('You provided invalid birth number!')
        print('Reason: your day of birth must be in range 1 - 31')
        return None

    if birth_date_month in range(1,13):
        sex = 'M'
        if len(check_sum) == 3 and birth_date_year <= 53:
            print(f'Date of birth: 19{birth_date_year:02d}-{birth_date_month:02d}-{birth_date_day:02d}')
            print(f'Sex: {sex}')
            exit()
        if len(check_sum) == 3 and birth_date_year > 53:
            print('You provided invalid birth number!')
            print('Reason: people after year 1953 have to have 4 digits check sum')
            return None
        if len(check_sum) == 4 and birth_date_year <= 53:
            print(f'Date of birth: 20{birth_date_year:02d}-{birth_date_month:02d}-{birth_date_day:02d}')
            print(f'Sex: {sex}')
            exit()
        else:
             print(f'Date of birth: 19{birth_date_year:02d}-{birth_date_month:02d}-{birth_date_day:02d}')
             print(f'Sex: {sex}')
             exit()      


    # if female => month -50 and check if month is 1 - 12
    if birth_date_month > 50:      #check month > 50 = Female
        birth_date_month = birth_date_month - 50
    
    if birth_date_month not in range(1,13):
        print('You provided invalid birth number!')
        print('Reason: the MONTH in your birth date is invalid')
        return None

    sex = 'F'

    if len(check_sum) == 3 and birth_date_year <= 53:
        print(f'Date of birth: 19{birth_date_year:02d}-{birth_date_month:02d}-{birth_date_day:02d}')
        print(f'Sex: {sex}')
        exit()
    if len(check_sum) == 3 and birth_date_year > 53:
        print('You provided invalid birth number!')
        print('Reason: people after year 1953 have to have 4 digits check sum')
        return None
    if len(check_sum) == 4 and birth_date_year <= 53:
        print(f'Date of birth: 20{birth_date_year:02d}-{birth_date_month:02d}-{birth_date_day:02d}')
        print(f'Sex: {sex}')
        exit()
    else:
        print(f'Date of birth: 19{birth_date_year:02d}-{birth_date_month:02d}-{birth_date_day:02d}')
        print(f'Sex: {sex}')
        exit()  


def evaluate_birth_num():
    if len(sys.argv) > 2:
        print('You can provide only 1 argument for this function! Please rerun the program with proper argument!')
    elif len(sys.argv) == 2:
        provided_birth = sys.argv[1]
        #print(provided_birth)
        convert_birth_format(provided_birth)
    else:
        entered_birth = input('Day of the birth [YYYY-MM-DD]: ')
        sex = input('Sex [M/F]: ')

        entered_birth = entered_birth.split('-')
        if len(entered_birth[0]) != 4 and len(entered_birth[1]) != 2 and len(entered_birth[2]) != 2:
            print('You provided invalid birth number!')
            exit()
        
        entered_birth_year = entered_birth[0][2:4]
        entered_birth_month = entered_birth[1]
        entered_birth_day = entered_birth[2]
        entered_birth_whole = entered_birth_year + entered_birth_month + entered_birth_day
        #print(entered_birth_year, entered_birth_month, entered_birth_day)

        check_sum = [str(random.randint(0,9)) for x in range(4)]
        check_sum = ''.join(check_sum)

        birth_date = int(entered_birth_whole + check_sum)
        if birth_date % 11:
            final_birth_date = entered_birth_whole + '/' + check_sum
            print(f'Generated birth number: {final_birth_date}')


evaluate_birth_num()