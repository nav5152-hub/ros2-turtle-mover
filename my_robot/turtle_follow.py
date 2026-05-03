import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleFollow(Node):
    def __init__(self):
        super().__init__('turtle_follow')
        self.publisher = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.sub1 = self.create_subscription(Pose, '/turtle1/pose', self.turtle1_callback, 10)
        self.sub2 = self.create_subscription(Pose, '/turtle2/pose', self.turtle2_callback, 10)
        self.timer = self.create_timer(0.1, self.follow)
        self.t1x = 5.5
        self.t1y = 5.5
        self.t2x = 5.5
        self.t2y = 5.5
        self.t2theta = 0.0

    def turtle1_callback(self, msg):
        self.t1x = msg.x
        self.t1y = msg.y

    def turtle2_callback(self, msg):
        self.t2x = msg.x
        self.t2y = msg.y
        self.t2theta = msg.theta

    def follow(self):
        dx = self.t1x - self.t2x
        dy = self.t1y - self.t2y
        distance = math.sqrt(dx**2 + dy**2)
        angle_to_target = math.atan2(dy, dx)
        angle_diff = angle_to_target - self.t2theta

        # 각도 정규화
        while angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        while angle_diff < -math.pi:
            angle_diff += 2 * math.pi

        msg = Twist()
        if distance > 0.5:
            msg.linear.x = 1.5 * distance
            msg.angular.z = 4.0 * angle_diff
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = TurtleFollow()
    rclpy.spin(node)

if __name__ == '__main__':
    main()