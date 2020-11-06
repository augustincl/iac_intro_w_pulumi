import pulumi
import infrabase


#export resources
pulumi.export("instance_name", infrabase.instance)
pulumi.export("instance_external_ip", infrabase.instance_addr.address)