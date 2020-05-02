#This program generate a compound interest table for principal amount and annual interest rate
#
#Author: Seyi Idowu
#        30-Jan-2020
#
#Description: this python program will generate a compound interest
#
#user input values for initial investment principal,interest rate,and years of investment

principal = float(input("Enter the amount you initially invested: "))
annual_rate = float(input("Enter the annual interest rate (in percent): "))
years_of_investment = int(input("how many years will this investment be for: "))

print ("year        Balance($)") # print strings for table header

# calculate the new principal for every year of investment and print the outputs in a table format

for i in range(0,years_of_investment,1):
    if (i < years_of_investment):
            principal = principal * (1 + (annual_rate / 100))
            year = (i + 1)
            
    print( "{:}           {:,.2f}".format(year,principal))
