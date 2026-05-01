import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TwoTurtles(Node):
    def __init__(self):
        super().__init__('two_turtles')
        self.pub1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move)

    def move(self):
        msg1 = Twist()
        msg1.linear.x = 2.0
        msg1.angular.z = 1.0

        msg2 = Twist()
        msg2.linear.x = 2.0
        msg2.angular.z = -1.0

        self.pub1.publish(msg1)
        self.pub2.publish(msg2)

def main():
    rclpy.init()
    node = TwoTurtles()
    rclpy.spin(node)

if __name__ == '__main__':
    main()