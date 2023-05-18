Three technical elements of the implementation:

1. 'if' statement for checking the project path, which makes sure the user will be always in the correct directory.
    Example:
    'project_path = os.getcwd()
    if project_name not in project_path:
        project_path = os.path.join(os.getcwd(), project_name)'

2. using 'assert' in few functions, which allows to make sure the date variable will be given in a correct format.

3. displaying results for 'report_inventory' function in table format.
    Example:
    'header = ['Id', 'Product', 'Count', 'Price', 'Expiry date']
    format_row = "{:>15}" * (len(header) + 1)
    print(f'Inventory on {date}:')
    print(format_row.format("", *header)) 
    for data in inventory_list: 
        print(format_row.format("",*data))'
