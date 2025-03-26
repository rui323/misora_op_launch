from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer, LoadComposableNodes
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    container = ComposableNodeContainer(
        name="my_container", 
        package="misora_gui",
        executable="",
        namespace="",
        composable_node_descriptions=[
            ComposableNode(
                package="misora_gui",
                plugin="component_operator_gui::DistributeImage",
                name="misora_gui",
                extra_arguments=[{"use_intra_process_comms": True}],
            ),
        ],
        output="screen",
    )
    
    load_composable_nodes = LoadComposableNodes(
        target_container="my_container",
        composable_node_descriptions=[
            ComposableNode(
                package="listener",
                plugin="Listener",
                name="listener",
                extra_arguments=[{"use_intra_process_comms": True}],
            ),
        ],
    )
    
    return LaunchDescription([
        container, 
        load_composable_nodes
    ])
