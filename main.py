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

    #client = hvac.Client(url=node['address'])
    #result = client.sys.initialize(5,3)

    # Add the result to the cred list
    # creds = vops.creds
    # creds.add_cred_from_result(name, result)
    # print("Creds: ", creds.creds)

    # Link the node to the cred
    # nodes.nodes[name]['creds'] = "localhost"

    print("Nodes: ", nodes.nodes)

    vops.write()

    cred_link = nodes.get_node(name)['creds']
    print(cred_link)
    cred = vops.creds.get_cred(cred_link)
    print(cred)
    print(cred['keys'])


    response = vops.unseal_node(name)
    #response = client.sys.submit_unseal_keys(cred['keys'])

    print(response)