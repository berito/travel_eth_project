class UserInput:  
    @staticmethod
    def get_user_input():
        start_city = input("Enter the start city: ")
        goal_city = input("Enter the goal city: ")
        return start_city, goal_city
    @staticmethod
    def get_question_no_input():
            question=input("Enter question (q1,q2,q3,q4) : ")
            return question
    @staticmethod
    def get_question_sub():
            default_start_city='AddisAbaba'
            default_goal_city='Lalibela'
            sub=input("Enter question (1,2) : ")
            if sub=='1':
                choice=input("use default start and goal state y/n : ")
                if choice=='n':
                   start_city,goal_city= UserInput.get_user_input()
                   return sub,start_city,goal_city
            return sub,default_start_city,default_goal_city
    @staticmethod
    def get_search_strategy_input():
            question=input("Enter algorithm (bfs,dfs) : ")
            return question
    @staticmethod
    def get_question3_input():
        default_start_city='AddisAbaba'
        default_goal_city='Moyale'
        choice=input(f"use default start {default_start_city} and goal {default_goal_city} state y/n : ")
        if choice=='n':
            start_city,goal_city= UserInput.get_user_input()
            return start_city,goal_city
        return default_start_city,default_goal_city