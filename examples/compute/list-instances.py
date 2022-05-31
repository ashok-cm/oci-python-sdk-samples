# 
#  Sample code to get list of instances in particular region, compartment.
#  You may still add more select criteria in list_instances like compartment_id.
#  
#  Sample Output (Masked):
#  Instance: ocid1.instance.oc1.iad.anu...xru2a
# 

import oci
import os.path
import sys

config = oci.config.from_file()
config['region'] = "us-ashburn-1"

compute_client = oci.core.ComputeClient(config)

response = compute_client.list_instances(compartment_id = config['tenancy'])

for instance in response.data:
    print("Instance: " + instance.id)
