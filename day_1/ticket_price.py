"""
Day 1 Challenge: Age-Based Ticket Pricing System
Problem Statement
Create a system to determine the ticket price based on the visitor's age, the time of visit, and VIP membership status.

Pricing Rules:
Age-Based Pricing:

Children under 5 years: Free entry.

Children between 5 and 12 years: 50% discount on the base price.

Senior citizens above 60 years: 30% discount on the base price.

Everyone else: Full price.

Time of Day Discount:

If the visit is before 11:00 AM, there’s an additional 20% discount on the ticket (after the age-based discount, if applicable).

VIP Membership Discount:

If the visitor is a VIP member, they get an extra 10% discount (after applying the previous discounts).

Solution Explanation:
The system applies discounts in the following order:

Determine Age-Based Discount: Check the visitor's age and apply the appropriate discount.

Apply Time of Day Discount: If the visit is before 11:00 AM, apply a 20% discount on the ticket price.

Apply VIP Membership Discount: If the visitor is a VIP member, apply an additional 10% discount on the ticket price.

This method ensures that all relevant discounts are applied correctly to calculate the final ticket price.
"""


# Input values
age = int(input("Enter your age: "))
tprice = 1000
time = int(input("Coming time (in 24-hour format): "))
vip = input("VIP member (yes or no): ").strip().lower()

# Determine the base price after age-based discounts
if age < 5:
    final_price = 0
elif age < 12:
    final_price = tprice * 0.5
elif age >= 60:
    final_price = tprice * 0.7
else:
    final_price = tprice

# Apply time of day discount if applicable
if time < 11:
    final_price *= 0.8

# Apply VIP discount if applicable
if vip == "yes":
    final_price *= 0.9

# Output the final price
if final_price == 0:
    print("Free entry")
else:
    print(f"The final ticket price is: {final_price}")
