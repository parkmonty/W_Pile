#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

from px4_msgs.msg import OffboardControlMode, TrajectorySetpoint, VehicleCommand, VehicleLocalPosition, VehicleStatus

class pub(Node):
    
    def __init__(self):
        super().__init__('pub')
        qos_profile = QoSProfile(
            reliability = ReliabilityPolicy.BEST_EFFORT,
            durability = DurabilityPolicy.TRANSIENT_LOCAL,
            history = HistoryPolicy.KEEP_LAST,
            depth = 1
        )
        
        self.offboard_control_mode_pub = self.create_publisher(
            OffboardControlMode, '/fmu/in/offboard_control_mode', qos_profile)
        self.trajectory_setpoint_pub = self.create_publisher(
            TrajectorySetpoint, '/fmu/in/trajectory_setpoint', qos_profile)
        self.vehicle_command_pub = self.create_publisher(
            VehicleCommand, '/fmu/in/vehicle_command', qos_profile)
        
        self.vehicle_local_position_sub = self.create_subscription(
            VehicleLocalPosition, '/fmu/out/vehicle_local_position', self.vehicle_local_position_callback, qos_profile)
        self.vehicle_status_sub = self.create_subscription(
            VehicleStatus, '/fmu/out/vehicle_status', self.vehicle_status_callback, qos_profile)
        
        self.offboard_setpoint_counter = 0
        self.vehicle_local_position = VehicleLocalPosition()
        self.vehicle_status = VehicleStatus()
        
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        self.x, self.y = input("PX4 Rover Position control\n-----------------------------------------\nInput desired position based on NED frame\n-----------------------------------------\n").split()
        self.x = float(self.x)
        self.y = float(self.y)
        self.x1 = 0.0
        self.y1 = 0.0
        
    def publish_offboard_control_heartbeat_signal(self):
        msg = OffboardControlMode()
        msg.position = True
        msg.velocity = False
        msg.acceleration = False
        msg.attitude = False
        msg.body_rate = False
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.offboard_control_mode_pub.publish(msg)
            
    def publish_position_setpoint(self, x: float, y: float, z: float):
        msg = TrajectorySetpoint()
        msg.position = [x, y, z]
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.trajectory_setpoint_pub.publish(msg)
        self.get_logger().info(f"Publishing position setpoints {[x, y, z]}")
            
    def publish_vehicle_command(self, command, **params) -> None:
        msg = VehicleCommand()
        msg.command = command
        msg.param1 = params.get("param1", 0.0)
        msg.param2 = params.get("param2", 0.0)
        msg.param3 = params.get("param3", 0.0)
        msg.param4 = params.get("param4", 0.0)
        msg.param5 = params.get("param5", 0.0)
        msg.param6 = params.get("param6", 0.0)
        msg.param7 = params.get("param7", 0.0)
        msg.target_system = 1
        msg.target_component = 1
        msg.source_system = 1
        msg.source_component = 1
        msg.from_external = True
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.vehicle_command_pub.publish(msg)
        
    def arm(self):
        self.publish_vehicle_command(
            VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, param1 = 1.0)
        self.get_logger().info('Arm command sent')
            
    def disarm(self):
        self.publish_vehicle_command(
            VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM, param1 = 0.0)
        self.get_logger().info('Disarm command sent')
            
    def engage_offboard_mode(self):
        self.publish_vehicle_command(
            VehicleCommand.VEHICLE_CMD_DO_SET_MODE, param1 = 1.0, param2 = 6.0)
        self.get_logger().info("Switching to offboard mode")
    
    def vehicle_local_position_callback(self, vehicle_local_position):
        self.vehicle_local_position = vehicle_local_position
    
    def vehicle_status_callback(self, vehicle_status):
        self.vehicle_status = vehicle_status
    
    def timer_callback(self) -> None:
        self.publish_offboard_control_heartbeat_signal()
                
        if self.offboard_setpoint_counter == 10:
            self.engage_offboard_mode()
            self.arm()
            
        if self.vehicle_status.nav_state == VehicleStatus.NAVIGATION_STATE_OFFBOARD:
            self.publish_position_setpoint(self.x, self.y, 0.0)
        
        if self.x != 0.0 and self.y == 0.0:
            if self.x > 0.0 and self.x >= self.x1 and self.vehicle_local_position.x >= self.x:
                self.x1 = self.x
                self.y1 = self.y
                self.x, self.y = input("PX4 Rover Position control\n-----------------------------------------\nInput desired position based on NED frame\n-----------------------------------------\n").split()
                self.x = float(self.x)
                self.y = float(self.y)
            elif self.x > 0.0 and self.x < self.x1 and self.vehicle_local_position.x <= self.x:
                self.x1 = self.x
                self.y1 = self.y
                self.x, self.y = input("PX4 Rover Position control\n-----------------------------------------\nInput desired position based on NED frame\n-----------------------------------------\n").split()
                self.x = float(self.x)
                self.y = float(self.y)
            elif self.x < 0.0 and self.x < self.x1 and self.vehicle_local_position.x <= self.x:
                self.x1 = self.x
                self.y1 = self.y
                self.x, self.y = input("PX4 Rover Position control\n-----------------------------------------\nInput desired position based on NED frame\n-----------------------------------------\n").split()
                self.x = float(self.x)
                self.y = float(self.y)
            elif self.x < 0.0 and self.x >= self.x1 and self.vehicle_local_position.x >= self.x:
                self.x1 = self.x
                self.y1 = self.y
                self.x, self.y = input("PX4 Rover Position control\n-----------------------------------------\nInput desired position based on NED frame\n-----------------------------------------\n").split()
                self.x = float(self.x)
                self.y = float(self.y)
        elif self.x == 0.0 and self.y != 0:
            if self.y > 0.0 and self.y >= self.y1 and self.vehicle_local_position.y >= self.y:
                self.x1 = self.x
                self.y1 = self.y
                self.x, self.y = input("PX4 Rover Position control\n-----------------------------------------\nInput desired position based on NED frame\n-----------------------------------------\n").split()
                self.x = float(self.x)
                self.y = float(self.y)
            elif self.y > 0.0 and self.y < self.y1 and self.vehicle_local_position.y <= self.y:
                self.x1 = self.x
                self.y1 = self.y
                self.x, self.y = input("PX4 Rover Position control\n-----------------------------------------\nInput desired position based on NED frame\n-----------------------------------------\n").split()
                self.x = float(self.x)
                self.y = float(self.y)
            elif self.y < 0.0 and self.y < self.y1 and self.vehicle_local_position.y <= self.y:
                self.x1 = self.x
                self.y1 = self.y
                self.x, self.y = input("PX4 Rover Position control\n-----------------------------------------\nInput desired position based on NED frame\n-----------------------------------------\n").split()
                self.x = float(self.x)
                self.y = float(self.y)
            elif self.y < 0.0 and self.y >= self.y1 and self.vehicle_local_position.y >= self.y:
                self.x1 = self.x
                self.y1 = self.y
                self.x, self.y = input("PX4 Rover Position control\n-----------------------------------------\nInput desired position based on NED frame\n-----------------------------------------\n").split()
                self.x = float(self.x)
                self.y = float(self.y)
        elif self.x == 0.0 and self.y == 0.0:
            if self.vehicle_local_position.vx <= 0.0 and self.vehicle_local_position.vy <= 0.0:
                self.disarm()
                exit(0)
            
        # elif self.x != 0.0 and self.y != 0.0:
        #     if self.x > 0.0 and self.x >= self.x1 and self.vehicle_local_position.x >= self.x:
        #         if self.y > 0.0 and self.y >= self.y1 and self.vehicle_local_position.y >= self.y:
        #             self.x1 = self.x
        #             self.y1 = self.y
        #             self.x, self.y = input().split()
        #             self.x = float(self.x)
        #             self.y = float(self.y)
        #         elif self.y > 0.0 and self.y < self.y1 and self.vehicle_local_position.y <= self.y:
        #             self.x1 = self.x
        #             self.y1 = self.y
        #             self.x, self.y = input().split()
        #             self.x = float(self.x)
        #             self.y = float(self.y)
        #         elif self.y < 0.0 and self.y < self.y1 and self.vehicle_local_position.y <= self.y:
        #             self.x1 = self.x
        #             self.y1 = self.y
        #             self.x, self.y = input().split()
        #             self.x = float(self.x)
        #             self.y = float(self.y)
        #         elif self.y < 0.0 and self.y >= self.y1 and self.vehicle_local_position.y >= self.y:
        #             self.x1 = self.x
        #             self.y1 = self.y
        #             self.x, self.y = input().split()
        #             self.x = float(self.x)
        #             self.y = float(self.y)
        #     elif self.x > 0.0 and self.x < self.x1 and self.vehicle_local_position.x <= self.x:
        #         self.x1 = self.x
        #         self.y1 = self.y
        #         self.x, self.y = input().split()
        #         self.x = float(self.x)
        #         self.y = float(self.y)
        #     elif self.x < 0.0 and self.x < self.x1 and self.vehicle_local_position.x <= self.x:
        #         self.x1 = self.x
        #         self.y1 = self.y
        #         self.x, self.y = input().split()
        #         self.x = float(self.x)
        #         self.y = float(self.y)
        #     elif self.x < 0.0 and self.x >= self.x1 and self.vehicle_local_position.x >= self.x:
        #         self.x1 = self.x
        #         self.y1 = self.y
        #         self.x, self.y = input().split()
        #         self.x = float(self.x)
        #         self.y = float(self.y)
            
        if self.offboard_setpoint_counter < 11:
            self.offboard_setpoint_counter += 1
            
def main(args=None) -> None:
    print('Starting offboard control node...')
    rclpy.init(args=args)
    offboard_control = pub()
    rclpy.spin(offboard_control)
    offboard_control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
