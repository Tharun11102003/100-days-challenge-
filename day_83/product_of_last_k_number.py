"""
✿ Task: Product of the Last K Numbers

❖ Problem Statement: You have a class ProductOfNumbers that can perform two main operations: adding a number to an internal list and retrieving the product of the last k numbers added to that list. The objective is to design this class to handle these operations efficiently.

★ Steps:
    1.Initialization: 
        ❖ You will initialize an instance of the class ProductOfNumbers. 
        ❖ Define two attributes within the class: ※ prefix_products: A list to store cumulative products of all added numbers. 
            ※ current_product: A variable to maintain the ongoing product of numbers.

    2.Add Operation: 
        ❖ Define a method add that takes an integer num as input. 
            ※ Handling Zero: 
                ● If the number added is zero, reset both prefix_products and current_product. 
            ※ Handling Non-Zero: 
                ● Multiply current_product by the added number. 
                ● Append this updated current_product to prefix_products.

    3.Product Retrieval: 
        ❖ Define a method getProduct that takes an integer k as input. 
            ※ Case When Less Than K Numbers are Present: 
                ● If the length of prefix_products is less than k, return 0. 
            ※ Case When Exactly K Numbers are Present: 
                ● If the length of prefix_products is exactly k, return the last product in the list. 
            ※ Case When More Than K Numbers are Present: 
                ● Retrieve the product of the last k numbers by dividing the last product by the product k positions back in prefix_products.

    4.Command Execution: 
        ❖ Create an instance of the ProductOfNumbers class. 
        ❖ Execute a list of commands (add, getProduct) and store results accordingly.

    5.Output: ❖ After processing all commands, print the outputs list, which will contain the results of the getProduct method calls and None for the add method calls
"""

class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [] 
        self.current_product = 1  

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = []  
            self.current_product = 1
        else:
            self.current_product *= num
            self.prefix_products.append(self.current_product)

    def getProduct(self, k: int) -> int:
        if len(self.prefix_products) < k:
            return 0  
        if len(self.prefix_products) == k:
            return self.prefix_products[-1] 
        return self.prefix_products[-1] // self.prefix_products[-k - 1]
    
commands = ["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add", "getProduct"]
inputs = [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]

product_obj = None
outputs = []
for command, value in zip(commands, inputs):
    if command == "ProductOfNumbers":
        product_obj = ProductOfNumbers()
        outputs.append(None)
    elif command == "add":
        product_obj.add(value[0])
        outputs.append(None)
    elif command == "getProduct":
        result = product_obj.getProduct(value[0])
        outputs.append(result)

print("Output:", outputs)






#==============================


