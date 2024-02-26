## Running q1 to q4 of the Project
cd travel_eth_project/travel_ethiopia
- Navigate to the project directory
- Run the main.py file
python main.py
Select the desired *questions* from q1 to q4
- Choose the type of algorithm

## Running q5 of the Project
 This part of the project uses ros2 foxy and gazebo classic 11
 - copy eth_travel_robot to the existing foxy workspace of src directory
 - cd to your workspace where you copied eth_travel_robot directory
 - colcon build --packages-select eth_travel_robot 
 - when the project successfully built 
 Run these commands 
 - ros2 launch eth_travel_robot launch_robot.launch.py 
   This launches the gazebo and the world
 In new terminal run 
   - ros2 run eth_travel_robot nav_move_node.py
   This run the node that executes the main logic for the algorithm and robot motion
   - Enter the start and goal city 
   - Select the algorithm bfs 
Note:
  The algorithm bfs only works in this version of the code and also if no nav_move_node.py file found error arises 
    make this file executable by going to the directory where this file resides and run
    - chmod +x nav_move_node.py
  
