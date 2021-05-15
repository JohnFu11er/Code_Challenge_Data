'''
EASY
 
From a list of IP addresses, return the first index and the last index in the list. Also return the number of available hosts in your network. 
 
*** Networks can be chosen at random, or you can use the example network below ***
 
Ex. 
['192.168.0.0', '192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5', '192.168.0.6', '192.168.0.7']
 
192.168.0.0
192.168.0.7
6 hosts in this range
'''

from ipaddress import IPv4Network

def network_data(network, mask):
    full_network = IPv4Network(f'{network}/{mask}', strict=True)
    data = [
        f'NETWORK:           {full_network}',
        f'Avaliable hosts:   {len([i for i in full_network])-2}',
        f'Network ID:        {full_network[0]}',
        f'First Usable:      {full_network[1]}',
        f'Last Usable:       {full_network[-2]}',
        f'Broadcast Address: {full_network[-1]}'
    ]
    
    return data

def main():
    network = input("Network Address: ")
    mask = input("Mask: ")
    print("*"*20 + "\n")
    
    try:
        for item in network_data(network,mask):
            print(item)
    except:
        print("Something in your request was incorrect.")
        
if __name__ == "__main__":
    main()
