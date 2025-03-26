from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    node1 = Node(
        package='misora_gui',
        executable='misora_gui',
        name='gui_operate',
        remappings=[
            ('/bulb', '/bulb_operate'),
        ],
        parameters=[{"my_parameter": "P2"}]  # ミッション
    )
    node2 = Node(
        package='misora_gui',
        executable='misora_gui_sub',
        name='pseudo_digital_twin',
        parameters=[{"sub_parameter": "P2"}]
    )
    ld.add_action(node1)
    ld.add_action(node2)
    return ld