import socket

with open(r'E:\GordeyGV$\WS\Python\files\domen_names.txt', 'r') as f:
    domain_list = f.read().splitlines()

ip_list = []
domen_name_off_pc_list = []
index = 1
for domain in domain_list:
    print(index, '-', domain)
    try:
        ip_list.append(socket.gethostbyname(domain))
    except socket.gaierror:
        domen_name_off_pc_list.append(domain)
    index += 1

index = 0
count = 0
for ip in ip_list:
    if index == 16:
        count += 1
        index = 0
    with open(rf'E:\Gordey$\WS\Python\files\scaner_vs\ip.txt', "a") as file:
        file.write(ip + '\n')
    index += 1

with open(r'E:\Gordey$\WS\Python\files\scaner_vs\ip_full.txt', "w") as file:
    for ip in ip_list:
        file.write(ip + '\n')

index = 0
with open(r'E:\Gordey$\WS\Python\files\scaner\domen_names_on.txt', "w") as file:
    for ip in ip_list:
        if index == 16:
            file.write('\n')
            index = 0
        index += 1
        file.write('{0} - {1}\n' .format(socket.getfqdn(ip).split('.')[0], ip))

with open(r'E:\Gordey$\WS\Python\files\scaner\domen_names_off.txt', "w") as file:
    for domen_name in domen_name_off_pc_list:
        file.write(domen_name + '\n')
