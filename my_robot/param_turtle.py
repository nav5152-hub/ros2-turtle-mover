import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ParamTurtle(Node):
    def __init__(self):
        super().__init__('param_turtle')
        self.declare_parameter('linear_speed', 2.0)
        self.declare_parameter('angular_speed', 1.0)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move)

    def move(self):
        linear = self.get_parameter('linear_speed').value
        angular = self.get_parameter('angular_speed').value

        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        self.publisher.publish(msg)
        self.get_logger().info(f'Speed: linear={linear}, angular={angular}')

def main():
    rclpy.init()
    node = ParamTurtle()
    rclpy.spin(node)

if __name__ == '__main__':
    main()