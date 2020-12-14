import socket


# for id_ in range(13):
id_ = 0
with open(rf'E:\GordeyGV$\WS\Python\files\scaner_vs\ip_as_fzd_{id_}.txt', 'r') as f:
    ip_list = f.read().splitlines()

domain_list = []
for ip in ip_list:
    domain_list.append(socket.getfqdn(ip).split('.')[0])

index = 1
ip_list_on = []
domen_name_off_pc_list = []
for domain in domain_list:
    # print(index, '-', domain)
    try:
        ip_list_on.append(socket.gethostbyname(domain))
    except socket.gaierror:
        domen_name_off_pc_list.append(domain)
    index += 1

print('\nВлаченные ПК:')
index = 0
for ip in ip_list_on:
    index += 1
    print(f'{index} - {ip}')

print('\nВыключенные ПК:')
index = 0
for domen_name in domen_name_off_pc_list:
    index += 1
    print(f'{index} - {domen_name}')
