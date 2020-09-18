purchase = 0
state_sales_tax = 0
county_sales_tax = 0
total_sales_tax = 0
print('Enter the amount of the purchase')
purchase = float(input())
state_sales_tax = (purchase*5)/100
county_sales_tax = (purchase*2.5)/100
total_sales_tax = state_sales_tax + county_sales_tax
print('The amount of the purchase: ', purchase)
print('The state sales tax: ', state_sales_tax)
print('The county sales tax: ', county_sales_tax)
print('The total sales tax: ', total_sales_tax)
print('The total of the sale: ', purchase + total_sales_tax)

