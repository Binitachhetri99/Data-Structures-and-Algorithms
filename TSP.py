import random
import math
from itertools import permutations
import time

class GraphGenerator:
    def __init__(self, num_nodes, spatial=True):
        self.num_nodes = num_nodes
        self.spatial = spatial
        self.node_positions = {}

    def generate_graph(self):
        if self.spatial:
            self.node_positions = {i: (random.randint(0, 100), random.randint(0, 100)) for i in range(self.num_nodes)}

        graph = {}
        for i in range(self.num_nodes):
            graph[i] = {}
            for j in range(i + 1, self.num_nodes):
                distance = self.calculate_distance(i, j)
                graph[i, j] = distance
                graph[j, i] = distance
        return graph

    def calculate_distance(self, node1, node2):
        """Calculate Euclidean distance between two nodes (cities)"""
        x1, y1 = self.node_positions[node1]
        x2, y2 = self.node_positions[node2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class BruteForce:
    def __init__(self, graph, num_nodes):
        self.graph = graph
        self.num_nodes = num_nodes

    def find_shortest_path(self):
        nodes = list(range(self.num_nodes))
        shortest_path = None
        min_distance = float('inf')

        for i in permutations(nodes[1:]):
            current_path = (0,) + i + (0,)
            current_distance = self.calculate_total_distance(current_path)

            if current_distance < min_distance:
                min_distance = current_distance
                shortest_path = current_path

        return shortest_path, min_distance

    def calculate_total_distance(self, path):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += self.graph[(path[i], path[i + 1])]
        return total_distance

class AntColonyOptimizer:
    def __init__(self, graph, num_nodes, num_ants, num_iterations, alpha, beta, evaporation_rate):
        self.graph = graph
        self.num_nodes = num_nodes
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.pheromones = {edge: 1.0 for edge in graph}

    def run(self):
        best_path = None
        best_cost = float('inf')
    

        for i in range(self.num_iterations):
            all_paths = []
            for _ in range(self.num_ants):
                path = self._construct_path()
                cost = self._calculate_cost(path)
                #euclidean_cost = self._calculate_euclidean_cost(path)  # Calculate Euclidean cost
                all_paths.append((path, cost))
                if cost < best_cost:
                    best_cost = cost
                    best_path = path

            self._update_pheromones(all_paths)

        return best_path, best_cost

    def _construct_path(self):
        start_node = random.randint(0, self.num_nodes - 1)
        path = [start_node]
        visited = set(path)

        while len(path) < self.num_nodes:
            next_node = self._select_next_node(path[-1], visited)
            if next_node is not None:
                path.append(next_node)
                visited.add(next_node)
            else:
                break

        return path

    def _select_next_node(self, current_node, visited):
        probabilities = []
        total_pheromone = 0.0

        for next_node in range(self.num_nodes):
            if next_node not in visited:
                pheromone = self.pheromones.get((current_node, next_node), 0) ** self.alpha
                distance = self.graph.get((current_node, next_node), float('inf'))
                probability = pheromone / (distance ** self.beta) if distance > 0 else 0
                probabilities.append((next_node, probability))
                total_pheromone += probability

        if total_pheromone > 0:
            probabilities = [(node, prob / total_pheromone) for node, prob in probabilities]

        return self._weighted_random_choice(probabilities)

    def _weighted_random_choice(self, probabilities):
        r = random.random()
        cumulative_probability = 0.0
        for node, prob in probabilities:
            cumulative_probability += prob
            if r <= cumulative_probability:
                return node
        return None

    def _calculate_cost(self, path):
        total_cost = 0
        for i in range(len(path)):
            next_index = (i + 1) % len(path)
            edge = (path[i], path[next_index])
            total_cost += self.graph.get(edge, float('inf'))
        return total_cost



    def _update_pheromones(self, all_paths):
        for edge in self.pheromones:
            self.pheromones[edge] *= (1 - self.evaporation_rate)

        for path, cost in all_paths:
            if cost > 0:
                pheromone_delta = 1.0 / cost
                for i in range(len(path)):
                    next_index = (i + 1) % len(path)
                    edge = (path[i], path[next_index])
                    self.pheromones[edge] += pheromone_delta

# Example usage - Comparision of two algorithms on same graph 
num_nodes = 10
num_ants = 5
num_iterations = 50
alpha = 1.0
beta = 2.0
evaporation_rate = 0.1

generator = GraphGenerator(num_nodes, spatial=True)
graph = generator.generate_graph()

# Ant Colony Optimization
time1 = time.perf_counter()
optimizer = AntColonyOptimizer(graph, num_nodes, num_ants, num_iterations, alpha, beta, evaporation_rate)
best_path, best_cost = optimizer.run()
time2 = time.perf_counter()
time_difference = time2-time1
print(f"Best Path (ACO): {best_path}")
print(f"Best Cost (ACO): {best_cost}")
print(f"Time taken: {time_difference}")


# Brute Force TSP
time1 = time.perf_counter()
tsp_solver = BruteForce(graph, num_nodes)
shortest_path, min_distance = tsp_solver.find_shortest_path()
time2 = time.perf_counter()
time_difference = time2-time2
print(graph)
print(f"Shortest path (Brute Force): {shortest_path}")
print(f"Minimum distance (Brute Force): {min_distance:.2f}")
print(f"Time taken: {time_difference}")
# Example usage:

#testing Ant colony optimization on 30 nodes
num_nodes = 30
num_ants = 10
num_iterations = 70
alpha = 2.0
beta = 3.0
evaporation_rate = 0.15

generator = GraphGenerator(num_nodes, spatial=True)
graph = generator.generate_graph()


time1 = time.perf_counter()
optimizer = AntColonyOptimizer(graph, num_nodes, num_ants, num_iterations, alpha, beta, evaporation_rate)
best_path, best_cost = optimizer.run()
time2 = time.perf_counter()
time_difference = time2-time1
print(f"Best Path (ACO): {best_path}")
print(f"Best Cost (ACO): {best_cost}")
print(f"Time taken: {time_difference}")
