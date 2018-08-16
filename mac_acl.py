from ci_addrs import switches_ch_all
from netmiko import ConnectHandler
from time import sleep

zeros = ' 0000.0000.0000'

numdev = int(input('How many devices? (2-4): '))
while numdev not in (2, 3, 4):
    print('There can be only 2 to 4 devices')
    numdev = int(input('How many devices? (2-4): '))

nummac = int(input('How many MAC addresses per device? (1-2): '))
while nummac not in (1, 2):
    print('There can be only 1 to 2 MAC addresses')
    nummac = int(input('How many MAC addresses per device? (1-2): '))

devlist = []
for i in range(numdev):
    dl = input('Enter the CI\'s name ')
    devlist.append(dl)

macdict = {}
for nd in range (1, numdev+1):
    for nm in range (1, nummac+1):
        macdict['dev{0}mac{1}'.format(nd, nm)] = \
        input('Enter MAC address in Cisco notation (aaaa.bbbb.cccc) \
in the same order you entered the devices (e.g. device1 MAC1, device1 MAC2): ')

print ('CI names: ', devlist)
print ('MAC addresses: ', macdict)

def output_d2m1():
    # dev[0] dev[1] mac 1
    command0 = 'mac access-list SB-ACL-VLAN310'
    command1 = ('remark N1:' + devlist[0] + ', N2:' + devlist[1])
    command2 = ('permit ' + macdict.get('dev1mac1') + zeros + ' '
    + macdict.get('dev2mac1') + zeros + ' 0x806')
    command3 = ('permit ' + macdict.get('dev2mac1') + zeros + ' '
    + macdict.get('dev1mac1') + zeros + ' 0x806')
    command4 = ('permit ' + macdict.get('dev1mac1') + zeros + ' '
    + macdict.get('dev2mac1') + zeros + ' ip')
    command5 = ('permit ' + macdict.get('dev2mac1') + zeros + ' '
    + macdict.get('dev1mac1') + zeros + ' ip')
    return [command0, command1, command2, command3, command4, command5]

def output_d2m2():
    # Commands for MAC1 are in output_d2m1(). It has to be executed too
    # dev[0] dev[1] mac 2
    command0 = 'mac access-list SB-ACL-VLAN310'
    command2 = ('permit ' + macdict.get('dev1mac2') + zeros + ' '
    + macdict.get('dev2mac2') + zeros + ' 0x806')
    command3 = ('permit ' + macdict.get('dev2mac2') + zeros + ' '
    + macdict.get('dev1mac2') + zeros + ' 0x806')
    command4 = ('permit ' + macdict.get('dev1mac2') + zeros + ' '
    + macdict.get('dev2mac2') + zeros + ' ip')
    command5 = ('permit ' + macdict.get('dev2mac2') + zeros + ' '
    + macdict.get('dev1mac2') + zeros + ' ip')
    return [command0, command2, command3, command4, command5]

def output_d3m1():
    # dev[0] dev[1]
    # Commands for dev[0], dev[1] MAC1 are in output_d2m1(). It has to be executed too
    #dev[0] dev[2]
    # dev[0] dev[2]
    command0 = 'mac access-list SB-ACL-VLAN310'
    command1 = ('remark N1:' + devlist[0] + ', N2:' + devlist[2])
    command2 = ('permit ' + macdict.get('dev1mac1') + zeros + ' '
    + macdict.get('dev3mac1') + zeros + ' 0x806')
    command3 = ('permit ' + macdict.get('dev3mac1') + zeros + ' '
    + macdict.get('dev1mac1') + zeros + ' 0x806')
    command4 = ('permit ' + macdict.get('dev1mac1') + zeros + ' '
    + macdict.get('dev3mac1') + zeros + ' ip')
    command5 = ('permit ' + macdict.get('dev3mac1') + zeros + ' '
    + macdict.get('dev1mac1') + zeros + ' ip')
    # dev[1] dev[2]
    command6 = ('remark N1:' + devlist[1] + ', N2:' + devlist[2])
    command7 = ('permit ' + macdict.get('dev2mac1') + zeros + ' '
    + macdict.get('dev3mac1') + zeros + ' 0x806')
    command8 = ('permit ' + macdict.get('dev3mac1') + zeros + ' '
    + macdict.get('dev2mac1') + zeros + ' 0x806')
    command9 = ('permit ' + macdict.get('dev2mac1') + zeros + ' '
    + macdict.get('dev3mac1') + zeros + ' ip')
    command10 = ('permit ' + macdict.get('dev3mac1') + zeros + ' '
    + macdict.get('dev2mac1') + zeros + ' ip')
    return [command0, command1, command2, command3, command4,
    command5, command6, command7, command8, command9, command10]

def output_d3m2():
    # devlist[0] devlist[1]
    # Commands for dev[0], dev[1] MAC1, 2 are in output_d2m1(), output_d2m2()
    # dev[0] dev[2]
    # Commands for dev[0] dev[2] MAC 1 are in output_d3m1()
    command0 = 'mac access-list SB-ACL-VLAN310'
    command1 = ('remark N1:' + devlist[0] + ', N2:' + devlist[2])
    command2 = ('permit ' + macdict.get('dev1mac2') + zeros + ' '
    + macdict.get('dev3mac2') + zeros + ' 0x806')
    command3 = ('permit ' + macdict.get('dev3mac2') + zeros + ' '
    + macdict.get('dev1mac2') + zeros + ' 0x806')
    command4 = ('permit ' + macdict.get('dev1mac2') + zeros + ' '
    + macdict.get('dev3mac2') + zeros + ' ip')
    command5 = ('permit ' + macdict.get('dev3mac2') + zeros + ' '
    + macdict.get('dev1mac2') + zeros + ' ip')
    # devlist[1] devlist[2]
    # Commands for dev[1], dev[2] MAC1 are in output_d3m1()
    command6 = ('remark N1:' + devlist[1] + ', N2:' + devlist[2])
    command7 = ('permit ' + macdict.get('dev2mac2') + zeros + ' '
    + macdict.get('dev3mac2') + zeros + ' 0x806')
    command8 = ('permit ' + macdict.get('dev3mac2') + zeros + ' '
    + macdict.get('dev2mac2') + zeros + ' 0x806')
    command9 = ('permit ' + macdict.get('dev2mac2') + zeros + ' '
    + macdict.get('dev3mac2') + zeros + ' ip')
    command10 = ('permit ' + macdict.get('dev3mac2') + zeros + ' '
    + macdict.get('dev2mac2') + zeros + ' ip')
    result = [command0, command1, command2, command3, command4, command5,
    command6, command7, command8, command9, command10]


def output_d4m1():
    pass

def output_d4m2():
    pass

def connect(acl_commands):
    for device in switches_ch_all:
        print ('*******   Connecting to ', device.get('ip'))
        net_connect = ConnectHandler(**device)
        output_acl = net_connect.send_config_set(acl_commands, exit_config_mode=False)
        print (output_acl + '\n')
        sleep(3)

if len(devlist) == 2 and len(macdict) == 1:
    connect(output_d2m1())
elif len(devlist) == 2 and len(macdict) == 4:
    connect(output_d2m1())
    connect(output_d2m2())
elif len(devlist) == 3 and len(macdict) == 3:
    connect(output_d2m1())
    connect(output_d3m1())
elif len(devlist) == 3 and len(macdict) == 6:
    connect(output_d2m1())
    connect(output_d2m2())
    connect(output_d3m1())
    connect(output_d3m2())
elif len(devlist) == 4 and len(macdict) == 4:
    connect(output_d4m1())
else:
    connect(output_d4m2())
