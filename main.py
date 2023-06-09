# Imports

import csv
from datetime import date, datetime, timedelta
import os
import itertools
from collections import Counter
import pandas as pd
import sys
from uuid import uuid4




# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass


if __name__ == "__main__":
    main()


      
    
# PRODUCTS
# When a new product has been bought/sold, new child class object is being created. 
# If product with same price and expiry date bought few times, the same buy_id would be used, thus an existing child_class for bought product to be used. Otherwise, new object to be created with new buy_id.
# Anytime when a product sold, the sell_id would be different each time.
class Product:
    def __init__(self, product_name:str):
        self.product_name = product_name

class BoughtProduct(Product):
    new_id = itertools.count(1)
    def __init__(self, product_name, buy_price, expiration_date):
        self.buy_id = next(BoughtProduct.new_id)
        super().__init__(product_name)
        self.buy_date = date.today() #the system automatically saves info into csv file once bought
        self.buy_price = buy_price
        self.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()

class SoldProduct(Product):
    new_id = itertools.count(2)
    def __init__(self, buy_id, product_name, sell_price):
        self.sell_id = next(SoldProduct.new_id)
        self.buy_id = buy_id
        super().__init__(product_name)
        self.sell_date = date.today() #the system automatically saves info into csv file once sold
        self.sell_price = sell_price

        


# TO STORE PRODUCTS DATA


project_name = 'superpy'
folder_name = 'products_csv'

project_path = os.getcwd()
if project_name not in project_path:
    project_path = os.path.join(os.getcwd(), project_name)

folder_path = os.path.join(project_path, folder_name)


#1
def create_folder(folder_name:str):   
    if os.getcwd() != project_path: 
        os.chdir(project_path)
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    else:
        return f'The folder already exists.'


#2
def create_csv_file(csv_name):    
    if os.getcwd() != folder_path:
        os.chdir(folder_path)  
        csv_path = os.path.join(folder_path, csv_name)
        if not os.path.isfile(csv_path):    
            with open (csv_path, 'w', newline='') as csv_name:
                if 'bought' in csv_path:
                    writer = csv.writer(csv_name, delimiter = '|')
                    writer.writerow(['buy_id',' product_name',' buy_date',' buy_price',' expiration_date'])
                elif 'sold' in csv_path:
                    writer = csv.writer(csv_name, delimiter = '|')
                    writer.writerow(['sell_id', 'buy_id', 'product_name', ' sell_date',' sell_price'])
                else:
                    return f'Enter correct file name: sold.csv or bought.csv.'

        else:
            return f'The file already exists.'
        
#print(create_csv_file('bought.csv'))
    


def bought_product_tulpe(product=BoughtProduct):
        return (product.buy_id, product.product_name, product.buy_date, product.buy_price, product.expiration_date)

def sold_product_tulpe(product=SoldProduct):        
        return (product.sell_id, product.buy_id, product.product_name, product.sell_date, product.sell_price)



buy_csv_path = os.path.join(folder_path, 'bought.csv')
sell_csv_path = os.path.join(folder_path, 'sold.csv')
if os.path.isfile(buy_csv_path):
    file1 = open(buy_csv_path, 'r') 
    csvreader1 = csv.reader(file1, delimiter='|')
    
if os.path.isfile(sell_csv_path):
    file2 = open(sell_csv_path, 'r') 
    csvreader2 = csv.reader(file2, delimiter='|')

#3 -> to be used from command line 
def add_csv_values(name):
    name=sys.argv[3]
    price=sys.argv[5]
    value=sys.argv[7]
    if os.getcwd() != folder_path:
        os.chdir(folder_path)
        
    if 'buy' in sys.argv[4]:
        name = BoughtProduct(name, price, value)
        lst = []
        
        csv_path = os.path.join(folder_path, 'bought.csv')
        next(csvreader1)
        for row in csvreader1:
            id = row [0]      
            lst.append(int(id))
            
            product = row[1]
            price = row[3]
            exp_d = row[4]
            if name.product_name == product.lower() and name.expiration_date == exp_d:
                name.buy_id = id
            elif name.product_name == product.lower() and name.expiration_date != exp_d or name.product_name != product.lower():
                name.buy_id = max(lst) + 1               

        with open(csv_path, 'a', newline='') as stream:
            writer = csv.writer(stream, delimiter = '|')
            line = bought_product_tulpe(name)
            writer.writerow(line)
            return f'Product added to bought.csv file with buy_d {name.buy_id}.'

    elif 'sell' in sys.argv[4] :
        next(csvreader1)
        for row in csvreader1:
            buy_id = row[0]   
            bought_product = row[1]
            if buy_id == value and bought_product.lower() == sys.argv[3]:
                               
                name = SoldProduct(value, sys.argv[3], price)
                csv_path = os.path.join(folder_path, 'sold.csv')
                lst = []
                
                next(csvreader2)
                for row in csvreader2:
                    id = row [0]      
                    lst.append(int(id))
                    name.sell_id = max(lst) + 1

                with open(csv_path, 'a', newline='') as stream:
                    writer = csv.writer(stream, delimiter = '|')
                    line = sold_product_tulpe(name)
                    writer.writerow(line)
                    return f'Product added to sold.csv file with sell_id {name.sell_id}.'
            
            
#print(add_csv_values('orange'))
#3-> to be used on back end if there is a created class object.
def add_csv_values_internal(product):
    if os.getcwd() != folder_path:
        os.chdir(folder_path)
    if hasattr(product, 'buy_price'):
        csv_path = os.path.join(folder_path, 'bought.csv')
        with open(csv_path, 'a', newline='') as stream:
            writer = csv.writer(stream, delimiter = '|')
            row = bought_product_tulpe(product)
            writer.writerow(row)
    elif hasattr(product, 'sell_price'):
        csv_path = os.path.join(folder_path, 'sold.csv')
        with open(csv_path, 'a', newline='') as stream:
            writer = csv.writer(stream, delimiter = '|')
            row = sold_product_tulpe(product)
            writer.writerow(row)
    else:
        return f'no buy_price or sell_price attribute'
    

#Example products:
"""orange = BoughtProduct('Orange', 2.34, '2023-4-25')
banana = BoughtProduct('Banana', 1.5, '2023-5-6')
milk = BoughtProduct('Milk', 2, '2023-2-25')
cherry = BoughtProduct('Cherry', 2, '2023-2-25')
bread = BoughtProduct('Bread', 0.8, '2023-04-13')
salt = BoughtProduct('Salt', 0.2, '2025-11-8')
choco = BoughtProduct('Chocolatte', 3.0, '2024-2-11')
potatos = BoughtProduct('Potatos', 0.45, '2023-7-25')
tomato = BoughtProduct('Tomatos', 1.25, '2023-4-20')
cream = BoughtProduct('Cream', 5.0, '2026-4-25')
onion = BoughtProduct('Onion', 1.0, '2024-4-25')
ketchup = BoughtProduct('Ketchup', 1.3, '2027-1-13')
x = BoughtProduct('X', 1.5, '2026-2-3')
apple = BoughtProduct('Apple', 0.3, '2023-05-10')
juice = BoughtProduct('Juice', 1.5, '2026-12-04')"""




"""orange = SoldProduct(orange.buy_id,'Orange', 3.00)
banana = SoldProduct(banana.buy_id,'Banana', 2.0)
milk = SoldProduct(milk.buy_id,'Milk', 3.0)
cherry = SoldProduct(cherry.buy_id,'Cherry', 2.0)
bread = SoldProduct( bread.buy_id,'Bread', 1.5)
salt = SoldProduct(salt.buy_id, 'Salt', 0.5)
tomato = SoldProduct(tomato.buy_id,'Tomato', 2.0)
potatos = SoldProduct(potatos.buy_id, 'Potatos', 0.75)
juice = SoldProduct(juice.buy_id, 'Juice', 3.5)"""
     
#print(add_csv_values_internal(cherry))

default_date = date.today()


#4 returns the date saved in csv file   
  
def read_date_csv(date:str):
    if os.getcwd() != folder_path:
        os.chdir(folder_path)
    new_date = default_date.strftime('%Y-%m-%d')
    csv_path = (os.path.join(folder_path, 'date.csv'))
    if not os.path.isfile(csv_path):
        with open (csv_path, 'w') as csv_name:
                writer = csv.writer(csv_name)
                writer.writerow([new_date]) 
        date_read = open(csv_path, 'r') 
        date_reader = csv.reader(date_read)
        for date in date_reader:
            for d in date:
                return d    
    else: 
        date_read = open(csv_path, 'r') 
        date_reader = csv.reader(date_read)
        for date in date_reader:
            for d in date:
                return d
                
        

#print(read_date_csv('x'))
 
# PROGRAM FUNCTIONALITIES



#5 - to check if the product has been bought.
def buy(product_name, price, expiration_date):
    for row in csvreader1:
        if product_name == row[1] and price == row[3] and expiration_date == row[4]:
            return f'OK'   
        elif product_name == row[1] and price != row[3] and expiration_date == row[4]:
            return f'Product bought for different price: {row[3]}.'
        elif product_name == row[1] and price == row[3] and expiration_date != row[4]:
            return f'Product bought has different expiration date: {row[4]}.'
       
 
#6 - to check if product has been sold or expired, if not.       
def sell(product_name, sell_price):
    for row in csvreader1:
        if product_name == row[1]:
            for sell_row in csvreader2:
                if row[0] != sell_row[1] and sell_price == sell_row[4]:
                    exp_date = datetime.strptime(row[4], '%Y-%m-%d').date()
                    if exp_date > default_date:
                        return f'Product has expired.'
                elif row[0] == sell_row[1] and sell_price == sell_row[4]:
                    sold_dates = []
                    sell_date = sell_row[3]
                    sold_dates.append(sell_date)
                    return f'Sold on {sold_dates}.'
                elif row[0] == sell_row[1] and sell_price != sell_row[4]:
                    return f'Sold for different price: {sell_row[4]} EUR.' 
                

#7 changes the date in csv file               
def set_date(new_date):
    with open((os.path.join(folder_path, 'date.csv')), 'w') as stream:
        writer = csv.writer(stream)
        new_date = [datetime.strptime(new_date, '%Y-%m-%d').date()]
        writer.writerow(new_date)
   
#print(set_date('2023-04-05'))

                 
#8 - to check if product will be expired in the given number of days    
def advance_time(input):
    try:
        if type(input) == int:
            csv_date = read_date_csv('x')
            if type(csv_date) == str:
                csv_date = datetime.strptime(csv_date, '%Y-%m-%d').date()            
                required_date = csv_date + timedelta(input)
            else:
                required_date = default_date + timedelta(input)       
        elif len(input) == 10:       
            required_date = datetime.strptime(input, '%Y-%m-%d').date()
            

        set_date(required_date.strftime('%Y-%m-%d'))
        expired_products = []      
        next(csvreader1)
        
        for row in csvreader1:
            date_str = row[4]
            exp_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            if exp_date < required_date and isinstance(required_date, date):            
                if (row[0], row[1]) not in expired_products:                
                    expired_products.append((row[0], row[1]))                     
        required_date_str = required_date.strftime('%d %b %Y')
        return f'Following products expired on {required_date_str}: {expired_products}.'
    except ValueError:
            return f'Enter a valid date'
    
#print(advance_time(9))
   

#9 - to check what products are in stock on the given date.
def report_inventory(date:str):
    assert isinstance(date, str),\
    f'date should be string in format yyyy-mm-dd or enter "now" or "yesterday", got {type(date), date}'
    if date == 'now':
        date = default_date
    elif date == 'yesterday':
        date = default_date - timedelta(1)
    else:
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return f'Enter a valid date.'
    
    if date <= default_date:
        inventory_list = []
        
        next(csvreader1) 
                
        counts = Counter(map(tuple,csvreader1))
        for k, v in counts.items():
            if k[2] <= date.strftime('%Y-%m-%d'):
                number_products = v
                id = k[0]
                product = k[1]
                price = k[3]
                exp_date = k[4]                     
                data = [id, product, number_products, price, exp_date]
                inventory_list.append(data)  
        next(csvreader2)
        for row in csvreader2:
            for item in inventory_list:
                if item[0] in row[1] and row[3] <= date.strftime('%Y-%m-%d'):
                    inventory_list.remove(item)
                                
            
        header = ['Id', 'Product', 'Count', 'Price', 'Expiry date']
        format_row = "{:>15}" * (len(header) + 1)
        print(f'Inventory on {date}:')
        print(format_row.format("", *header)) 
        for data in inventory_list: 
            print(format_row.format("",*data))  
    else:
        return f'Date should not be in the future'

#print(report_inventory('2023-09-09'))           
               

#10 - to check revenue on a specific date/month/year.    
def report_revenue(date):
    assert isinstance(date, str),\
    f'date should be string in format yyyy-mm-dd/yyyy-mm/yyyy or enter "today" or "yesterday", got {type(date), date}'
    if date == 'today':
        date = default_date
        date = date.strftime('%Y-%m-%d')
    elif date == 'yesterday':
        date = default_date - timedelta(1)
        date = date.strftime('%Y-%m-%d')
    else: 
        if len(date) == 10:
            
            try:
                datetime.strptime(date,'%Y-%m-%d').date()

            except ValueError:
                return f'Enter a valid date.'
        elif len(date) == 7:
            
            try:
                datetime.strptime(date,'%Y-%m').date()

            except ValueError:
                return f'Enter a valid month.'
        elif len(date) == 4:
            
            try:
                datetime.strptime(date,'%Y').date()

            except ValueError:
                return f'Enter a valid year.'
        else:
            return f'Enter a valid date.'
        

   
    if date <= default_date.strftime('%Y-%m-%d') or date < default_date.strftime('%Y-%m') or date < default_date.strftime('%Y'):
        

        next(csvreader2)
        prices = []
        for row in csvreader2:       
            if date in row[3]:
                item_price = row[4]
                item_price = float(item_price)
                prices.append(item_price)
        revenue = sum(prices)       
        return f'{date}: revenue was {revenue} EUR.'
        
            
    else:
        return f'Date should not be in the future.'
    
   
    
#print(report_revenue('19999-12-31'))

#11 - to check profit on a specific date/month/year.
def report_profit(date):
    assert isinstance(date, str),\
    f'date should be string in format yyyy-mm-dd/yyyy-mm/yyyy or enter "today" or "yesterday", got {type(date), date}'
    if date == 'today':
        date = default_date
        date = date.strftime('%Y-%m-%d')
    elif date == 'yesterday':
        date = default_date - timedelta(1)
        date = date.strftime('%Y-%m-%d')
    else: 
        if len(date) == 10:
            
            try:
                datetime.strptime(date,'%Y-%m-%d').date()

            except ValueError:
                return f'Enter a valid date.'
        elif len(date) == 7:
            
            try:
                datetime.strptime(date,'%Y-%m').date()

            except ValueError:
                return f'Enter a valid month.'
        elif len(date) == 4:
            
            try:
                datetime.strptime(date,'%Y').date()

            except ValueError:
                return f'Enter a valid year.'
        else:
            return f'Enter a valid date.'
        

   
    if date <= default_date.strftime('%Y-%m-%d') or date < default_date.strftime('%Y-%m') or date < default_date.strftime('%Y'):
        

        next(csvreader1)
        costs = []
        for row in csvreader1:       
            if date in row[2]:
                item_cost = row[3]
                item_cost= float(item_cost)
                costs.append(item_cost)
        spent = sum(costs) 
    
        next(csvreader2)
        prices = []
        for row in csvreader2:       
            if date in row[3]:
                item_price = row[4]
                item_price = float(item_price)
                prices.append(item_price)
        revenue = sum(prices)    
        profit = revenue - spent     
        return f'{date}: profit was {round(profit,2)} EUR.' 
    else:
        return f'Date should not be in the future.'  
#print(report_profit('2023-14-30'))


#12 - to export csv data into excel sheet, which will be created automatically.
def csv_to_excel(csv_filename:str, excel_filename:str):   
    if os.getcwd() != folder_path:
        os.chdir(folder_path)  
        csv_path = os.path.join(folder_path, csv_filename)
        result_excel_file = pd.ExcelWriter(excel_filename)
        excel_path = os.path.join(folder_path, result_excel_file)
    # Read CSV file
    read_csv = pd.read_csv(csv_path)

    # Import to Excel  
    read_csv.to_excel(excel_path, index=True)



#13 - to display pie-chart.
def spent_vs_revenue(date):    
    if date == 'today':
        date = default_date
        date = date.strftime('%Y-%m-%d')
    elif date == 'yesterday':
        date = default_date - timedelta(1)
        date = date.strftime('%Y-%m-%d')
    else: 
        if len(date) == 10:
            
            try:
                datetime.strptime(date,'%Y-%m-%d').date()

            except ValueError:
                return f'Enter a valid date.'
        elif len(date) == 7:
            
            try:
                datetime.strptime(date,'%Y-%m').date()

            except ValueError:
                return f'Enter a valid month.'
        elif len(date) == 4:
            
            try:
                datetime.strptime(date,'%Y').date()

            except ValueError:
                return f'Enter a valid year.'
        else:
            return f'Enter a valid date.'
        

   
    if date <= default_date.strftime('%Y-%m-%d') or date < default_date.strftime('%Y-%m') or date < default_date.strftime('%Y'):
              
        next(csvreader1)
        costs = []
        for row in csvreader1:       
            if date in row[2]:
                item_cost = row[3]
                item_cost= float(item_cost)
                costs.append(item_cost)
            else:
                return f'no items bought on this date'
        spent = sum(costs)
        next(csvreader2)
        prices = []
        for row in csvreader2:       
            if date in row[3]:
                item_price = row[4]
                item_price = float(item_price)
                prices.append(item_price)
            else:
                return f'no items sold on this date'
        revenue = sum(prices)
        

        import matplotlib.pyplot as plt
        import numpy as np

        plt.style.use('_mpl-gallery-nogrid')
        # make data
        x = [spent, revenue]
        colors = ['red','blue']
        # plot
        fig, ax = plt.subplots()
        ax.pie(x, colors=colors, radius=3, center=(4, 4),
            wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))
        
        print(f'This is chart "spent(red) vs. revenue(blue)" for {date}.')
        plt.show()
    else:
        return f'Date should not be in the future.'
    
#print(spent_vs_revenue("2023"))
    
   









