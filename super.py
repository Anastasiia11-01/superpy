import argparse
import main
import sys

global_parser = argparse.ArgumentParser(
    prog='super.py',
    description='Keeps track and produces reports on various kinds of data of the supermarket.',
    epilog='Thanks for using SuperPy!'
    ) 
   

subparsers = global_parser.add_subparsers(
    title='subcommands', help='info about bought and sold products in the supermarket'
)

arg_template = {
    'dest': 'functions',
    'metavar': 'FUNCTION',
    'help': 'Type the function in.'
}


#1
create_folder_parser = subparsers.add_parser('create folder', help='specify folder name')
create_folder_parser.add_argument(nargs=1, type=str, default='products_csv', **arg_template)
create_folder_parser.set_defaults(func=main.create_folder)

#2
create_csv_file_parser = subparsers.add_parser('file', help='enter file name as csv and a header list')
create_csv_file_parser.add_argument(nargs=2, 
                                    choices=[('bought.csv', ['buy_id',' product_name',' buy_date',' buy_price',' expiration_date']), 
                                             ('sold.csv', ['sell_id', 'buy_id', 'product_name', ' sell_date',' sell_price'])],
                                    default=('bought.csv', ['buy_id',' product_name',' buy_date',' buy_price',' expiration_date']),
                                    **arg_template)
create_csv_file_parser.set_defaults(func=main.create_csv_file)
#3
add_csv_values_parser = subparsers.add_parser('value', help='specify product name, whihc was bought/sold')
add_csv_values_parser.add_argument(nargs=1, type=str, **arg_template)
add_csv_values_parser.set_defaults(func=main.add_csv_values)
#The previous 3 parsers do not meant to be used in general, but are here in case user needs the program for files creation also.

#4
buy_parser = subparsers.add_parser('buy', help="enter product name. it's price and expiration date")
buy_parser.add_argument(nargs=3,**arg_template)
buy_parser.set_defaults(func=main.buy)

#5
sell_parser = subparsers.add_parser('sell', help="enter name of sold product and it's sell price")
sell_parser.add_argument(nargs=2,**arg_template)
sell_parser.set_defaults(func=main.sell)

#6
advance_time_parser = subparsers.add_parser('advance time', help="enter number of days, when you want to check the expiration date from now")
advance_time_parser.add_argument(nargs=1, type=int, default = 1, **arg_template)
advance_time_parser.set_defaults(func=main.advance_time)

#7
report_inventory_parser = subparsers.add_parser('report inventory', help="enter date in format yyyy-mm-dd or enter 'now' or 'yesterday'")
report_inventory_parser.add_argument(nargs=1, type=str, default = 'now', **arg_template)
report_inventory_parser.set_defaults(func=main.report_inventory)


#8
report_revenue_parser = subparsers.add_parser('report revenue', help="enter date in format yyyy-mm-dd/yyyy-mm/yyyy or enter 'today' or 'yesterday'")
report_revenue_parser.add_argument(nargs=1,type=str, default = 'today', **arg_template)
report_revenue_parser.set_defaults(func=main.report_revenue)

#9
report_profit_parser = subparsers.add_parser('report profit', help="enter date in format yyyy-mm-dd/yyyy-mm/yyyy or enter 'today' or 'yesterday'")
report_profit_parser.add_argument(nargs=1,type=str, default = 'today', **arg_template)
report_profit_parser.set_defaults(func=main.report_profit)

#10
csv_to_excel_parser = subparsers.add_parser('csv to excel', help="enter name of csv file and of excel file")
csv_to_excel_parser.add_argument(nargs=2,type=str,**arg_template)
csv_to_excel_parser.set_defaults(func=main.csv_to_excel)

#11
spent_vs_profit_parser = subparsers.add_parser('spent vs profit', help="enter date in format yyyy-mm-dd/yyyy-mm/yyyy or enter 'today' or 'yesterday'")
spent_vs_profit_parser.add_argument(nargs=1,default = 'today',**arg_template)
spent_vs_profit_parser.set_defaults(func=main.spent_vs_profit)

args = global_parser.parse_args()

try:
    args.func(args)
except AttributeError:
    global_parser.print_help()
    global_parser.exit()

#print(args.func(*args.functions))


sys.stdin.read()
sys.stdout.write(args.func(*args.functions))
