# DevNet Always-On NETCONF/YANG & RESTCONF Sandbox Device
# https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
ios_xe1 = {
             "address": "ios-xe-mgmt.cisco.com",
             "netconf_port": 10000,
             "restconf_port": 9443,
             "ssh_port": 8181,
             "username": "developer",
             "password": "C1sco12345",
             "device_type": "cisco_ios"
          }

# DevNet Always-On Sandbox NX-OS
#
nxos1 = {
             "address": "sbx-nxos-mgmt.cisco.com",
             "netconf_port": 10000,
             "restconf_port": 443,
             "ssh_port": 818122,
             "username": "admin",
             "password": "Admin_1234!",
             "device_type": "cisco_nxos"
          }