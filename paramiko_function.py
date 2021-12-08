import myParamiko as m
import time

def dobackup(incoming_msg):
    routers = m.get_list_from_file("router_list.txt")

    for router in routers:
        backup(router)

    reply = "Success! \n I saved all backup configs in the current directory in the \'backups\' folder."

    return reply

def backup(router):
    print(f'Connecting to {router["server_ip"]}')
    ssh_client= m.connect(**router)
    shell = m.get_shell(ssh_client)

    shell.send(" terminal length 0\n")
    shell.send("en\n")
    shell.send("show run\n")
    time.sleep(2)
    output = shell.recv(10000)
    output = output.decode('utf-8')
    print(output)
    
    output_list= output.splitlines()
    output_list= output_list[11:-1]
    output = '\n'.join(output_list)
    
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    file_name= f'{router["server_ip"]}_{year}-{month}-{day}.txt'

    with open("./backups/"+file_name, 'w') as f:
        f.write(output)

    m.close(ssh_client)