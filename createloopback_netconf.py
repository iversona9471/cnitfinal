import xml.dom.minidom

from ncclient import manager

m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )


netconf_loopback = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<interface>
<Loopback>
<name>1</name>                                        
<description>Other Loopback0</description>            
<ip>
<address>
<primary>
<address>1.1.1.1</address>
<mask>255.255.255.0</mask>
</primary>
</address>
</ip>
</Loopback>
</interface>
</native>
</config>
"""
print('#'*80)
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


