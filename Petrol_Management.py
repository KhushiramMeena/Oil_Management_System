# Importing directories for implementation.
from typing import IO
import numpy as np                      # NUMPY
import pandas as pd                     # PANDAS
from matplotlib import pyplot as plt    # MATPLOTLIB
import matplotlib.dates as mdates
import random                           # RANDOM


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                                   INNER WORKING SECTION                                     """
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# Class for User Login
class User:
    # Default User Name and Password
    def __init__(self):
        self.__username = "admin"
        self.__password = "python_manage"
        self.__code = "1211"    

    # Function to validate user name and password
    def validatePassword(self,userE, passE):
        # Check for user name
        if self.__username == userE and self.__password == passE:
            return True

        # Details match only if check point is 2
        return False
            
    # Backup in case on have forgotten his/her password
    def forgotPassword(self, code):
        if self.__code == code:
            return True
        
        else:
            return False
            
        

# Defining a function for printing the Documentation of the Project
def printDocumentation(fileName):
    # Exception Handling in case of Invalid File name
    try:
        # Opening the Documentation File for reading.
        f = open(fileName+".txt","r")
    
    # Catching an error if the entered file name in invalid
    except FileNotFoundError:
        print("Please once check the name of the file to be entered!")
        return


    # Printing the title of the system in the centre
    print("\t\t\t", f.readline())

    # Then printing the rest of the text
    print(f.read())
    # Two blank lines space are left after the last line of the text


    # Closing the file
    f.close()



# This shall determine if one has login correctly or not
loginFlag = 0

# Create an object of class User        
login = User()

# ------------------------------------ Customer Details ------------------------------------------
try:
    #setting dataframe with unique names to read excel sheet
    df_customer = pd.read_excel('customer_details.xlsx', sheet_name='Sheet1')
    
except IOError:
    #setting dataframes with unique names if Excels sheet does not exists
    df_customer = pd.DataFrame(columns=['Customer ID', 'Name', 'State', 'Address'])

#class Production
class Customer_Details:
    def __init__(self,customer_id,customer_name,customer_state,customer_address):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_state = customer_state
        self.customer_address = customer_address

# function to add row in customer dataframe which user has given input
    def Customer_addRow(self,row):
        df_customer.loc[row] = [ self.customer_id, self.customer_name, self.customer_state, self.customer_address]

# delete row function to delete a particular file in production dataframe
    def Customer_deleteRow(self):
            df_customer1 = df_customer.query(f'Customer ID!={self.customer_id}')
            
            print('Your Customer ID row is deleted successfully')
            print(df_customer1)
            return df_customer1

# search row function to search a row in production dataframe
    def Customer_searchRow(self):
        try:
            df_customer1 = df_customer.query(f'PUN=={self.pun}')
            print(df_customer1)
        except:
            print('Invalid input')

#function to export the data present in production dataframe
    def export_Customer_data(self):
            writer = pd.ExcelWriter('customer_details.xlsx')
            df_customer.to_excel(writer,sheet_name='Sheet1',index=False)
            writer.save()
            print('Your excel sheet is saved successfully as customer_details.xlsx')

# ------------------------------------------------------------------------------------------------

# ------------------------------------ Employee Details ------------------------------------------
try:
    #setting dataframe with unique names to read excel sheet
    df_employee = pd.read_excel('employee_details.xlsx', sheet_name='Sheet1')
    
except IOError:
    #setting dataframes with unique names if Excels sheet does not exists
    df_employee = pd.DataFrame(columns=['Employee ID', 'Name', 'Date of Joining', 'Department'])

#class Production
class Employee_Details:
    def __init__(self,employee_id,employee_name,employee_date,employee_department):
        self.employee_id = employee_id                      # String
        self.employee_name = employee_name                  # String
        self.employee_date = employee_date                  # String
        self.employee_department = employee_department      # String

# function to add row in customer dataframe which user has given input
    def Employee_addRow(self,row):
        df_employee.loc[row] = [ self.employee_id, self.employee_name, self.employee_date, self.employee_department]

# delete row function to delete a particular file in production dataframe
    def Employee_deleteRow(self):
            df_employee1 = df_employee.query(f'Employee ID!={self.employee_id}')
            
            print('Your Employee ID row is deleted successfully')
            print(df_employee1)
            return df_employee1

# search row function to search a row in production dataframe
    def Employee_searchRow(self):
        try:
            df_employee1 = df_employee.query(f'PUN=={self.pun}')
            print(df_employee1)
        except:
            print('Invalid input')

#function to export the data present in production dataframe
    def export_Employee_data(self):
            writer = pd.ExcelWriter('employee_details.xlsx')
            df_employee.to_excel(writer,sheet_name='Sheet1',index=False)
            writer.save()
            print('Your excel sheet is saved successfully as employee_details.xlsx')

# ------------------------------------------------------------------------------------------------

# ------------------------------------ Production Section ----------------------------------------
try:
    #setting dataframe with unique names to read excel sheet
    df_production = pd.read_excel('production_details.xlsx', sheet_name='Sheet1')
    
except IOError:
    #setting dataframes with unique names if Excels sheet does not exists
    df_production = pd.DataFrame(columns=['PUN', 'Fuel_output', 'Production_Cost', 'Date_of_arrival'])

#class Production
class Production_Details:
    def __init__(self,pun,fuel_output,cost,arrival_date):
        self.pun = pun
        self.fuel_output = fuel_output
        self.cost = cost
        self.arrival_date = arrival_date

# function to add row in production dataframe which user has given input
    def Production_addRow(self,row):
            df_production.loc[row, 'PUN'] = self.pun
            df_production.loc[row, 'Fuel_output'] = self.fuel_output
            df_production.loc[row, 'Production_Cost'] = self.cost
            df_production.loc[row, 'Date_of_arrival'] = self.arrival_date

# delete row function to delete a particular file in production dataframe
    def Production_deleteRow(self):
            df_production1 = df_production.query(f'PUN!={self.pun}')
            
            print('Your PUN row is deleted successfully')
            print(df_production1)
            return df_production1

# search row function to search a row in production dataframe
    def Production_searchRow(self):
        try:
            df_production1 = df_production.query(f'PUN=={self.pun}')
            print(df_production1)
        except:
            print('Invalid input')

#function to export the data present in production dataframe
    def export_Production_data(self):
            writer = pd.ExcelWriter('production_details.xlsx')
            df_production.to_excel(writer,sheet_name='Sheet1',index=False)
            writer.save()
            print('Your excel sheet is saved successfully as production_details.xlsx')
     
# --------------------------------------------------------------------------------------------

# ------------------------------------ Demand Section ----------------------------------------

try:
    #setting dataframe with unique names to read excel sheet
    df_demand = pd.read_excel('demand_details.xlsx',sheet_name='Sheet1')
except IOError:
    #setting dataframes with unique names if Excels sheet does not exists
    df_demand = pd.DataFrame(columns=['Order_id', 'ID', 'Demand', 'Fuel_given', 'Selling_price', 'Date', 'Transaction_Id', 'Transaction_status'])

#class demand
class Demand_Details:
    def __init__(self,order_id, id, demand, fuel_given, price, date, transaction_id, transaction_status):
        self.order_id = order_id
        self.id = id
        self.demand = demand
        self.fuel_given = fuel_given
        self.price = price
        self.date = date
        self.transaction_id = transaction_id
        self.transaction_status = transaction_status

#function to add row to demand dataframe which user has given input
    def Demand_addRow(self,row):
            df_demand.loc[row, 'Order_id'] = self.order_id
            df_demand.loc[row, 'ID'] = self.id
            df_demand.loc[row, 'Demand'] = self.demand
            df_demand.loc[row, 'Fuel_given'] = self.fuel_given
            df_demand.loc[row, 'Selling_price'] = self.price
            df_demand.loc[row, 'Date'] = self.date
            df_demand.loc[row, 'Transaction_Id'] = self.transaction_id
            df_demand.loc[row, 'Transaction_status'] = self.transaction_status

#function to delete a row from demand dataframe
    def Demand_deleteRow(self):
            try:
                df_demand1 = df_demand.query(f'Order_id!={self.order_id}')
                print('your order id is deleted successfully')
                print(df_demand1)
                return df_demand1
            
            except:
                print('Invalid Input')
            
# function to search in the demand dataframe
    def Demand_searchRow(self):
        try:
            df_demand1 = df_demand.query(f'Order_id=={self.order_id}')
            print(df_demand1)
        except:
            print('Invalid input')

# function to export the data from demand dataframe to excel sheet
    def export_Demand_data(self):
        writer = pd.ExcelWriter('demand_details.xlsx')
        df_demand.to_excel(writer,sheet_name='Sheet1',index=False)
        writer.save()
        print('Your excel sheet is saved successfully as demand_details.xlsx')
    
# --------------------------------------------------------------------------------------------



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                                        MENU SECTION                                         """
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# ------------------------------ SECTION FOR LOGIN ------------------------------

# Getting username and pssword from the user.
enteredUser = input("Enter the username for login:\n")
enteredPass = input("Enter the password for login:\n")

# Validating the entered username and password
uploginFlag = login.validatePassword(enteredUser, enteredPass)

# In case of successful login
if uploginFlag == True:
    loginFlag = True
    
else:
    print("Entered username/password is invalid")
    
    print("Do you want to login through code?")
    choice = input("Enter Y for yes or N for no\n")
    if choice == 'Y':
        enteredCode = input("Enter the code for login\n")
        loginFlag = login.forgotPassword(enteredCode)
    
    elif choice == 'N':
        print("Login unsuccessful! Please try again.")

    else:
        print("Invalid Choice")

# -------------------------------------------------------------------------------


# ------------------------- MENU AFTER SUCCESSFUL LOGIN -------------------------
if loginFlag == True:
    
    # Defining a File Name for passing as arguments
    fileName = "Documentation"

    # Calling the function
    printDocumentation(fileName)

    # The remaining code will go here...
    # --------------------- CUSTOMER MANAGEMENT MENU ------------------------------
    print("Do you want to manage the customers?")
    ch_Cust = input("Enter Y for yes or N for no\n")
    
    if ch_Cust == 'Y':
        print("Select the option which you want to perform:\n")
        print("\t1. Add a row into excel sheet")
        print("\t2. Delete a row in the excel sheet")
        print("\t3. Search a particular row in the excel sheet\n")
        option = int(input("Enter the index number as input\n"))

        if option == 1 or option == 2 or option == 3:
            num = int(input("Enter the number of operations you want to perform\n"))

            while num > 0:

                # Option for adding a row
                if option == 1:
                    id = input("Enter the customer ID\n")
                    name = input("Enter the customer's name\n")
                    state = input("Enter the customer's state\n")
                    address = input("Enter the address of the customer\n")
                    obj_Cust = Customer_Details(id, name, state, address)
                    obj_Cust.Customer_addRow(len(df_customer.index))
            
                # Option for deleting a row
                elif option == 2:
                    id = input("Enter the customer ID\n")
                    obj_Cust = Customer_Details(id,None,None,None)
                    df_customer = obj_Cust.Customer_deleteRow()
                
                # Option for searching a particular row in the excel sheet
                elif option == 3:
                    id = input("Enter the customer ID\n")
                    obj_Cust = Customer_Details(id,None,None,None)
                    obj_Cust.Customer_searchRow()                

                num -= 1        
        
            try:
                obj_Cust.export_Customer_data()
            except NameError:
                pass

        else:
            print("Invalid choice!")
    # -----------------------------------------------------------------------------
    
    # --------------------- EMPLOYEE MANAGEMENT MENU ------------------------------
    print("\nDo you want to manage the employees?")
    ch_Emp = input("Enter Y for yes or N for no\n")
    
    if ch_Emp == 'Y':
        print("Select the option which you want to perform:\n")
        print("\t1. Add a row into excel sheet")
        print("\t2. Delete a row in the excel sheet")
        print("\t3. Search a particular row in the excel sheet\n")
        option = int(input("Enter the index number as input\n"))

        if option == 1 or option == 2 or option == 3:
            num = int(input("Enter the number of operations you want to perform\n"))

            while num > 0:

                # Option for adding a row
                if option == 1:
                    id = input("Enter the employee ID\n")
                    name = input("Enter the employee's name\n")
                    date = input("Enter the employee's date of joining\n")
                    dept = input("Enter the department of the employee\n")
                    obj_Emp = Employee_Details(id, name, date, dept)
                    obj_Emp.Employee_addRow(len(df_employee.index))
            
                # Option for deleting a row
                elif option == 2:
                    id = input("Enter the employee ID\n")
                    obj_Emp = Employee_Details(id,None,None,None)
                    df_employee = obj_Emp.Employee_deleteRow()
                
                # Option for searching a particular row in the excel sheet
                elif option == 3:
                    id = input("Enter the employee ID\n")
                    obj_Emp = Employee_Details(id,None,None,None)
                    obj_Emp.Employee_searchRow()                

                num -= 1        
            try:
                obj_Emp.export_Employee_data()
            except NameError:
                pass

        else:
            print("Invalid Choice\n")
    # -----------------------------------------------------------------------------


    # ---------------------- PRODUCTION MANAGEMENT --------------------------------
    print("\nDo you want to manage the production?")
    ch_Prod = input("Enter Y for yes or N for no\n")
    
    if ch_Prod == 'Y':
        print("Select the option which you want to perform:\n")
        print("\t1. Add a row into excel sheet")
        print("\t2. Delete a row in the excel sheet")
        print("\t3. Search a particular row in the excel sheet\n")
        option = int(input("Enter the index number as input\n"))

        
        if option == 1 or option == 2 or option == 3:
            num = int(input("Enter the number of operations you want to perform\n"))

            while num > 0:

                # Option for adding a row
                if option == 1:
                    punitNo = int(input("Enter Production Unit Number\n"))
                    fuelOutput = int(input("Enter the fuel output\n"))
                    pcost = int(input("Enter Production Cost\n"))
                    date = input("Enter date of arrival\t")
                    obj_Prod = Production_Details(punitNo,fuelOutput,pcost,date)
                    obj_Prod.Production_addRow(len(df_production.index))
            
                # Option for deleting a row
                elif option == 2:
                    punitNo = int(input("Enter Production Unit Number\n"))
                    obj_Prod = Production_Details(punitNo,None,None,None)
                    df_production = obj_Prod.Production_deleteRow()
                
                # Option for searching a particular row in the excel sheet
                elif option == 3:
                    punitNo = int(input("Enter Production Unit Number\n"))
                    obj_Prod = Production_Details(punitNo,None,None,None)
                    obj_Prod.Production_searchRow()                

                num -= 1        

            try:
                obj_Prod.export_Production_data()
            except NameError:
                pass
        else:
            print("Invalid Choice\n")
    # -----------------------------------------------------------------------------

    # ------------------------- DEMAND MANAGEMENT ---------------------------------
    print("\nDo you want to manage the demand?")
    ch_Demand = input("Enter Y for yes or N for no\n")
    
    if ch_Demand == 'Y':
        print("Select the option which you want to perform:\n")
        print("\t1. Add a row into excel sheet")
        print("\t2. Delete a row in the excel sheet")
        print("\t3. Search a particular row in the excel sheet\n")
        option = int(input("Enter the index number as input\n"))

        if option == 1 or option == 2 or option == 3:
            num = int(input("Enter the number of operations you want to perform\n"))

            while num > 0:

                # Option for adding a row
                if option == 1:
                    order_id = random.randrange(321654987, 987654321, 7)
                    id = input("Enter customer ID\n")
                    demand = int(input('Enter Demand made by customer\n'))
                    fuel_given = int(input('Enter the Fuel given to customer\n'))
                    price = int(input('Enter Price of the oil\n'))
                    date = input('Enter Date at which customer made the demand\n')
                    transaction_id = input('Enter the Transaction ID\n')
                    transaction_status = input('Enter the Transaction Status\n')
                    obj_Demand = Demand_Details(order_id,id,demand,fuel_given,price,date,transaction_id,transaction_status)
                    obj_Demand.Demand_addRow(len(df_demand.index))

            
                # Option for deleting a row
                elif option == 2:
                    order_id = input("Enter the order ID\n")
                    obj_Demand = Demand_Details(order_id,None,None,None,None,None,None,None)
                    df_demand = obj_Demand.Demand_deleteRow()
                
                # Option for searching a particular row in the excel sheet
                elif option == 3:
                    order_id = input("Enter the order ID\n")
                    obj_Demand = Demand_Details(order_id,None,None,None,None,None,None,None)
                    obj_Demand.Demand_searchRow()               

                num -= 1        

            try:
                obj_Demand.export_Demand_data()
            except NameError:
                pass

        else:
            print("Invalid Choice\n")
    # -----------------------------------------------------------------------------


    # --------------------------- PROFIT/LOSS MENU --------------------------------
    status_Flag = True
    try:
        df_demand = pd.read_excel('demand_details.xlsx',sheet_name='Sheet1')
        df_production = pd.read_excel('production_details.xlsx', sheet_name='Sheet1')
    
    except IOError:
        status_Flag = False

    if status_Flag == False:
        print("You can't manage profit/loss section because either production_details.xlsx ")
        print("demand_details.xlsx file is missing!")

    else:

        print("\nDo you want to manage profit/loss data?")    
        ch_Prof = input("Enter Y for yes or N for no\n")
        
        
        if ch_Prof == 'Y':
            # read the excel files
            data1= pd.read_excel('production_details.xlsx')
            data2= pd.read_excel('demand_details.xlsx')

            # getting the average value of the fuel per litre
            hover = data1['Production_Cost'].sum()
            hover2 = data1['Fuel_output'].sum()

            hover3 = hover/hover2

            # creating the profit and loss section in excel file(demand_details.xlsx)
            data2['profit_section']=None
            data2['loss_section']= None

            # getting the location of the columns 
            index_fuel1 = data2.columns.get_loc('Fuel_given')
            index_demand = data2.columns.get_loc('Selling_price')
            index_profit1 = data2.columns.get_loc('profit_section')
            index_loss1 = data2.columns.get_loc('loss_section')


            # getting the loss and profit .
            # with every sale of company the below code calculates 
            # the profit and loss on the fuel using the cost of the fuel per litre (Cost/Litre)

            for row in range(0,len(data2)):
                y= data2.iat[row, index_fuel1]/data2.iat[row, index_demand]
                if y > hover3:
                    data2.iat[row , index_profit1] = (data2.iat[row, index_fuel1])*(y-hover3)
                    data2.iat[row , index_loss1] = 0
                elif y==hover3:
                    data2.iat[row , index_profit1] = 0
                    data2.iat[row , index_loss1] = 0
                else:
                    data2.iat[row , index_loss1] = (data2.iat[row, index_fuel1])*(hover3-y)
                    data2.iat[row , index_profit1] = 0

            # converting the datetime string into the standard date and time 
            # according to the excel using pandas datetime.
            data2["Date"] = pd.to_datetime(data2["Date"]).dt.strftime("%Y-%m-%d")

            data2.to_excel('ultimate_chart_excel.xlsx', sheet_name='Sheet1', index=False)

            # caluculating the all statitics of the profit and loss 
            mean_profit= data2['profit_section'].mean()
            median_profit= data2['profit_section'].median()
            max_profit= data2['profit_section'].max()
            min_profit= data2['profit_section'].min()
            mean_loss= data2['loss_section'].mean()
            median_loss= data2['loss_section'].median()
            max_loss= data2['loss_section'].max()
            min_loss= data2['loss_section'].min()

            def describe():
                print('\tThe mean profit is ', mean_profit)
                print('\tThe median profit is ',median_profit)
                print('\tThe min profit is ',min_profit)
                print('\tThe max profit is ',max_profit)
                print('\tThe mean loss is ',mean_loss)
                print('\tThe median loss is ',median_loss)
                print('\tThe max loss is ',max_loss)
                print('\tThe min loss is ',min_loss)
                
            print("The data related to profit/loss of the company is stored in ultimate_chart_excel.xlsx")
            print("\nThe statistical data of the profit/loss data is:")
            describe()



        # -----------------------------------------------------------------------------

        # --------------------------- GRAPH MENU --------------------------------------

            # getting the excel file
            data3= pd.read_excel('ultimate_chart_excel.xlsx',index_col=0,parse_dates=True)

            # getting the profit and the loss section
            profitpoint= data3['profit_section']
            losspoint= data3['loss_section']

            # sorting the dates values
            data3['Date'] = pd.to_datetime(data3['Date'])
            data3.sort_values('Date', inplace=True)

            # getting serleg as the series from the excel file
            serleg = data3['Date'] 
            
            # menu driven program for the graph display
            print("\n------Welcome to the graph store---------\n")
            print("\t A: Date vs profit")
            print("\t B: Date vs loss")
            print("\t C: Profit vs Loss")
            num = int(input("\nEnter how many graphs do you want to print\n"))

            while num > 0:
                num -= 1
                val=input("\nChoose the type of graph you want :\t")

                if val == 'A':
                    plt.plot(serleg,profitpoint,marker="o",ms=7)
                    plt.gcf().autofmt_xdate()
                    plt.title('petrol profit/loss')
                    plt.xlabel('Date')
                    plt.ylabel('profit')
                    plt.grid(axis = 'x')
                    plt.grid(axis = 'y')
                    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
                    plt.tight_layout()
                    plt.show()
                elif val == 'B':
                    plt.plot(serleg,losspoint,marker="o",ms=7)
                    plt.gcf().autofmt_xdate()
                    plt.title('petrol profit/loss')
                    plt.xlabel('Date')
                    plt.ylabel('loss')
                    plt.grid(axis = 'x')
                    plt.grid(axis = 'y')
                    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
                    plt.tight_layout()
                    plt.show()
                elif val == 'C':
                    plt.plot(profitpoint,losspoint,marker="o",ms=7)
                    plt.gcf().autofmt_xdate()
                    plt.title('petrol profit/loss')
                    plt.xlabel('profit')
                    plt.ylabel('loss')
                    plt.grid(axis = 'x')
                    plt.grid(axis = 'y')
                    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
                    plt.tight_layout()
                    plt.show()
                else:
                    print("Invalid choice!")
        

    # -----------------------------------------------------------------------------


print("\n--------- Thank you for using our project! ---------\n")
f = open("Student.txt", "r")
print(f.read())
    
    
# -------------------------------------------------------------------------------
