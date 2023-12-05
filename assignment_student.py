import sys

# 1. Declare two constant variables named COMBO_MEAL_PRICE and COLD_DRINK_PRICE



# 2. Complete the function read_burger_from_file to read in burgers information from file named "burger_list.csv"
def read_burger_from_file():
    # Zero marks will be given if you assigned the burger data by this static variable

    list_dict_burgers = list()
    filename = "burger_list.csv"
    # your implemention starts here














    # This static variable is for your development in early stage
    # Comment out this static variable after you completed your implementation of read from file
    
    list_dict_burgers = [
        {'Name': 'Queens\'s Signature', 'Price': 45.0},
        {'Name': 'Cheeseburger', 'Price': 25.0},
        {'Name': 'Chili Burger', 'Price': 32.0},
        {'Name': 'Olive Burger', 'Price': 36.0},
        {'Name': 'Beef Burger', 'Price': 40.0}
    ]

    return list_dict_burgers



# Complete your compute_sales function here
def compute_sales(burger_price, combo_meal, cold_drink, quantity):

    sales = 0

    # your implemention starts here









    
    return sales

# You may implement other necessary functions here






def main():

    # 3. Declare a list of dictionary named list_dict_burgers in main function
    #    to store all burgers information returned by the function read_burger_from_file()
    list_dict_burgers = read_burger_from_file()
  
    # 4. list of tuple to store all burger orders which are not yet completed by customer
    list_tuple_current_sales = list()

    # 5. dictionary to accumulate the quantity sold for each type of burger
    dict_no_of_burgers_sold = dict()

    # your implemention starts here
    # Display a welcome message and followed by the main menu of Burger Queen Food Ordering system






















































if __name__ == "__main__":
    main()
