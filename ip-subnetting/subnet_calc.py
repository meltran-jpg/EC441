import ipaddress

network = ipaddress.ip_network("192.168.1.0/24")

print("Network:", network.network_address)
print("Broadcast:", network.broadcast_address)

print("First 5 Hosts:")
for i, host in enumerate(network.hosts()):
    if i == 5:
        break
    print(host)
