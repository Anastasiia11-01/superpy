import argparse
import main


global_parser = argparse.ArgumentParser(prog='super.py',
    description='Keeps track and produces reports on various kinds of data of the supermarket.',
    epilog='Thanks for using SuperPy!')

subparsers = global_parser.add_subparsers(
    title='subcommands', help='info about bought and sold products in the supermarket'
)

arg_template = {
    "dest": "value"
}

#1
create_folder_parser = subparsers.add_parser('create_folder')
create_folder_parser.add_argument('--folder',nargs=1, type=str, default = 'folder_csv',help='specify folder name', **arg_template)
create_folder_parser.set_defaults(func=main.create_folder)

#2
create_csv_file_parser = subparsers.add_parser('create_csv_file')
create_csv_file_parser.add_argument('--file',nargs=1,choices=['bought.csv', 'sold.csv'],default='bought.csv',help='enter file name as csv',**arg_template)
create_csv_file_parser.set_defaults(func=main.create_csv_file)

#3 -> not advisable for the use
add_csv_values_parser = subparsers.add_parser('add_csv_values')
add_csv_values_parser.add_argument('--name',nargs=1,type=str, help='specify product name, which was bought/sold',**arg_template)
add_csv_values_parser.add_argument('--buy_price',nargs=1,type=float, help='specify bought price',**arg_template)
add_csv_values_parser.add_argument('--sell_price',nargs=1,type=float, help='specify sold price',**arg_template)
add_csv_values_parser.add_argument('--value',nargs=1, help='specify expiration date as yyyy-mm-dd if for bought product or bought-id if for sold product',**arg_template)
add_csv_values_parser.set_defaults(func=main.add_csv_values)

#The previous 3 parsers are not meant to be used in general, but are here in case user needs the program for files creation also.

#4 
read_date_csv_parser = subparsers.add_parser('read_date_csv')
read_date_csv_parser.add_argument('-d','--date',help='returns the date which is saved in csv file', **arg_template)
read_date_csv_parser.set_defaults(func=main.read_date_csv)


#5
buy_parser = subparsers.add_parser('buy')
buy_parser.add_argument('--buy',nargs=3, help="enter product name. it's price and expiration date", **arg_template)
buy_parser.set_defaults(func=main.buy)

#6
sell_parser = subparsers.add_parser('sell')
sell_parser.add_argument('--sell',nargs=2, help="enter name of sold product and it's sell price",  **arg_template)
sell_parser.set_defaults(func=main.sell)

#7 
set_date_parser = subparsers.add_parser('set_date')
set_date_parser.add_argument('--date', required=True, nargs=1, type=str, help="enter name of sold product and it's sell price", **arg_template)
set_date_parser.set_defaults(func=main.set_date)  

#8
advance_time_parser = subparsers.add_parser('advance_time')
advance_time_parser.add_argument('-n','--number', nargs=1, type=int, help="enter number of days, when you want to check the expiration date from the date specified in csv file", **arg_template)
advance_time_parser.add_argument('-d','--date', nargs=1, type=str, help="enter date, when you want to check the expiration date", **arg_template)
advance_time_parser.set_defaults(func=main.advance_time)

#9
report_inventory_parser = subparsers.add_parser('report_inventory')
report_inventory_parser.add_argument('-in','--inventory',nargs=1, type=str, default = 'now', help="enter date in format yyyy-mm-dd or enter 'now' or 'yesterday'", **arg_template)
report_inventory_parser.set_defaults(func=main.report_inventory)


#10
report_revenue_parser = subparsers.add_parser('report_revenue')
report_revenue_parser.add_argument('-rev','--revenue',nargs=1,type=str, default = 'today',help="enter date in format yyyy-mm-dd/yyyy-mm/yyyy or enter 'today' or 'yesterday'", **arg_template)
report_revenue_parser.set_defaults(func=main.report_revenue)

#11
report_profit_parser = subparsers.add_parser('report_profit')
report_profit_parser.add_argument('--profit',nargs=1,type=str, default = 'today', help="enter date in format yyyy-mm-dd/yyyy-mm/yyyy or enter 'today' or 'yesterday'", **arg_template)
report_profit_parser.set_defaults(func=main.report_profit)

#12
csv_to_excel_parser = subparsers.add_parser('csv_to_excel')
csv_to_excel_parser.add_argument('--file',nargs=2,type=str, help="enter name of csv file and of excel file", **arg_template)
csv_to_excel_parser.set_defaults(func=main.csv_to_excel)

#13
spent_vs_revenue_parser = subparsers.add_parser('spent_revenue')
spent_vs_revenue_parser.add_argument('--sprev',nargs=1,default = 'today', help="enter date in format yyyy-mm-dd/yyyy-mm/yyyy or enter 'today' or 'yesterday'", **arg_template)
spent_vs_revenue_parser.set_defaults(func=main.spent_vs_revenue)



args = global_parser.parse_args()

print(args.func(*args.value))
