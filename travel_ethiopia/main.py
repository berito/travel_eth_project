from city_file_reader import CityFileReader
from city_graph import CityGraph
from city_search import CitySearch
from quality_coffe import QualityCoffe
from user_input import UserInput

question_dic={
    'q1':'data/figure1.txt',
    'q2':'data/figure2.txt',
    'q3':'data/figure3.txt',
    'q4':'data/figure4.txt',   
}
city_graph = CityGraph()

def question1():
    # Get user input for start and goal cities
    start_city_name, goal_city_name = UserInput.get_user_input()

    # Ensure the provided cities exist in the graph
    if start_city_name not in cities_dict or goal_city_name not in cities_dict:
        print("Invalid city names. Please provide valid city names.")
    else:
        start_city = cities_dict[start_city_name]
        goal_city = cities_dict[goal_city_name]
        algorithm=UserInput.get_search_strategy_input()
        if algorithm not in ['bfs','dfs']:
            print("Invalid algorithm names. Please provide either bfs or dfs.")
        else:
            if algorithm=='bfs':
                bfs_path=CitySearch.bfs_shortest_path(city_graph,start_city,goal_city)
                if bfs_path is not None:
                    path_strings = [city.get_city_name() for city in bfs_path]
                    print("BFS Shortest Path:", ' -> '.join(path_strings))
                else:
                    print("No path found.")
            else:
                dfs_path=CitySearch.dfs_shortest_path(city_graph,start_city,goal_city)
                if dfs_path is not None:
                    path_strings = [city.get_city_name() for city in dfs_path]
                    print("DFS Shortest Path:", ' -> '.join(path_strings))
                else:
                    print("No path found.")

def question2():
    # Get user input for start and goal cities
    sub,start_city_name, goal_city_name = UserInput.get_question_sub()
    if sub=='2':
        cities = ['Axsum', 'Gonder', 'Lalibela', 'Babile', 'Jimma', 'Bale', 'Softoumer', 'Arbaminch']
        start_city = cities_dict['AddisAbaba']
        goal_cities = {cities_dict[city_name] for city_name in cities}
        ucs_path=CitySearch.ucs_ssmd(city_graph,start_city,goal_cities.copy())
        if ucs_path is not None:
                    path_strings = [city.get_city_name() for city in ucs_path]
                    print('single source multiple destination')
                    print("UCS Shortest Path:", ' -> '.join(path_strings))
        else:
            print("No path found.")
    elif sub=='1':
             start_city=cities_dict[start_city_name]
             goal_city=cities_dict[goal_city_name]
             ucs_path=CitySearch.ucs_sssd(city_graph,start_city,goal_city)
             if ucs_path is not None:
                    path_strings = [city.get_city_name() for city in ucs_path]
                    print('single source single destination')
                    print("UCS Shortest Path:", ' -> '.join(path_strings))
             else:
                    print("No path found.")
def question3():
    # Get user input for start and goal cities
    start_city_name, goal_city_name = UserInput.get_question3_input()

    # Ensure the provided cities exist in the graph
    if start_city_name not in cities_dict or goal_city_name not in cities_dict:
        print("Invalid city names. Please provide valid city names.")
    else:
        start_city = cities_dict[start_city_name]
        goal_city = cities_dict[goal_city_name]
        astar_path=CitySearch.astar_search(city_graph,start_city,goal_city)
        if astar_path is not None:
            path_strings = [city.get_city_name() for city in astar_path]
            print("A* search Shortest Path:", ' -> '.join(path_strings))  
        else:
            print("No path found.")
         

def question4():
     # Get user input for start and goal cities
    print('get quality coffe initial city Addis Ababa')
    start_city_name="AddisAbaba"
    start_city = cities_dict[start_city_name]
    quality_coffee_depth = 0
    quality_coffe=QualityCoffe()
    path, best_move = quality_coffe.a_star_search_with_minimax(city_graph, start_city, quality_coffee_depth)
    print(path)
    print(best_move)
    # print("Full Path:", [city.get_city_name() for city in path])
    # print("Best Move:", best_move.get_city_name())


select_question=UserInput.get_question_no_input()
if select_question not in question_dic.keys():
     print("Invalid question number. Please provide valid question number.")
else:
    # Read cities and distances from file
    cities_dict = CityFileReader.read_cities_and_distances(select_question,question_dic[select_question], city_graph)
    if select_question=='q1':
        # bfs and dfs
        question1()
    elif select_question=='q2':
         # uniform cost search
        # 2.2  addis ababa to lalibela
        question2()
    elif select_question=='q3':
        # A* search
        # addis abeba to moyale
        question3()
    else:
        # Adversary (minimax)
        question4() 
      
   
