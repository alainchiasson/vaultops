#!/usr/bin/env python3
import hvac
from vaultops.vops import vops

if __name__ == '__main__':

    # get variables
    name = "localhost"

    # Add a node to be managed.
    vops.add_node(name, "http://localhost:8200")
    result = vops.init_node(name)

    vops.write()

    # Unseal the node
    response = vops.unseal_node(name)

