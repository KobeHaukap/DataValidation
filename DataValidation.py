"My Python Data Validator"

# imports
import re

# metadata for authorship information
__author__ = 'Kobe Haukap'
__version__ = '1.0'
__date__ ='2023.04.27'
__status__ = 'development'


def validate_id(id):

    regex_id = '^[0-9]+$'
    if re.compile(regex_id, id):
        return ""
    else:
        return "I"

    
def validate_name(name):

    parts = name.split()
    if len(parts) == 2:
        return ""
    else:
        return "N"


def validate_email(email):

    regex_email = r'^[\w-]+@\w+\.edu$'
    if re.compile(regex_email, email):
        return ""
    else:
        return "E"


def validate_phone(number):

    regex_phone = r'\d{3}-\d{3}-\d{4}'
    if re.match(regex_phone, number):
        return ""
    else:
        return "P"


def validate_date(date):

    regex_date = "%d-%m-%Y"
    if re.compile(regex_date, date):
        return ""
    else:
        return "D"


def validate_time(time):

    regex_time = "([01]?[0-9]|2[0-3]):[0-5][0-9]"
    if re.compile(regex_time, time):
        return ""
    else:
        return "T"


def process_file(input_data, valid_data, invalid_data):

    with open('input_data.txt', 'a', newline='\n') as input_data


def __main__():
    process_file()

