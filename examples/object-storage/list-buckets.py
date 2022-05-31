# 
#  Sample code to get list of buckets based on region, compartment, name space.
#  You may still add more select criteria in list_buckets like compartment_id, namespace_name.
#  
#  Sample Output (Masked):
#  [Bucket] Name: tagtestbucket3
#  [Bucket] Name: testbucket1
#  [Bucket] Name: testbucket2
# 

import oci
import os.path
import sys

config = oci.config.from_file()
config['region'] = "us-ashburn-1"

os_client = oci.object_storage.ObjectStorageClient(config)

response = os_client.list_buckets(compartment_id = config['tenancy'], namespace_name = "fa...cy")

for bucket in response.data:
    print("Bucket: " + bucket.name)
