import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DarwinMotionNode(Node):
    def __init__(self):
        super().__init__('darwin_motion_node')

        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.callback)
        self.i = 0

    def callback(self):
        msg = String()
        msg.data = 'Hello, World! : %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = DarwinMotionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()