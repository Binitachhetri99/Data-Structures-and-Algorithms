import random 
def genrate_item(num_items, max_value, max_weight = 50):
    """ Generate a list of items with random weights and values"""
    items = []
    for i in range(num_items):
        value = random.randint(1, max_value)
        weight = random.randint(1, max_weight)
        items.append((value, weight))
    return items

# greedy algorithm case 1: high value to weight ratio
def greedy_case1(array, max_weight):
    # in an array that has a valueweight tuple in it, we loop around the array and pick and add pair to a list if the pair has highest ratio
    #print(array)
    sorted_items = sorted(array, key = lambda item: item[0]/item[1], reverse = True)

    bucket = []
    total_weight = 0
    total_value = 0
    for value, weight in sorted_items:
        ratio = value/weight
        #max_ratio = 0
        if total_weight+weight <= max_weight:
            
            bucket.append((value,weight, ratio))
            total_weight += weight
            total_value += value

    return bucket, total_value
    
#case2 : maximizing value alone 
def greedy_case2(array, max_weight):
    sorted_items = sorted(array, key = lambda item: item[0], reverse = True)

    bucket = []
    total_weight = 0
    total_value = 0
    for value, weight in sorted_items:
        
        if total_weight+weight <= max_weight:
            
            bucket.append((value,weight))
            total_weight += weight
            total_value += value
    return bucket, total_value

#case3 : minimizing weight alone 
def greedy_case3(array, max_weight):
    sorted_items = sorted(array, key = lambda item: item[1], reverse = False)

    bucket = []
    total_weight = 0
    total_value = 0
    for value, weight in sorted_items:
        
        if total_weight+weight <= max_weight:
            
            bucket.append((value,weight))
            total_weight += weight
            total_value += value
    return bucket, total_value

# using dynamic programming 
import random

def knapsack_dp(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Populating the DP table
    for i in range(1, n + 1):
        value, weight = items[i - 1]  
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]
    
    included_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]: 
            included_items.append(items[i - 1])
            w -= items[i - 1][1]  
    
    max_value = dp[n][capacity]
    return included_items, max_value

# Test cases
import time
#test 1: with 10 items and weight capacity 50
print(" Test case1: with 10 items and weight capacity 50")
test = genrate_item(10, 50)
#print("the list is: ", test)

time1 = time.perf_counter()
result1 = greedy_case1(test, 50)
time2 = time.perf_counter()
time_diff1 = time2-time1
result2 = greedy_case2(test, 50)
result3 = greedy_case3(test, 50)

time1 = time.perf_counter()
result4= knapsack_dp(test, 50)
time2 = time.perf_counter()
time_diff2 = time2-time1
print("maximizing value-weight ratio", result1, "time taken:", time_diff1)
print("maximizing value alone",result2)
print("minimizing weight alone",result3)
print("Dynamic Programming",result4, "time taken: ", time_diff2 )



#test 2: with 50 items and weight capacity 100
print(" Test case 2: with 50 items and weight capacity 100")
test = genrate_item(50, 50)
#print(test)

time1 = time.perf_counter()
result1 = greedy_case1(test, 100)
time2 = time.perf_counter()
time_diff1 = time2-time1

result2 = greedy_case2(test, 100)
result3 = greedy_case3(test, 100)

time1 = time.perf_counter()
result4= knapsack_dp(test, 100)
time2 = time.perf_counter()
time_diff2 = time2-time1
print("maximizing value-weight ratio", result1, "time taken for greedy algorithm to run:", time_diff1)
print("maximizing value alone",result2)
print("minimizing weight alone",result3)
print("Dynamic Programming",result4, "time taken for dynamic programming to run: ", time_diff2 )


#test 3: with 100 items and weight capacity 200
print(" Test case 3: with 100 items and weight capacity 200")
test = genrate_item(100, 50)
#print(test)

time1 = time.perf_counter()
result1 = greedy_case1(test, 200)
time2 = time.perf_counter()
time_diff1 = time2-time1

result2 = greedy_case2(test, 200)
result3 = greedy_case3(test, 200)

time1 = time.perf_counter()
result4= knapsack_dp(test, 200)
time2 = time.perf_counter()
time_diff2 = time2-time1
print("maximizing value-weight ratio", result1, "time taken for greedy algorithm to run:", time_diff1)
print("maximizing value alone",result2)
print("minimizing weight alone",result3)
print("Dynamic Programming",result4, "time taken for dynamic programming to run: ", time_diff2 )
