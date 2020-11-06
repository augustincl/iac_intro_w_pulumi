#setup project package
import os
import sys

root_folder=os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

#Prepare the Mock for the test
import pulumi

class IaCIntroMocks(pulumi.runtime.Mocks):
    def new_resource(self, type_, name, inputs, provider, id_):
        return [name, inputs]
    def call(self, token, args, providers):
        return {}

pulumi.runtime.set_mocks(IaCIntroMocks())

import unittest
import infrabase
from pulumi_gcp import compute

class TestingMe(unittest.TestCase):

    # 1. Firewall should only allow the traffic from port 22 and port 80
    @pulumi.runtime.test
    def test_firewall_settings(self):
        def check_ports(args):
            #conver the allowed ports into a list for the later checking
            actualAllows=[]
            for allow in args[0]:
                ports=allow.get("ports")
                ports.sort()
                elem="".join(ports)
                elem+="_"+allow.get("protocol")
                actualAllows.append(elem)

            #port number in the alphabetical order
            expectedAllows=["22_tcp","80_tcp"]

            #filter out the violations
            unexpectedActual=[port for port in actualAllows if port not in expectedAllows]
            missedExpected=[port for port in expectedAllows if port not in actualAllows]

            #assert the result
            if (len(unexpectedActual)>0 or len(missedExpected)>0):
                self.fail(f"{len(unexpectedActual)} unexpected opened ports :"+str(unexpectedActual)
                    +f"{len(missedExpected)} missed ports :"+str(missedExpected))

        return pulumi.Output.all(infrabase.firewall.allows).apply(check_ports)

    # 2. make sure we leverage the correct cost/quality-level network
    @pulumi.runtime.test
    def test_network_tier(self):
        def check_tier(args):
            #get tier value
            addr_tier, instance_network_interface = args
            instance_network_tier = instance_network_interface[0].get("accessConfigs")[0].get("network_tier")

            #assert the result
            self.assertEqual([addr_tier,instance_network_tier],["STANDARD","STANDARD"])

        return pulumi.Output.all(infrabase.instance_addr.network_tier,infrabase.instance.network_interfaces).apply(check_tier)