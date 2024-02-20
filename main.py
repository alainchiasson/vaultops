#!/usr/bin/env python3
import hvac
from vaultops.vops import vops

if __name__ == '__main__':

    # Starting point
    print("Config: ", vops.config)
    print("Nodes: ", vops.nodes)
    print("Creds: ", vops.creds)

    # get variables
    name = "localhost"

    # add a vault nodes - refactor after

    nodes = vops.nodes
    vops.add_node(name, "http://localhost:8200")
    print("Nodes: ", nodes.nodes)

    # Confirm the node needs to be initialised.
    node = vops.get_node(name)
    print("Node: ", node)

    # Init the nodes
    result = vops.init_node(name)
    print("Result: ", result)

    print("Nodes: ", nodes.nodes)

    vops.write()

    response = vops.unseal_node(name)
    #response = client.sys.submit_unseal_keys(cred['keys'])

    print(response)