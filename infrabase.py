import pulumi
from pulumi import ResourceOptions
from pulumi_gcp import compute
import script_init_nginx

#setup the network settings
network=compute.Network("network-4-intro")

firewall=compute.Firewall(
    "firewall-4-intro",
    network=network.self_link,
    allows=[
        compute.FirewallAllowArgs(
            protocol="tcp",
            ports=["22"]
        ),
        compute.FirewallAllowArgs(
            protocol="tcp",
            ports=["80"]
        ),
        #WARN: for unit test demo only.
#       compute.FirewallAllowArgs(
#            protocol="udp",
#            ports=["53"]
#        )
    ]
)


#setup the compute engine and init it with the script
instance_addr=compute.Address("addr-4-intro",network_tier="STANDARD")
instance=compute.Instance(
    "instance-4-intro",
    machine_type="e2-small",
    boot_disk=compute.InstanceBootDiskArgs(
        initialize_params=compute.InstanceBootDiskInitializeParamsArgs(
            image="ubuntu-os-cloud/ubuntu-1804-bionic-v20200414"
        ),
    ),
    network_interfaces=[
        compute.InstanceNetworkInterfaceArgs(
            network=network.id,
            access_configs=[compute.InstanceNetworkInterfaceAccessConfigArgs(
                nat_ip=instance_addr.address,
                network_tier="STANDARD"
            )]
        )
    ],
    metadata_startup_script=script_init_nginx.init_4_nginx,
    opts=ResourceOptions(delete_before_replace=True),
    zone="asia-east1-a",
)
