"""
Task: Best Time to Buy and Sell Stock 
    1.Input:
       ❖ Start with a list of stock prices for a specific number of days. Let's call this list prices.

    2.Algorithm:
       ❖ Set an initial buying price as the price on the first day.
       ❖ Set an initial profit amount to zero.
       ❖ Loop through the prices from the second day onward to update the buying price and profit based on the current day's price.

    3.Steps in the Process:
       ❖ Initialize:
           ● Begin with the given list of stock prices.
           ● Set the initial buying price to the price on the first day.
           ● Initialize the profit to zero.

       ❖ Loop:
           ● For each day, starting from the second day:
               ⁕ Check if the current day's price is less than the current buying price. If it is, update the buying price to this new, lower price.
               ⁕ If the current buying price is less than the current day's price, calculate the profit by subtracting the buying price from the current day's price, add this profit to the total profit, and then update the buying price to the current day's price.

    4.Output:
       ❖ After going through all the days' prices, the total profit is printed.
"""


prices = [7,1,5,3,6,4]
buy = prices[0] 
profit = 0 
for i in range(1,len(prices)):
    if prices[i] < buy:
        buy = prices[i]
    elif buy < prices[i]:
        profit += prices[i] - buy
        buy = prices[i]
print(f"Profit = {profit}")