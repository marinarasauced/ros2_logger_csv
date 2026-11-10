#!/usr/bin/env python3

import rclpy
from rclpy.executors import MultiThreadedExecutor

from ros2_logger_csv.logger_init import LoggerInitializer
from ros2_logger_csv.logger_node import LoggerNode


def main(args=None):
    """
    """
    rclpy.init(args=args)
    initializer = LoggerInitializer()

    container: list[LoggerNode] = []
    for topic_name in initializer.topic_names:
        clean_name = topic_name.strip("/").replace("/", "_")
        node_name = f"ros2_logger_csv_{clean_name}"
        container.append(LoggerNode(
            log_dir_path=initializer.log_dir_path, 
            node_name=node_name,
            topic_name=topic_name,
            period=initializer.period
        ))
    
    initializer.destroy_node()

    executor = MultiThreadedExecutor(num_threads=2)
    for node in container:
        executor.add_node(node)
    
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        for node in container:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__=="__main__":
    main()
