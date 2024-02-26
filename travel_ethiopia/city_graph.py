from queue import Queue
from collections import defaultdict
class City:
    def __init__(self, city_name, heuristic_cost=None):
        if  heuristic_cost is None:
            self.city_name = city_name
            self.heuristic_cost=1
        else:
            self.city_name = city_name
            # default values
            self.heuristic_cost=int(heuristic_cost)
    def get_city_name(self):
        return self.city_name
    def get_heuristic(self):
        return self.heuristic_cost
    def __lt__(self, other):
        # Compare cities based on heuristic values
        return self.get_heuristic() < other.get_heuristic()
    def __hash__(self):
        return hash(self.city_name)
    def __str__(self):
        return f"{self.city_name}, Heuristic: {self.heuristic_cost}"
class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
class CityPoint:
    def __init__(self, city_name, point):
        self.city_name=city_name
        self.point=point
    def get_city_name(self):
        return self.city_name
    def __str__(self):
        return f"{self.city_name}, pont: ({self.x},{self.y})"

class CityAdversary:
    def __init__(self, city_name,coffee_quality=None):
        self.city_name=city_name
        self.coffee_quality=coffee_quality
    def get_city_name(self):
        return self.city_name
    def get_coffee_quality(self):
        return self.coffee_quality
    def degrade_coffee_quality(self, amount):
        if self.coffee_quality is not None:
            self.coffee_quality -= amount
    def __lt__(self, other):
        
        my_quality = self.get_coffee_quality()
        other_quality = other.get_coffee_quality()
        if my_quality is not None and other_quality is not None:
            return my_quality < other_quality
        elif my_quality is None and other_quality is not None:
            return True  # None is considered less than any non-None value
        elif my_quality is not None and other_quality is None:
            return False  # Any non-None value is considered greater than None
        elif my_quality is None and other_quality is None:
            return 0
        else:
            return NotImplemented
    def __str__(self):
        return f"{self.city_name} (Quality: {self.coffee_quality})"
    
class CityGraph:
    def __init__(self):
        self.graph = {}

    def add_city(self, city):
        if city not in self.graph:
            self.graph[city] = []
   
    def add_distance(self, source, destination, distance=None):
        self.add_city(source)
        self.add_city(destination)
        if distance is not None:
            # Assuming distances are bidirectional
            self.graph[source].append((destination, distance))
            self.graph[destination].append((source, distance))
        else:
          self.graph[source].append((destination,None))
          self.graph[destination].append((source,None))  

    def get_neighbors(self, city):
        return self.graph.get(city, [])
    
    def degrade_coffee_quality(self, source, destination):
        # Degrade coffee quality between source and destination (for simplicity, degrade by 1)
        if source.get_coffee_quality() is not None:
            # degrades coffe quality by one 
            destination.degrade_coffee_quality(1)
    
    def get_coffee_quality(self, city):
        # Return the coffee quality of the city (None for non-leaf nodes)
        return city.get_coffee_quality()
   
    def minimax_decision(self, city, depth, maximizing_player):
        if depth == 0 or city.get_coffee_quality() is not None:
            return city.get_coffee_quality() if city.get_coffee_quality() is not None else 0

        if maximizing_player:
            max_eval = float('-inf')
            for child_state in self.get_neighbors(city):
                eval_score = self.minimax_decision(child_state, depth - 1, False)
                max_eval = max(max_eval, eval_score)
            return max_eval
        else:
            min_eval = float('inf')
            for child_state in self.get_neighbors(city):
                eval_score = self.minimax_decision(child_state, depth - 1, True)
                min_eval = min(min_eval, eval_score)
            return min_eval
    
    def __str__(self):
        result = []
        for city, neighbors in self.graph.items():
            neighbor_str = ', '.join([f"{neighbor[0].city_name} ({neighbor[1]})" for neighbor in neighbors])
            result.append(f"{city.city_name} -> Neighbors: {neighbor_str}")
        return '\n'.join(result)

