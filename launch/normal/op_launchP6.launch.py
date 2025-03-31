from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    node1 = Node(
        package='misora_gui',
        executable='misora_gui_node',
        name='gui_operate',
        remappings=[
            ('/disaster', '/disaster_report'),
            ('/debris', '/debris_report'),
            ('/missing', '/missing_report'),
        ], 
        parameters=[{"my_parameter": "P6"}]  # ミッション
    )
    node2 = Node(
        package='misora_gui',
        executable='misora_gui_sub_node',
        name='pseudo_digital_twin',
        remappings=[
            ('/disaster', '/disaster_report'),
            ('/debris', '/debris_report'),
            ('/missing', '/missing_report'),
        ], 
        parameters=[{"sub_parameter": "P6"}]
    )

    ld.add_action(node1)
    ld.add_action(node2)

    return ld
