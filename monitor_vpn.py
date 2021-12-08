import xml.dom.minidom
from ncclient import manager
import myParamiko as m
import time
from disaster_recovery import reset_ips

def monitor_vpns():
    ssh_client= m.connect('192.168.56.109', '22', 'cisco', 'cisco123!')
    shell = m.get_shell(ssh_client)
    output = m.show(shell, 'show crypto sess')
    m.close(ssh_client)

    tmp = open('./temps/temp_crypto_sess.txt', 'w')
    tmp.write(output)
    tmp.close()

    tmp = open('./temps/temp_crypto_sess.txt', 'r')
    lines = tmp.readlines()
    count = 0

    for line in lines:
        count += 1
        if "Session status:" in line:
            goodline = line
            break

    goodline1 = goodline.split()
    print(goodline1[2])
    return goodline1[2]

def monitoring(incoming_msg):
    message = incoming_msg
    status = monitor_vpns()
    if (status == 'DOWN'):
        reset_ips()
        time.sleep(20)
        monitoring(message)
    else:
        time.sleep(20)
        monitoring(message)    