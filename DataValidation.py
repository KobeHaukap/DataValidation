"My Python Data Validator"

# imports
import re
import csv
from datetime import datetime

# metadata for authorship information
__author__ = 'Kobe Haukap'
__version__ = '1.0'
__date__ ='2023.04.27'
__status__ = 'development'


def validate_id(id):

    regex_id = '^[0-9]+$'
    if re.match(regex_id, id):
        return ""
    else:
        return "I"

    
def validate_name(name):

    parts = name.split(',')
    if len(parts) == 2:
        return ""
    else:
        return "N"


def validate_email(email):

    regex_email = r'^[\w-]+@\w+\.edu$'
    if re.match(regex_email, email):
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

    date_format = r'^\d{2}-\d{2}-\d{4}$'
    if re.match(date_format, date):
        return ""
    else:
        return "D"


def validate_time(time):

    regex_time = "([01]?[0-9]|2[0-3]):[0-5][0-9]"
    if re.match(regex_time, time):
        return ""
    else:
        return "T"


def process_file():

    with open('input_data.txt', mode='r', newline='\n') as input_data:
        input_reader = csv.reader(input_data, delimiter='|')
        for lines in input_reader:
            error_string = ""
            data_count = len(lines)
            if data_count == 6:
                error_string += validate_id(lines[0])
                error_string += validate_name(lines[1])
                error_string += validate_email(lines[2])
                error_string += validate_phone(lines[3])
                error_string += validate_date(lines[4])
                error_string += validate_time(lines[5])

            else:
                error_string = 'C'

            if error_string == 'C':
                with open('valid_data.txt', mode='a', newline='\n') as valid_data:
                    valid_writer = csv.writer(valid_data, delimiter=',')
                    valid_writer.writerow(lines)
            else:
                with open('invalid_data.txt', mode='a', newline='\n') as invalid_data:
                    invalid_writer = csv.writer(invalid_data, delimiter='|')
                    invalid_writer.writerow(error_string)


if __name__ == '__main__':
    process_file()

