import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.timer = self.create_timer(0.1, self.move)
        self.x = 5.5
        self.y = 5.5
        self.turning = False
        self.turn_count = 0

    def pose_callback(self, msg):
        self.x = msg.x
        self.y = msg.y

    def move(self):
        msg = Twist()
        if self.turning:
            msg.linear.x = 1.0
            msg.angular.z = 1.0
            self.turn_count += 1
            self.get_logger().info('Turning...')
            if self.turn_count >= 20:
                self.turning = False
                self.turn_count = 0
        elif self.x < 1.5 or self.x > 9.5 or self.y < 1.5 or self.y > 9.5:
            self.turning = True
            self.turn_count = 0
            self.get_logger().info('Wall detected!')
        else:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.get_logger().info('Moving forward...')
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = ObstacleAvoider()
    rclpy.spin(node)

if __name__ == '__main__':
    main()