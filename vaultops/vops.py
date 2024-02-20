# #!/usr/bin/env python3
import hvac
from vaultops.config_loader import config
from vaultops.nodelist import nodes
from vaultops.credlist import creds

class _Vops():
    def __init__(self):
        """Create the Nodes object"""
        self.config = config
        self.nodes = nodes
        self.creds = creds

vops = _Vops()




# if __name__ == '__main__':

#     # Starting point
#     print("Config: ", config.config)
#     print("Nodes: ", nodes.nodes)
#     print("Creds: ", creds.creds)

#     # get variables
#     name = "localhost"

#     # add a vault nodes
#     nodes.add_node(name, "http://localhost:8200")
#     print("Nodes: ", nodes.nodes)

#     # Confirm the node needs to be initialised.
#     node = nodes.get_node(name)
#     print("Node: ", node)

#     # Initi the nodes
#     client = hvac.Client(url=node['address'])
#     result = client.sys.initialize(5,3)

#     # Add the result to the cred list
#     creds.add_cred_from_result(name, result)
#     print("Creds: ", creds.creds)

#     # Link the node to the cred
#     nodes.nodes[name]['creds'] = "localhost"

#     print("Nodes: ", nodes.nodes)

#     creds.write_credlist()
#     nodes.write_nodelist()

#     cred_link = nodes.get_node(name)['creds']

#     print(cred_link)

#     cred = creds.get_cred(cred_link)

#     print(cred)
#     print(cred['keys'])

#     response = client.sys.submit_unseal_keys(cred['keys'])

#     print(response)