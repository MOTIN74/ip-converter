
from termcolor import colored
print(colored("************************* Domain To IP Converter **************************",'green'))
print(colored("************************* Cyber Expert **************************",'red'))


import socket
import pyfiglet

banner = colored(pyfiglet.figlet_format("IP Converter"),'green')

print(banner)

domain_name = input("Enter your domain name:")

ip = socket.gethostbyname(domain_name)
print("IP for {} : {}".format(domain_name,ip))