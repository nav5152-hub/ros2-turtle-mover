import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleMover(Node):
    def __init__(self):
        super().__init__('turtle_mover')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_turtle)
        self.step = 0
        self.count = 0

    def move_turtle(self):
        msg = Twist()
        if self.count < 20:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 1.6
            if self.count >= 26:
                self.count = -1
        self.publisher.publish(msg)
        self.count += 1

def main():
    rclpy.init()
    node = TurtleMover()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
