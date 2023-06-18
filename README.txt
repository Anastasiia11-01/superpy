Requirements for main.py:
- csv
- datetime (import date, datetime, timedelta)
- os
- itertools
- collections (import Counter)
- pandas as pd
- matplotlib.pyplot as plt
- numpy as np

Requirements for super.py:
- argparse
- main
- sys


General use:
The program SuperPy has been developed in order to keep track of a supermarket's inventory.

Functions:

    - 1.'create_folder' function:

        usage: python super.py create_folder {arguments}
        required arguments: folder
        example: python super.py create_folder --folder products_csv

        Note: if you do not specify the folder_name yourself, it will be set to default name: products_csv

Important: after creating this folder, please manually create a csv file called 'date.csv' specifying the date in there in format yyyy-mm-dd. This date will be taken for default date when working with 'advance_time' function (it's description you will find later in this file). If you don't do it, the default date will be set to the date, when running the function called 'read_date_csv'.

    - 2.'create_csv_file' function:

        usage: python super.py create_csv_file {arguments}
        required arguments: file
        example: python super.py create_csv_file --file bought.csv

        Note: you can choose from 2 arguments options:
            1) 'bought.csv'
            2) 'sold.csv'

            Default set to option №1.
        IMPORTANT to create csv files before proceeding to the next function!

    - 3.'add_csv_values' function 
    (better to use internal version 'add_csv_values_internal'):

        usage: python super.py add_csv_values {arguments}
        required arguments: name (name of a product), buy_price/sell_price, value (which is date in yyyy-mm-dd for bought product and id for sold product)
        example1: python super.py add_csv_values --name orange --buy_price 5.0 --value 2023-06-04
        example2: python super.py add_csv_values --name orange --sell_price 6.0 --value 1

    - 'read_date_csv' function:

        usage: python super.py read_date_csv
        required arguments: no arguments required
        example1: python super.py read_date_csv -d
        example2: python super.py read_date_csv --date

        Note: this function returns the date saved in 'date.csv' file. If no such file exists, the function will create the file with the date of the day when you run it.

    - 5.'buy' function:

        usage: python super.py buy {arguments}
        required arguments: product_name, price, expiration_date (in format yyyy-mm-dd)
        example: python super.py buy --buy orange 2.0 2023-12-01

    - 6.'sell' function:

        usage: python super.py sell {arguments}
        required arguments: product_name, sell_price
        example: python super.py sell --sell orange 3.0

    - 7.'set_date' function:

        usage: python super.py set_date {arguments}
        required arguments: date(in format yyyy-mm-dd)
        example: python super.py set_date --date 2023-04-02

        Note: this function will update the date in the 'date.csv' file to the date you specify as an argument.

    - 8.'advance_time' function:

        usage: python super.py advance_time {arguments}
        required arguments: date(in format yyyy-mm-dd) or any number
        example1: python super.py advance_time -d 2023-04-02
        example2: python super.py advance_time -n 3

        Note: if your argument will be date, the function will return the list of products which will expire on that given date; if your argument will be a number, the function will return the list of products which will expire on the date calculated as date saved in csv file + the number (example: today(2023-06-07) + number(3) = list for date(2023-06-10)).
        Important: if your argument is a date, then this date will be automatically saved in the 'date.csv' file. If you need to change it again, you may use 'set_date' function or do it manually.

    - 9.'report_inventory' function:

        usage: python super.py report_inventory {arguments}
        required arguments: date (in format yyyy-mm-dd or yyyy-mm or yyyy; also you can write 'now' or 'yesterday') 
        example1: python super.py report_inventory --inventory 2023-04-02
        example2: python super.py report_inventory --inventory 2023-04
        example3: python super.py report_inventory -- inventory now

        Note: it will return the list of the products available on the given date.

    - 10.'report_revenue' function:

        usage: python super.py report_revenue {arguments}
        required arguments: date (in format yyyy-mm-dd or yyyy-mm or yyyy; also you can   write 'today' or 'yesterday') 
        example1: python super.py report_revenue --revenue 2023-04-02
        example2: python super.py report_revenue --revenue 2023
        example3: python super.py report_revenue --revenue yesterday

    - 11.'report_profit' function:

        usage: python super.py report_profit {arguments}
        required arguments: date (in format yyyy-mm-dd or yyyy-mm or yyyy; also you can write 'today' or 'yesterday') 
        example1: python super.py report_profit --profit 2023-04-02
        example2: python super.py report_profit --profit 2023
        example3: python super.py report_profit --profit today

     - 12.'csv_to_excel' function:

        usage: python super.py csv_to_excel {arguments}
        required arguments: csv_filename, excel_filename
        example: python super.py csv_to_excel --file bought.csv ResultExcelFile.xlsx

    - 13.'spent_vs_revenue' function:

        usage: python super.py spent_vs_revenue {arguments}
        required arguments: date (in format yyyy-mm-dd or yyyy-mm or yyyy; also you can write 'today' or 'yesterday') 
        example1: python super.py spent_vs_revenue --spent_revenue 2023-04-02
        example2: python super.py spent_vs_revenue --spent_revenue 2023
        example3: python super.py spent_vs_revenue --spent_revenue today

   

    


        

