from ci_addrs import switches_ch_all
from netmiko import ConnectHandler

numdev = int(input('How many devices? '))
nummac = int(input('How many MAC addresses per device? '))

quad0 = ' 0000.0000.0000'

devlist = []
for i in range(numdev):
    dl = input('Enter the CI\'s name ')
    devlist.append(dl)

macdict = {}
for nd in range (1, numdev+1):
    for nm in range (1, nummac+1):
        macdict['dev{0}mac{1}'.format(nd, nm)] = \
        input('Enter MAC address in Cisco notation (aaaa.bbbb.cccc) \
in the same order you entered MAC addresses: ')

print (devlist)
print (macdict)

def output_d2m1():
    command1 = ('remark N1:' + devlist[0]
    + ', N2:' + devlist[1])
    command2 = ('permit ' + macdict.get('dev1mac1')
    + quad0 + ' ' + macdict.get('dev2mac1') + quad0 + ' 0x806')
    command3 = ('permit ' + macdict.get('dev2mac1')
    + quad0 + ' ' + macdict.get('dev1mac1') + quad0 + ' 0x806')
    command4 = ('permit ' + macdict.get('dev1mac1')
    + quad0 + ' ' + macdict.get('dev2mac1') + quad0 + ' ip')
    command5 = ('permit ' + macdict.get('dev2mac1')
    + quad0 + ' ' + macdict.get('dev1mac1') + quad0 + ' ip')
    result = [command1, command2, command3, command4, command5]
    return result

def output_d2m2():
    pass

def output_d3m1():
    pass

def output_d3m2():
    pass

def output_d4m1():
    pass

def output_d4m2():
    pass


# for i in output_d2m1():
#     print(i)

def connect(x):
    for device in switches_ch_all:
        print ('*******   Connecting to ', device.get('ip'))
        net_connect = ConnectHandler(**device)
        acl_commands = x
        output_acl = net_connect.send_config_set(acl_commands)
        print (output_acl + '\n')

if len(devlist) == 2 and len(macdict) == 1:
    connect(output_d2m1())
elif len(devlist) == 2 and len(macdict) == 4:
    connect(output_d2m2())
elif len(devlist) == 3 and len(macdict) == 3:
    connect(output_d3m1())
elif len(devlist) == 3 and len(macdict) == 6:
    connect(output_d3m2())
elif len(devlist) == 4 and len(macdict) == 4:
    connect(output_d4m1())
elif len(devlist) == 4 and len(macdict) == 8:
    connect(output_d4m2())
