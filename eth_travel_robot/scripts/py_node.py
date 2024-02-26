#!/usr/bin/env python3
import rclpy

from eth_travel_robot.path_publisher import SearchNode
from eth_travel_robot.path_listener import PathListenerNode

def main(args=None):
	rclpy.init(args=args)
	publisher_node=SearchNode()
	publisher_node.publish_path()
	rclpy.spin(publisher_node)
	rclpy.shutdown()	
if __name__=="__main__":
	main()

