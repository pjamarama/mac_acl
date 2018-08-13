from ci_addrs import test_switch
from netmiko import ConnectHandler

def connect(x):
    print ('*******   Connecting to ', test_switch.get('ip'))
    net_connect = ConnectHandler(test_switch)
    acl_commands = x
    output_acl = net_connect.send_config_set(acl_commands)
    print (output_acl + '\n')

def output_d2m1():
    return 'show clock'

connect(output_d2m1)
