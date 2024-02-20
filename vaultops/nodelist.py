import json
import os
import hvac

class _Nodes(dict):
    def __init__(self):
        """Create the Nodes object"""
        self.nodes = {}

    def read_nodelist(self, node_file="node_config.json"):
        """Load the nodes from the config file"""
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), node_file)) as json_config_file:
            loaded_conf = json.load(json_config_file)
        
    def write_nodelist(self, node_file="node_config.json"):
        """Write the nodes to the config file"""
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), node_file), 'w') as json_config_file:
            json.dump(self.nodes, json_config_file)

    def add_node(self, name, address):
        """Add a node to the list"""
        # TODO: Verify if node exists, if so error out.
        # TODO: Should take NODE object.
        # new_node = Node(name, address)
        new_node = {
                "address": address,
                "creds": ""
            }
        
        self.nodes[name] = new_node

    def get_node(self, name):
        """Get a node from the list"""
        # I sould really return a Node object here.
        return self.nodes[name]

nodes = _Nodes()

# class Node(dict):
#     def __init__(self, name, address):
#         """Vault node definition"""
#         self.node = { name : {
#             "address": address
#         }}

#     @classmethod
#     def from_node(cls, node):
#         """New Node object from a Node object"""
#         if type(node) is not Node:
#             raise TypeError("Expected Node object")

#         return cls(node.name, node.address)
    

#     def __dict__(self):
#         return self.node

    # def get_vault_endpoint(self):
    #     """Get the status of the node"""
    #     return hvac.Client(url=self.node['address'])


