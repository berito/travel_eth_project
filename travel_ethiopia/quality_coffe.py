from queue import Queue,PriorityQueue
class QualityCoffe:    
    def a_star_search_with_minimax(self,graph, start, quality_coffee_depth):
        
        open_set = PriorityQueue()
        open_set.put((0, start))  # Tuple: (total_cost, city)
       
        came_from = {}  # Dictionary to store the parent of each city
        cost_so_far = {start: 0}  # Dictionary to store the cost to reach each city

        while not open_set.empty():
            _, current_city = open_set.get()
            print(f"Exploring {current_city.get_city_name()}")
            if current_city.get_coffee_quality() is not None:
                # Reconstruct the path
                path = reconstruct_path(came_from, start, current_city)
                print(f"Found leaf node with coffee quality: {current_city.get_city_name()} - Path: {path}")
                return path, current_city  # Return the path and the leaf node with the highest coffee quality

            for neighbor in graph.get_neighbors(current_city):
                new_cost = cost_so_far[current_city] + 1  # Assuming unit distance
                if neighbor[0] not in cost_so_far or new_cost < cost_so_far[neighbor[0]]:
                    cost_so_far[neighbor[0]] = new_cost
                    priority = new_cost + heuristic(neighbor[0], start, graph)  # Updated heuristic
                   
                    open_set.put((priority, neighbor[0]))
                    came_from[neighbor[0]] = current_city
            
        # If no leaf node with coffee quality is reached, perform minimax to find the best move
       
        best_move = max(graph.get_neighbors(start), key=lambda neighbor: graph.minimax_decision(neighbor, quality_coffee_depth, maximizing_player=True))
        print(f"No leaf node found. Performing minimax on neighbors of {start.get_city_name()}")
        print(f"Best move according to minimax: {best_move[0].get_city_name()}")

        path, _ = self.a_star_search_with_minimax(graph, start, quality_coffee_depth - 1)
        return path, best_move[0]  # Return the path and the best move

def heuristic(city,start, graph):
    # Updated heuristic to include coffee quality as part of the cost
    coffee_quality = graph.get_coffee_quality(city)
    return coffee_quality if coffee_quality is not None else 0
def reconstruct_path(came_from, start, goal):
    current_city = goal
    path = []
    print(path)
    while current_city != start:
        path.insert(0, current_city)  # Insert at the beginning to maintain the correct order
        current_city = came_from[current_city]
    path.insert(0, start)
    arrow_path = " -> ".join(str(city.get_city_name()) for city in path)
    return arrow_path
    