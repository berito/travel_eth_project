from city_graph import City,CityAdversary
class CityFileReader:
    @staticmethod
    def read_cities_and_distances(q,file_path, city_graph):
        cities = {}
        with open(file_path, 'r') as file:
             if q=='q1':
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts)==1:
                        city_name = parts[0]
                        cities[city_name] = City(city_name)  
                    elif len(parts) == 2:
                        source, destination = parts[0], parts[1]
                        city_graph.add_distance(cities[source], cities[destination])
             if q=='q2':
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts)==1:
                        city_name = parts[0]
                        cities[city_name] = City(city_name)  
                    elif len(parts) == 3:
                        source, destination,distance = parts[0], parts[1],parts[2]
                       #print(cities[source],cities[destination],int(distance))
                        city_graph.add_distance(cities[source], cities[destination],int(distance))
             if q=='q3':
                  for line in file:
                    parts = line.strip().split(',')
                    if len(parts)==2:
                        city_name,herustic = parts
                        cities[city_name] = City(city_name,int(herustic))  
                    elif len(parts) == 3:
                        source, destination,distance = parts[0], parts[1],parts[2]
                        city_graph.add_distance(cities[source], cities[destination],int(distance))
             if q=='q4':
                    for line in file:
                        parts = line.strip().split(',')
                        if len(parts)==2:
                            city_name,coffe_quality = parts
                            # print(city_name,coffe_quality)
                            if coffe_quality!='None':
                                cities[city_name] = CityAdversary(city_name,int(coffe_quality)) 
                            else:
                               cities[city_name] = CityAdversary(city_name)  
                        elif len(parts) == 3:
                            # use distance as None only to differntiate from the city
                            source, destination,_ = parts[0], parts[1],parts[2]
                            city_graph.add_distance(cities[source], cities[destination])
        return cities
