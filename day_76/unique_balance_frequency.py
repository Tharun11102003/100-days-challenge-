"""
Task Name: Unique Balance Frequency Tracker
Problem Statement:
    You are given a list of account balance update queries. The objective is to determine the number of unique balances after each query. Each query updates an account_id with a new_balance. If the account already exists, its balance is updated, and the frequency of the previous balance is adjusted.The goal is to track and return the count of distinct balances after processing each query.

Steps:
    1. Input:
       ❖ A list of queries, where each query is in the form [account_id, new_balance].
       ❖ An integer limit, representing the maximum number of accounts.
    
    2. Initialization:
       ❖ Create a dictionary account_balances to store the latest balance of each account.
       ❖ Use a defaultdict(int) called balance_frequencies to track how many accounts hold each balance.
       ❖ Initialize a result list result to store the number of unique balances after each query.
    
    3. Processing Queries:
       ❖ For each query [account_id, new_balance]:
           ● If account_id exists in account_balances:
               ※ Retrieve its old_balance.
               ※ Decrease the frequency of old_balance in balance_frequencies.
               ※ If old_balance becomes zero, remove it from balance_frequencies.

           ● Update account_balances with new_balance.

           ● Increase the frequency of new_balance in balance_frequencies.

           ● Store the number of unique balances (length of balance_frequencies) in result.
    
    4. Output:
       ❖ Return the list result, where each element represents the count of unique balances after processing a query.
"""


from collections import defaultdict

class Solution(object):
    def queryResults(self, limit, queries):
        
        account_balances = {}
        balance_frequencies = defaultdict(int)
        num_queries = len(queries)
        result = [0] * num_queries

        for i in range(num_queries):
            account_id = queries[i][0]
            new_balance = queries[i][1]

            if account_id not in account_balances:
                account_balances[account_id] = new_balance
            else:
                old_balance = account_balances[account_id]
                if balance_frequencies[old_balance] == 1:
                    del balance_frequencies[old_balance]
                else:
                    balance_frequencies[old_balance] -= 1
                account_balances[account_id] = new_balance

            balance_frequencies[new_balance] += 1
            result[i] = len(balance_frequencies)

        return result


solution = Solution()
limit = 4
queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
print(solution.queryResults(limit, queries))




#============================================


