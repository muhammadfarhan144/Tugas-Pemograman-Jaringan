import ipaddress 

def validate_ip_address(address):
    while True:
        try:
            ip = ipaddress.ip_address(address)
            print("{} adalah IP valid.".format(address, ip))
            break
        except ValueError:
            print("{} adalah IP tidak valid".format(address))
            break
ip = input("Masukan alamat IP : ")
validate_ip_address(ip)