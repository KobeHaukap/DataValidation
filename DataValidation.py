"My Python Data Validator"

# imports
import re
import csv

# metadata for authorship information
__author__ = 'Kobe Haukap'
__version__ = '1.0'
__date__ ='2023.04.27'
__status__ = 'development'


def validate_id(id):
    """
    Validates the integer ID in the input_data file
    :param id: id in input file
    :return: None
    """

    regex_id = '^[0-9]+$'  # sets the pattern for id
    if re.match(regex_id, id):  # matches the input id with pattern
        return ""  # returns empty if match
    else:
        return "I"  # returns error code if not matching

    
def validate_name(name):
    """
    Validates the NAME in the input_data file
    :param name: name in input file
    :return: None
    """

    parts = name.split(',')  # splits name into 2 parts with the comma
    if len(parts) == 2:
        return ""  # returns empty if match
    else:
        return "N"  # returns error code if not matching


def validate_email(email):
    """
    Validates the format of the EMAIL in the input_data file
    :param email: email in input file
    :return: None
    """

    regex_email = r'^[\w-]+@\w+\.edu$'  # sets pattern for input email
    if re.match(regex_email, email):
        return ""  # returns empty if match
    else:
        return "E"  # returns error code if not matching


def validate_phone(number):
    """
    Validates the format of the PHONE NUMBER in the input_data file
    :param number: number in input file
    :return: None
    """

    regex_phone = r'\d{3}-\d{3}-\d{4}'  # sets pattern for input phone number
    if re.match(regex_phone, number):
        return ""  # returns empty if match
    else:
        return "P"  # returns error code if not matching


def validate_date(date):
    """
    Validates the format of the DATE in the input_data file
    :param date: date in input file
    :return: None
    """

    date_format = r'^\d{2}-\d{2}-\d{4}$'  # sets pattern for input date
    if re.match(date_format, date):
        return ""  # returns empty if match
    else:
        return "D"  # returns error code if not matching


def validate_time(time):
    """
    Validates the format of the TIME in the input_data file
    :param time: time in input file
    :return: None
    """

    regex_time = "([01]?[0-9]|2[0-3]):[0-5][0-9]"  # sets pattern for input time
    if re.match(regex_time, time):
        return ""  # returns empty if match
    else:
        return "T"  # returns error code if not matching


def process_file():
    """
    Opens the input data file and validates each line
    for formatting. If the string has no errors it adds it to
    the valid data file, and if the string has errors it appends
    the errors to the invalid data file.
    :return: None
    """

    # opens the input data file as 'read'
    with open('input_data.txt', mode='r', newline='\n') as input_data:
        input_reader = csv.reader(input_data, delimiter='|')
        for lines in input_reader:
            error_string = ""  # string containing error codes for invalid data file
            data_count = len(lines)

            # validates each section of input data file and adds error code to error string
            if data_count == 6:
                error_string += validate_id(lines[0])
                error_string += validate_name(lines[1])
                error_string += validate_email(lines[2])
                error_string += validate_phone(lines[3])
                error_string += validate_date(lines[4])
                error_string += validate_time(lines[5])

            #  if input line doesn't contain errors sets 'error code' to C
            else:
                error_string = 'C'

            #  if the error code is C it writes valid line to valid data file
            if error_string == 'C':
                with open('valid_data.txt', mode='a', newline='\n') as valid_data:
                    valid_writer = csv.writer(valid_data, delimiter=',')
                    valid_writer.writerow(lines)

            # if error codes are present it adds them to the invalid data file
            else:
                with open('invalid_data.txt', mode='a', newline='\n') as invalid_data:
                    invalid_writer = csv.writer(invalid_data, delimiter='|')
                    invalid_writer.writerow(error_string)


if __name__ == '__main__':
    process_file()

