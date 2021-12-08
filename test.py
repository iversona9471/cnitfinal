import myParamiko as m
import time

#router = {'server_ip': '192.168.56.108', 'server_port': '22', 'user':'cisco', 'passwd':'cisco123!'}

ssh_client= m.connect('192.168.56.108', '22', 'cisco', 'cisco123!')
shell = m.get_shell(ssh_client)
output = m.show(shell, 'show ip int br')

tmp = open('./temps/temp_file.txt', 'w')
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
print(ip_addr)