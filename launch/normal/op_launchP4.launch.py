from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    node1 = Node(
        package='misora_gui',
        executable='misora_gui_node',
        name='gui_operate',
        remappings=[
            ('/bulb', '/bulb_operate'),
            ('/disaster', '/disaster_report'),
            ('/debris', '/debris'),
        ],
        parameters=[{"my_parameter": "P4"}]  # ミッション
    )
    node2 = Node(
        package='misora_gui',
        executable='misora_gui_sub_node',
        name='pseudo_digital_twin',
        parameters=[{"sub_parameter": "P4"}]
    )
    ld.add_action(node1)
    ld.add_action(node2)
    return ld