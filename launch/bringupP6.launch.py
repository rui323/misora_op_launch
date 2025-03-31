from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer, LoadComposableNodes
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    container = ComposableNodeContainer(
        name="misora_op", 
        package="rclcpp_components",
        executable="component_container_mt",#マルチスレッドの場合component_container_mt,シングルはcomponent_container
        namespace="",
        composable_node_descriptions=[
            ComposableNode(
                package="misora_gui",
                plugin="component_operator_gui::DistributeImage",
                name="misora_gui",
                extra_arguments=[{"use_intra_process_comms": True}],
                parameters=[{"my_parameter": "P6"}]
            ),
            ComposableNode(
                package="misora_gui",
                plugin="component_operator_gui_sub::DistributeImage_sub",
                name="pseudo_dt_client",
                extra_arguments=[{"use_intra_process_comms": True}],
                parameters=[{"sub_parameter": "P6"}]
            )
        ],
        output="screen",
    )
    # remapping で"0 | 1"を"bulb_operate" "OP | CL"を"bulb_report"
    
    # load_composable_nodes = LoadComposableNodes(
    #     target_container="my_container",
    #     composable_node_descriptions=[
    #         ComposableNode(
    #             package="listener",
    #             plugin="Listener",
    #             name="listener",
    #             extra_arguments=[{"use_intra_process_comms": True}],
    #         ),
    #     ],
    # )
    
    return LaunchDescription([
        container, 
        # load_composable_nodes
    ])
