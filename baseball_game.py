# -*- coding: utf-8 -*-

import random

def get_random_number():
    return random.randrange(100, 1000)

def is_digit(user_input_number):
    res = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    for i in user_input_number:
        if i not in res:
            return False
    return True

def is_between_100_and_999(user_input_number):
    return 100 <= int(user_input_number) <= 999

def is_duplicated_number(three_digit):
    return not len(set(three_digit)) == 3

def is_validated_number(user_input_number):
    return is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not is_duplicated_number(user_input_number)


def get_not_duplicated_three_digit_number():
    while True:
        res = get_random_number()
        if len(set(str(res))) == 3:
            return res

def get_strikes_or_ball(user_input_number, random_number):
    ans = [0,0]
    res1 = dict().fromkeys([str(i) for i in range(10)], -1)
    res2 = dict().fromkeys([str(i) for i in range(10)], -1)
    for i in range(3):
        res1[user_input_number[i]] = i
        res2[random_number[i]] = i
    for i in res1:
        if res1[i] == res2[i]:
            if res1[i] != -1:
                ans[0] += 1
        else:
            if res1[i] != -1 and res2[i] != -1:
                ans[1] += 1
    return ans



def is_yes(one_more_input):
    return one_more_input.upper() in ['Y', 'YES']


def is_no(one_more_input):
    return one_more_input.upper() in ['N', 'NO']

def main():
    print("Play Baseball")
    user_input = 999
    terminate = False
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    while not terminate:
        user_input = input('Input guess number : ')
        if not is_validated_number(user_input):
            if list(set(user_input)) == ['0']:
                break
            print('Wrong Input, Input Again')
        else:
            res = get_strikes_or_ball(user_input, random_number)
            print('Strikes : %d , Balls : %d' % (res[0], res[1]))
            if res[0] == 3:
                while True:
                    retry = input('You Win, one more(Y/N)?')
                    if is_yes(retry):
                        random_number = str(get_not_duplicated_three_digit_number())
                        print("Random Number is : ", random_number)
                        break
                    elif is_no(retry):
                        terminate = True
                        break
                    else:
                        if list(set(retry)) == ['0']:
                            terminate = True
                            break
                        print('Wrong Input, Input Again')
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
