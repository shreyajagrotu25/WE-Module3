import math

def calculate_distance(point1, point2):
    """
    Calculate Euclidean distance between two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def nearest_neighbor(start_node, unvisited_nodes, distances):
    """
    Nearest neighbor algorithm to find the next nearest node.
    """
    min_distance = float('inf')
    nearest_node = None
    
    for node in unvisited_nodes:
        if distances[start_node][node] < min_distance:
            min_distance = distances[start_node][node]
            nearest_node = node
    
    return nearest_node

def nearest_neighbor_route(nodes, distances):
    """
    Construct a route using the nearest neighbor algorithm.
    """
    num_nodes = len(nodes)
    unvisited_nodes = set(nodes)
    route = [nodes[0]]  # Starting node
    
    unvisited_nodes.remove(nodes[0])
    
    while unvisited_nodes:
        current_node = route[-1]
        next_node = nearest_neighbor(current_node, unvisited_nodes, distances)
        route.append(next_node)
        unvisited_nodes.remove(next_node)
    
    return route

def delivery_vehicle_routing_optimization(nodes):
    """
    Solve the Delivery Vehicle Routing Optimization problem.
    """
    # Calculate distances between nodes
    num_nodes = len(nodes)
    distances = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            distances[i][j] = calculate_distance(nodes[i], nodes[j])
    
    # Construct route using nearest neighbor algorithm
    route = nearest_neighbor_route(range(num_nodes), distances)
    
    return route

def main():
    # Example data: nodes represent delivery locations (x, y coordinates)
    nodes = [(0, 0), (1, 2), (3, 1), (2, 3)]
    
    # Solve Delivery Vehicle Routing Optimization problem
    optimized_route = delivery_vehicle_routing_optimization(nodes)
    
    print("Optimized route:", optimized_route)

if __name__ == "__main__":
    main()
