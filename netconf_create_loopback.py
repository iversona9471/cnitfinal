import xml.dom.minidom

from ncclient import manager

def create_loopback(incoming_msg):
    m = manager.connect(
        host="192.168.56.109",
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
                    <name>69</name>                                        
                    <description>Other Loopback</description>            
                    <ip>
                        <address>
                            <primary>
                                <address>69.69.69.69</address>
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

    return "Success! Lo69 created on CSR1 (192.168.56.109)!"