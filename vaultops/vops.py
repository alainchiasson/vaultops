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

    def add_node(self, name, address):
        """Add a node to the list"""
        self.nodes.add_node(name, address)


    def get_node(self, name):
        """Get a node from the list"""
        return self.nodes.get_node(name)   


    def init_node(self, name):
        """Initialise a node"""
        node = self.nodes.get_node(name)
        client = hvac.Client(url=node['address'])
        result = client.sys.initialize(5,3)

        # Create a new credential store
        self.creds.add_cred_from_result(name, result)

        # Create a "soft link" between the node and the credential
        self.nodes.nodes[name]['creds'] = name

        return result
    
    def unseal_node(self, name):
        """Unseal a node"""
        node = self.nodes.get_node(name)
        cred_link = node['creds']
        cred = self.creds.get_cred(cred_link)
        client = hvac.Client(url=node['address'])
        response = client.sys.submit_unseal_keys(cred['keys'])
        return response
    
    def write(self):
        # Store the changes
        # self.config.write_config()
        self.creds.write_credlist()
        self.nodes.write_nodelist()
    
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