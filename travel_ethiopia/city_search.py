from queue import Queue,PriorityQueue
from collections import defaultdict
class CitySearch:
    # breadth first search
    @staticmethod
    def bfs_shortest_path(graph, start_city, goal_city):
        visited = set()
        queue = Queue()
        queue.put((start_city, [start_city]))

        while not queue.empty():
            current_city, path = queue.get()

            if current_city == goal_city:
                return path

            visited.add(current_city)

            for neighbor, _ in graph.get_neighbors(current_city):
                if neighbor not in visited:
                    queue.put((neighbor, path + [neighbor]))

        return None  # If no path is found
    # depth first search
    @staticmethod
    def dfs_shortest_path(graph, start_city, goal_city):
        visited = set()
        stack = [(start_city, [start_city])]

        while stack:
            current_city, path = stack.pop()

            if current_city.get_city_name() == goal_city.get_city_name():
                return path

            visited.add(current_city.get_city_name())

            for neighbor, _ in graph.get_neighbors(current_city):
                neighbor_name = neighbor.get_city_name()
                if neighbor_name not in visited:
                    stack.append((neighbor, path + [neighbor]))

        return None
    # uniform cost search ,single source single destination(sssd)
    @staticmethod
    def ucs_sssd(self, start_city, goal_city):
        visited = set()
        priority_queue = PriorityQueue()
        priority_queue.put((0, [start_city]))

        while not priority_queue.empty():
            current_cost, current_path = priority_queue.get()
            current_node = current_path[-1]

            if current_node == goal_city:
                return current_path
            if current_node in visited:
                continue  # Skip exploring this node if it has been visited
            visited.add(current_node)
            
            for neighbor, cost in self.graph.get(current_node, []):
                new_cost = current_cost + cost
                new_path = current_path + [neighbor]
                priority_queue.put((new_cost, new_path))

        return None
    # uniform cost search ,single source multiple destination(sssd)
    @staticmethod
    def ucs_ssmd(self, start_city, goal_cities):
        visited = set()
        priority_queue = PriorityQueue()
        priority_queue.put((0, [start_city]))

        while not priority_queue.empty():
            current_cost, current_path = priority_queue.get()
            current_node = current_path[-1]
            print([city.get_city_name() for city in current_path],current_cost)
            # print("Current Path:", [city.get_city_name() for city in current_path])
            # print("Visited Cities:", [city.get_city_name() for city in visited])
            # print("Goal Cities Remaining:", [city.get_city_name() for city in goal_cities])

            if current_node in goal_cities:
                goal_cities.remove(current_node)
                if not goal_cities:
                    return current_path  # All goals reached
            if current_node in visited:
                continue  # Skip exploring this node if it has been visited
            visited.add(current_node)
           
            for neighbor, cost in self.graph.get(current_node, []):
                print(cost)
                new_cost = current_cost + cost
                new_path = current_path + [neighbor]
                priority_queue.put((new_cost, new_path))

        return None
    # a star search A*
    @staticmethod
    def astar_search(graph, start_city, goal_city):
        open_set = PriorityQueue()
        closed_set = set()
        open_set.put((0 + start_city.get_heuristic(), 0, start_city, None))
        while not open_set.empty():
            _, current_cost, current_city, parent = open_set.get()
            if current_city == goal_city:
                path = []
                while parent:
                    path.insert(0, parent[2])
                    parent = parent[3]
                path.insert(0, start_city)  # Insert the start_city at the beginning
                return path

            closed_set.add(current_city)

            for neighbor, distance in graph.get_neighbors(current_city):
                if neighbor not in closed_set:
                    heuristic_cost = distance + current_cost + neighbor.get_heuristic()
                    open_set.put((heuristic_cost, distance + current_cost, neighbor, (current_cost, current_city, neighbor, parent)))

        return None
   