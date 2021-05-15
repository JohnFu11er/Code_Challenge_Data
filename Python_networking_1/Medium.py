'''
MEDIUM
 
From the easy challenge, write a Python script to subnet a network size of your choice. 
Return whether this network is public or private
 
Ex. 192.168.0.0/24
('192.169.0.0/27')
('192.169.0.32/27')
('192.169.0.64/27')
('192.169.0.96/27')
'''

from ipaddress import IPv4Network

def subnets(network, mask, new_mask):
    return IPv4Network(f'{network}/{mask}').subnets(new_prefix=new_mask)


def main():
    network = input("Network Address: ")
    mask = input("Network Mask: ")
    new_mask = int(input("Mask of new subnets: "))
    try:
        data = subnets(network,mask,new_mask)
        print("Private?    /   Subnet")
        for item in data:
            print(f'{item.is_private}     /   {item}')
    except:
        print("Something in your request was incorrect.")
        
        
if __name__ == "__main__":
    main()