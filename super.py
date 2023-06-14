import argparse
import main
import sys

global_parser = argparse.ArgumentParser(
    prog='super.py',
    description='Keeps track and produces reports on various kinds of data of the supermarket.',
    epilog='Thanks for using SuperPy!'
    ) 
   

subparsers = global_parser.add_subparsers(
    title='subcommands', help='info about bought and sold products in the supermarket', dest = 'command'
    )

"""arg_template = {
    'metavar': 'FUNCTION',
    'help': 'Type the function in.'
}"""


#1
create_folder_parser = subparsers.add_parser('create_folder', help='specify folder name')
create_folder_parser.add_argument('--folder_name', nargs=1, type=str, default='products_csv')
#create_folder_parser.set_defaults(func=main.create_folder)

#2
create_csv_file_parser = subparsers.add_parser('create_csv_file', help='enter file name as csv and a header list', )
create_csv_file_parser.add_argument(nargs=2, dest = 'command',
                                    choices=[('bought.csv', ['buy_id',' product_name',' buy_date',' buy_price',' expiration_date']), 
                                             ('sold.csv', ['sell_id', 'buy_id', 'product_name', ' sell_date',' sell_price'])],
                                    default=('bought.csv', ['buy_id',' product_name',' buy_date',' buy_price',' expiration_date'])
                                    )
#create_csv_file_parser.set_defaults(func=main.create_csv_file)

#3
add_csv_values_parser = subparsers.add_parser('add_csv_values', help='specify product name, whihc was bought/sold')
add_csv_values_parser.add_argument(nargs=1, type=str, dest = 'command')
#add_csv_values_parser.set_defaults(func=main.add_csv_values)
#The previous 3 parsers are not meant to be used in general, but are here in case user needs the program for files creation also.

#4 
read_date_csv_parser = subparsers.add_parser('read_date_csv', help='returns the date which is saved in csv file')
read_date_csv_parser.add_argument('--date', dest = 'command')
#read_date_csv_parser.set_defaults(func=main.read_date_csv)


#5
buy_parser = subparsers.add_parser('buy', help="enter product name. it's price and expiration date")
buy_parser.add_argument(nargs=3, dest = 'command')
#buy_parser.set_defaults(func=main.buy)

#6
sell_parser = subparsers.add_parser('sell', help="enter name of sold product and it's sell price")
sell_parser.add_argument(nargs=2, dest = 'command')
#sell_parser.set_defaults(func=main.sell)

#7 
set_date_parser = subparsers.add_parser('set_date', help="enter name of sold product and it's sell price")
set_date_parser.add_argument('--date', required=True, nargs=1, type=str, dest = 'command')
#set_date_parser.set_defaults(func=main.set_date)  

#8
advance_time_parser = subparsers.add_parser('advance_time', help="enter number of days, when you want to check the expiration date from now")
advance_time_parser.add_argument('-n', nargs=1, type=int, dest = 'command')
advance_time_parser.add_argument('-d', nargs=1, type=str, dest = 'command')
#advance_time_parser.add_argument('-d','--date', required=True, type=str, dest = 'command')

#9
report_inventory_parser = subparsers.add_parser('report_inventory', help="enter date in format yyyy-mm-dd or enter 'now' or 'yesterday'")
report_inventory_parser.add_argument(nargs=1, type=str, default = 'now', dest = 'command')
#report_inventory_parser.set_defaults(func=main.report_inventory)


#10
report_revenue_parser = subparsers.add_parser('report_revenue', help="enter date in format yyyy-mm-dd/yyyy-mm/yyyy or enter 'today' or 'yesterday'")
report_revenue_parser.add_argument(nargs=1,type=str, default = 'today', dest = 'command')
#report_revenue_parser.set_defaults(func=main.report_revenue)

#11
report_profit_parser = subparsers.add_parser('report_profit', help="enter date in format yyyy-mm-dd/yyyy-mm/yyyy or enter 'today' or 'yesterday'")
report_profit_parser.add_argument(nargs=1,type=str, default = 'today', dest = 'command')
#report_profit_parser.set_defaults(func=main.report_profit)

#12
csv_to_excel_parser = subparsers.add_parser('csv_to_excel', help="enter name of csv file and of excel file")
csv_to_excel_parser.add_argument(nargs=2,type=str, dest = 'command')
#csv_to_excel_parser.set_defaults(func=main.csv_to_excel)

#13
spent_vs_profit_parser = subparsers.add_parser('spent_vs_profit', help="enter date in format yyyy-mm-dd/yyyy-mm/yyyy or enter 'today' or 'yesterday'")
spent_vs_profit_parser.add_argument(nargs=1,default = 'today', dest = 'command')
#spent_vs_profit_parser.set_defaults(func=main.spent_vs_profit)



args = global_parser.parse_args()


#all parsers

if args.command == 'create_folder':
    create_folder_parser.set_defaults(func=main.create_folder)
elif args.command == 'create_csv_file':
    create_csv_file_parser.set_defaults(func=main.create_csv_file)
elif args.command == 'add_csv_values':
    add_csv_values_parser.set_defaults(func=main.add_csv_values)
elif args.command == 'read_date_csv':
    read_date_csv_parser.set_defaults(func=main.read_date_csv)
elif args.command == 'buy':
    buy_parser.set_defaults(func=main.buy)
elif args.command == 'sell':
    sell_parser.set_defaults(func=main.sell)
elif args.command == 'set_date':
    set_date_parser.set_defaults(func=main.set_date)
elif args.command == 'advance_time':
    advance_time_parser.set_defaults(func=main.advance_time) 
elif args.command == 'report_inventory':
    report_inventory_parser.set_defaults(func=main.report_inventory)
elif args.command == 'report_revenue':
    report_revenue_parser.set_defaults(func=main.report_revenue)
elif args.command == 'report_profit':
    report_profit_parser.set_defaults(func=main.report_profit)
elif args.command == 'csv_to_excel':
    csv_to_excel_parser.set_defaults(func=main.csv_to_excel)
elif args.command == 'spent_vs_profit':
    spent_vs_profit_parser.set_defaults(func=main.spent_vs_profit)


    

#sys.stdout.write(args.command(*args.command))
"""try:
    args.func(args)
except AttributeError:
    global_parser.print_help()
    global_parser.exit()

#print(args.func(*args.functions))


sys.stdin.read()
sys.stdout.write(args.func(*args.functions))"""
