# #!/usr/bin/env python3
import hvac

from vaultops.config_loader import config
from vaultops.nodelist import nodes
from vaultops.credlist import creds

class _Vops():
    """
    Vault operations class
    This class is a high level operations around the Vault API class, to help manipulate and manage multiple vault systems.
    
    It has classes to help manage the node end point, the credentials associated with them. As well as manage some stadard node 
    operations like initialisation, unsealing and credential management.

    These are ultimatly to be placed either in a vault, or locally encrypted with a DEK-KEK key set.
    """
    def __init__(self):
        """Create the Nodes object"""
        self.config = config
        self.nodes = nodes
        self.creds = creds

    def add_node(self, name, address):
        """Add a node to the list"""
        self.nodes.add(name, address)


    def get_node(self, name):
        """Get a node from the list"""
        return self.nodes.get(name)   


    def init_node(self, name):
        """Initialise a node"""
        node = self.nodes.get(name)
        client = hvac.Client(url=node['address'])
        result = client.sys.initialize(5,3)

        # Create a new credential store
        self.creds.add_from_result(name, result)

        # Create a "soft link" between the node and the credential
        self.nodes.nodes[name]['creds'] = name

        return result
    
    def unseal_node(self, name):
        """Unseal a node"""
        node = self.nodes.get(name)
        node_cred = node['creds']
        cred = self.creds.get(node_cred)
        client = hvac.Client(url=node['address'])
        response = client.sys.submit_unseal_keys(cred['keys'])
        return response
    
    def write(self):
        # Store the changes
        # self.config.write_config()
        self.creds.write_credlist()
        self.nodes.write_nodelist()
    
vops = _Vops()

