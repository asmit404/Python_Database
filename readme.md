# Overview
This is a very simple command-line database management system made in python using prettytable, json and in-built libraries.

## Functions
The application includes four main functions:
    1. Add Data
    2. Display Data
    3. Search Data
    4. Export Data

## In Depth Explanation of Functions
The first function is to add data to the database. The application takes has three functiions to take names, email addresses and phone numbers as input and store them in lists. This function has some data validation so that user can't enter invaid values. For names, the functions checks if the length of the entered string is zero. For email addresses, the function checks if the entered string has an `@` present in it. For phone numbers, the function checks if the length of the entered *string* is less than 10 digits. The functions loop until a valid value is inputted. One limitation of this application is that it stores this data in a variable, so it is cleared when the instance is closed.

The second function is to display the data present in the database. This function uses the prettytable library to display the data from the lists in a table. I was having trouble with tabulate to display all elements from the list in a table and I found it easier and more efficient to use prettytable.

The third function is to search through data in the database. It can search data in the database using name, email or phone. Entering a name would find the respective email address and phone number of the entry. Entering a phone number would find the respective email address and name of the entry. Entering an email address would find the respective name and phone number of the entry.

The fourth function is to export the data in the database using json_save in the json library. The function maps the data into two dictionaries and exports it into a JSON file. The first dict contains the name and phone number of the entries and the second dict contains name and email addresses of the entries.
