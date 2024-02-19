import json
import os
import hvac

class _Creds(dict):
    def __init__(self):
        """Create the creds object"""
        self.creds = {}

    def read_credlist(self, cred_file="cred_config.json"):
        """Load the creds from the config file"""
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), cred_file)) as json_config_file:
            self.creds = json.load(json_config_file)
        

    def write_credlist(self, cred_file="cred_config.json"):
        """Write the creds to the config file"""
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), cred_file), 'w') as json_config_file:
            json.dump(self.creds, json_config_file)

    def add_cred_from_result(self, name, results):
        """Add a cred to the list"""
        self.creds[name] = results

    def add_cred(self, name, keys, root_token):
        """Add a cred to the list"""
        new_cred = {
                "keys": keys,
                "root_token": root_token
            }
        
        self.creds[name] = new_cred

    def get_cred(self, name):
        """Get a cred from the list"""
        # I sould really return a cred object here.
        return self.creds[name]

creds = _Creds()

# class cred(dict):
#     def __init__(self, name, address):
#         """Vault cred definition"""
#         self.cred = { name : {
#             "address": address
#         }}

#     @classmethod
#     def from_cred(cls, cred):
#         """New cred object from a cred object"""
#         if type(cred) is not cred:
#             raise TypeError("Expected cred object")

#         return cls(cred.name, cred.address)
    

#     def __dict__(self):
#         return self.cred

    # def get_vault_endpoint(self):
    #     """Get the status of the cred"""
    #     return hvac.Client(url=self.cred['address'])


