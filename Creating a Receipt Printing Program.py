"""
Creating a Receipt Printing Program
"""
# create a product and price for three items
p1_name, p1_price = "Books", 49.00
p2_name, p2_price = "Computer", 499.00
p3_name, p3_price = "Mointor", 125.00

# create a company name and information
company_name = "The Book Shop"
company_address = "402 Park Road"
company_city = "Bangalore, KA"

# declare ending message
message =  "Thanks for shopping with us today!"

# create a top border
print("*" * 70)

# print company information first, using format
print(f"\t\t{company_name.title( )}")
print(f"\t\t{company_address}")
print(f"\t\t{company_city}")

# print a line between sections
print( "=" * 70 )

# print out header for section of items
print("\tProduct Name \tProduct Price")

# create a print statement for each product
print(f"\t{p1_name}\t\t{p1_price}")
print(f"\t{p2_name}\t{p2_price}")
print(f"\t{p3_name}\t\t{p3_price}")

# print a line between sections
print('=' * 70)

# print out header for section of total
print("\t\t\tTotal")

# calculate total price and print out
total = p1_price + p2_price + p3_price
print(f"\t\t\t{total}")

# print a line between sections
print('=' * 70)

# output thank you message
print(f"\n\t{message}\n")

# create a bottom border
print("*" * 70)