KNAPSACK PROBLEM USING GREEDY APPROACH AND DYNAMIC PRORAMMING APPROACH:
0/1 Knapsack problem is a problem where we must choose items from a given set of items with value and a weight for each item and store them in a knapsack that has a weight capacity, in a way that the chosen items result in the maximum total value. 0/1 signifies that we either choose an item or don’t, meaning we cannot choose a fraction of an item. Its significance in optimization is that it relates to the real-world practical problems where choices must be made considering the constraints while maximizing the gain/output. 
 • A discussion of the strengths and weaknesses of each approach (Greedy and Dynamic Programming). 
The strength of greedy programming is that it is easy to implement, logic is simple, and the run time is O(n log n) given that we use pythons sort function to sort the list of items which is O(n log n) and the iteration is O(n). The weakness is that it does not guarantee an optimal solution and is not suitable for complex problems with their limited flexibility.
The strength of dynamic programming is that it guarantees an optimal solution and is suitable for complex problems as well. The weakness is that the design and implementation is difficult compared to greedy algorithms. Time and space complexity are also high. Time complexity is O(nW) where n is number of items and W is maximum capacity of the knapsack. 
• A comparison of the performance of each algorithm based on your test cases, including solution quality and execution time. 
When testing greedy the algorithms in various cases such as different number if items and different weight capacities, Dynamic programming always gave the optimal solution and automatically highest total value compared to all the cases of greedy algorithm whether it was high value-weight ratio, high value only, or low weight only, which proves that when it comes to optimality Dynamic programming is the way to go. And in terms of run time calculation, greedy algorithm always took less time than Dynamic programming but as expected did not provide optimal solution with one or two exception cases where it did give optimal solution. 
Exmple :
Test case1: with 10 items and weight capacity 50
maximizing value-weight ratio ([(48, 6, 8.0), (31, 4, 7.75), (40, 9, 4.444444444444445), (44, 14, 3.142857142857143)], 163) time taken: 1.699995482340455e-05
maximizing value alone ([(48, 6), (46, 18), (44, 14), (40, 9)], 178)
minimizing weight alone ([(31, 4), (48, 6), (40, 9), (44, 14)], 163)
Dynamic Programming ([(48, 6), (40, 9), (44, 14), (46, 18)], 178) , time taken: 0.00010439998004585505

If optimality is crucial, I would recommend Dynamic programming since it guarantees optimal solution even though it is time and resource intensive and when speed is more important Greedy algorithm is appropriate. 

TRAVELING SALESMAN PROBLEM USING ANT COLONY OPTIMIZATION APPROACH:
Traveling salesman problem (TSP) is a problem where a salesman must visit the cities exactly once and return to its original city in a way that the route he takes is the best route in terms of cost/distance. In other words, given the places, find the shortest possible route while visiting each city exactly once. 
While this sounds easy to solve, reality is different. TSP is an NP-hard problem where NP stands for Nondeterministic Polynomial, as it is computationally difficult to solve. Finding the optimal solution is difficult as the number of cities grows, the run time grows exponentially, but given the solution to TSP, verifying if the solution is optimal can be done efficiently in polynomial time. 
Brute force algorithm in simple term is a solution to TSP where all possible ways of visiting each city exactly once then returning to the starting city is explored then after computing and comparing the distance/cost for each route, it returns the best route (minimum distance/cost). While this algorithm is easy to implement, it is not efficient since every permutation of the cities needs to be explored, and the number of permutations grows factorially with the number of cities. This results in runtime of O(n-1)!. Hence, this algorithm is not practical.
Ant colony optimization (ACO) is a heuristic algorithm to solve TSP, where the concept is inspired by ant’s nature of releasing pheromones while heading towards their food source. As the pheromones concentration gets stronger in the shorter path over time, all the ants are attracted to that shorter path which converge toward an optimal or near-optimal path.
Why I chose this algorithm is because it was easier for me to visualize the concept since it relates to nature, and ACO works mathematically, and the concept being like machine learning where the algorithm converges over multiple iterations to find the best or optimal solution. Plus the time complexity is O(t.a.n^2) where t is number of iterations, a is number of ants, and n is number of nodes. 
Ther important mechanism of ACO is Ants decision rule that combines the “pheromone level” deposited by ants which gets updated after each iteration, using evaporation rate to avoid over accumulation for a given edge and “heuristic information” and the parameters that control their rate to overall provide the probabilistic value that an ant will travel that edge.
After implementing both Brute Force and Ant colony optimization in same graph with 12 nodes, I got the run time of 0.0 seconds for both, and the quality was same in the sense that the path they generated gave similar cost/distance or sometimes brute force giving the best and ACO providing the near optimal solution. But for anything above 12 nodes, Brute force stopped giving output or at least does not give output within a reasonable time that I can wait. This proves that for lesser number of nodes, the time and quality are approximately similar for both, but ACO performs better as the number of nodes increases. 
Output on same graph: 
Best Path (ACO): [6, 4, 8, 2, 9, 3, 1, 5, 0, 7]
Best Cost (ACO): 294.36897120931394
Time taken: 0.016042100003687665
Shortest path (Brute Force): (0, 5, 1, 7, 3, 9, 2, 8, 4, 6, 0)
Minimum distance (Brute Force): 290.77
Time taken: 0.0

Upon implementing ACO on 30 nodes with adjusted parameters to balance exploration and exploitation, given that higher evaporation rate allows more exploration and higher pheromone level allows more exploitation and vice versa.
Output:
Best Path (ACO): [12, 22, 0, 19, 10, 29, 13, 18, 25, 26, 21, 2, 8, 24, 4, 5, 1, 23, 7, 9, 28, 6, 27, 16, 11, 3, 14, 20, 17, 15]
Best Cost (ACO): 481.6927698320381
Time taken: 0.4568547000089893
Implementing ACO on various number of nodes and multiple attempts and getting consistent results with little variations in cost shows that the algorithm has a better quality.
