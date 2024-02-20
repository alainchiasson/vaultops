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
        self.creds.add_cred_from_result(name, result)

        # Create a "soft link" between the node and the credential
        self.nodes.nodes[name]['creds'] = name

        return result
    
    def unseal_node(self, name):
        """Unseal a node"""
        node = self.nodes.get(name)
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

