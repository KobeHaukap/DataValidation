# DataValidation
This program uses 'regex' to validate the formatting of data in a file. Any errors in the formatting are shown as an error code
and written in it's own invalid data file. If all of the data is correct the complete line is written in a valid data file.

## Usage
To use this program, simply input the data you wish to validate into input data file,
and the program will analyze it and provide feedback on whether it is valid or not.

## Features
This program uses 'with open' to open three .csv files. It reads the 
input file's data in segments delimited by a '|' and validates each segment separatly.
If the data is formatted correctly the program opens the valid data file, and writes the line in.
Each segment formatted incorrectly is added to a list, the invalid data file is opened,
and the error code(s) are written in the file.

## Output
If there are any error codes they will be written in the invalid data file.
If the line is free of formatting errors, all of the correct data is written
in the valid data file.


## Author
Kobe Haukap

