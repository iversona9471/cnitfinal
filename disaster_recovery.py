import xml.dom.minidom
from ncclient import manager
import myParamiko as m
import time

def reset_ips():
    #connects to the branch router and gets sends a sh ip int br
    ssh_client= m.connect('192.168.56.108', '22', 'cisco', 'cisco123!')
    shell = m.get_shell(ssh_client)
    output = m.show(shell, 'show ip int br')
    m.close(ssh_client)

    tmp = open('./temps/temp_ip_int_br.txt', 'w')
    tmp.write(output)
    tmp.close()

    tmp = open('./temps/temp_file.txt', 'r')
    lines = tmp.readlines()
    count = 0

    for line in lines:
        count += 1
        if "GigabitEthernet2" in line:
            goodline = line

    goodline1 = goodline.split()
    ip_addr = goodline1[1][:-1] + '1'

    print('NEW IP: ' + ip_addr)
    ssh_client = m.connect('192.168.56.109', '22', 'cisco', 'cisco123!')
    shell = m.get_shell(ssh_client)
    m.send_command(shell, 'enable')
    time.sleep(1)
    m.send_command(shell, 'config t')
    time.sleep(1)
    m.send_command(shell, 'interface G2')
    time.sleep(1)
    m.send_command(shell, 'ip address ' + ip_addr +  ' 255.255.255.0')
    time.sleep(1)
    m.send_command(shell, 'exit')
    time.sleep(1)
    m.send_command(shell, 'exit')

    output = shell.recv(10000)
    output = output.decode('utf-8')
    print(output)

    m.close(ssh_client)