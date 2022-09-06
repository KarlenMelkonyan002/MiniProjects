import re


def email_check(my_mail):
    email = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(email, my_mail):
        return "Valid"
    return "Not valid"


def URL_check(my_url):
    url = "((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" + "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)"
    if re.match(url, my_url):
        return "Valid"
    return "Not Valid"


def date_check(my_date):
    day, month, year = my_date.split(".")
    day = int(day)
    month = int(month)
    year = int(year)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    elif year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
        max_days = 29
    else:
        max_days = 28
    if 12 < month or month < 1:
        return "Not Valid"
    elif max_days < day or day < 1:
        return "Not Valid"
    else:
        return "Valid"


def number_check(my_num):
    if my_num.isnumeric():
        return "Valid"
    else:
        return "Not Valid"


def card_check(my_card):
    """Here I use Luhn's algorithm for credit card validation"""
    if len(my_card) not in [15, 16] or not my_card.isnumeric():
        return "Not Valid"
    card_num = [int(digit) for digit in my_card]
    last_digit = card_num.pop()
    card_num.reverse()
    card_num = [digit * 2 if idx % 2 == 0 else digit for idx, digit in enumerate(card_num)]
    card_num = [digit - 9 if idx % 2 == 0 and digit > 9 else digit for idx, digit in enumerate(card_num)]
    card_num.append(last_digit)
    card_num_sum = sum(card_num)

    if card_num_sum % 10 == 0:
        return "Valid"
    return "Not Valid"


def phone_num_check(my_number):
    if len(my_number) != 8 or not my_number.isnumeric():
        return "Not Valid"
    return "Valid"


data_type = input("Enter please data type to validate(only Armenian phone numbers if chosen):")
data = input("Enter data: ")
if data_type == "Email":
    print(f"Your Email is {email_check(data)}")
elif data_type == "Website URL":
    print(f"Your URL is {URL_check(data)}")
elif data_type == "Date":
    print(f"Your Date is {date_check(data)}")
elif data_type == "Credit Card":
    print(f"Your Credit Card is {card_check(data)}")
elif data_type == "Mobile Phone Number":
    print(f"Your Phone Number is {phone_num_check(data)}")
