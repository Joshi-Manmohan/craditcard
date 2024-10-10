# Credit Card Validator Program
sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1
card_number = input("Enter a credit card number #: ")  # Example: 6011000990139424
card_number = card_number.replace(" ", "")  
card_number = card_number[::-1]  # Reverse the card number

# Step 2
for x in card_number[::2]:  # Odd indexed digits
    sum_odd_digits += int(x)

# Step 3
for x in card_number[1::2]:  # Even indexed digits
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))  # Adding the digits of numbers 10 or more
    else:
        sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits

# Step 5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")
