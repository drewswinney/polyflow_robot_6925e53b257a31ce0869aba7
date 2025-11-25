import json
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    parameters = json.loads('{"joint_ids":[],"control_mode":"velocity","max_velocity":4}')
    configuration = json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')
    inbound_connections = json.loads('[]')
    outbound_connections = json.loads('[]')
    env = {
        "POLYFLOW_NODE_ID": "6925e6ff257a31ce0869abe4",
        "POLYFLOW_PARAMETERS": json.dumps(parameters),
        "POLYFLOW_CONFIGURATION": json.dumps(configuration),
        "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(inbound_connections),
        "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(outbound_connections),
    }

    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["python3", "workspace/src/6925e6ff257a31ce0869abe4/odrive-s1/node.py"],
                additional_env=env,
                output="screen",
            )
        ]
    )