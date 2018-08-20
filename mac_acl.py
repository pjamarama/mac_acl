from time import sleep
from netmiko import ConnectHandler
from ci_addrs import switches_ch_all

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
    dl = input('Enter the CI\'s name: ')
    devlist.append(dl)

macdict = {}
for nd in range(1, numdev+1):
    for nm in range(1, nummac+1):
        macdict['dev{0}mac{1}'.format(nd, nm)] = \
        input('Enter MAC address in Cisco notation (aaaa.bbbb.cccc) \
in the same order you entered the devices (e.g. device1 MAC1, device1 MAC2): ')

print('CI names: ', devlist)
print('MAC addresses: ', macdict)

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
    command2 = ('permit ' + macdict.get('dev1mac2') + zeros + ' '               ';'
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
    return [command0, command1, command2, command3, command4, command5,
    command6, command7, command8, command9, command10]

def output_d4m1():
    # dev1mac1 dev2mac1 defined in output_d2m1(). To be executed
    # dev1mac1 dev3mac1
    # dev2mac1 dev3mac1
    # defined in output_d3m1(). To be executed

    # dev1mac1 dev4mac1
    command0 = 'mac access-list SB-ACL-VLAN310'
    command1 = ('remark N1:' + devlist[0] + ', N2:' + devlist[3])
    command2 = ('permit ' + macdict.get('dev1mac1') + zeros + ' '
    + macdict.get('dev4mac1') + zeros + ' 0x806')
    command3 = ('permit ' + macdict.get('dev4mac1') + zeros + ' '
    + macdict.get('dev1mac1') + zeros + ' 0x806')
    command4 = ('permit ' + macdict.get('dev1mac1') + zeros + ' '
    + macdict.get('dev4mac1') + zeros + ' ip')
    command5 = ('permit ' + macdict.get('dev4mac1') + zeros + ' '
    + macdict.get('dev1mac1') + zeros + ' ip')

    # dev2mac1 dev4mac1
    command6 = ('remark N1:' + devlist[1] + ', N2:' + devlist[3])
    command7 = ('permit ' + macdict.get('dev2mac1') + zeros + ' '
    + macdict.get('dev4mac1') + zeros + ' 0x806')
    command8 = ('permit ' + macdict.get('dev4mac1') + zeros + ' '
    + macdict.get('dev2mac1') + zeros + ' 0x806')
    command9 = ('permit ' + macdict.get('dev2mac1') + zeros + ' '
    + macdict.get('dev4mac1') + zeros + ' ip')
    command10 = ('permit ' + macdict.get('dev4mac1') + zeros + ' '
    + macdict.get('dev2mac1') + zeros + ' ip')

    # dev3mac1 dev4mac1
    command11 = ('remark N1:' + devlist[2] + ', N2:' + devlist[3])
    command12 = ('permit ' + macdict.get('dev3mac1') + zeros + ' '
    + macdict.get('dev4mac1') + zeros + ' 0x806')
    command13 = ('permit ' + macdict.get('dev4mac1') + zeros + ' '
    + macdict.get('dev3mac1') + zeros + ' 0x806')
    command14 = ('permit ' + macdict.get('dev3mac1') + zeros + ' '
    + macdict.get('dev4mac1') + zeros + ' ip')
    command15 = ('permit ' + macdict.get('dev4mac1') + zeros + ' '
    + macdict.get('dev3mac1') + zeros + ' ip')
    return [command0, command1, command2, command3, command4, command5,
    command6, command7, command8, command9, command10, command11,
    command12, command13, command14, command15]

def output_d4m2():
    # Commands for devlist[0] devlist[1] MAC1 are in output_d2m1()
    # Commands for devlist[0] devlist[1] MAC2 are in output_d2m2()
    # Commands for devlist[0] devlist[2] MAC 1 are in output_d3m1()
    # Commands for devlist[0] devlist[2] MAC 2 are in output_d3m2()
    # Commands for devlist[0] devlist[3] MAC 1 are in output_d4m1()
    command0 = 'mac access-list SB-ACL-VLAN310'
    command1 = ('remark N1:' + devlist[0] + ', N2:' + devlist[3])
    # dev1mac2 dev4mac2
    command2 = ('permit ' + macdict.get('dev1mac2') + zeros + ' '
    + macdict.get('dev4mac2') + zeros + ' 0x806')
    command3 = ('permit ' + macdict.get('dev4mac2') + zeros + ' '
    + macdict.get('dev1mac2') + zeros + ' 0x806')
    command4 = ('permit ' + macdict.get('dev1mac2') + zeros + ' '
    + macdict.get('dev4mac2') + zeros + ' ip')
    command5 = ('permit ' + macdict.get('dev4mac2') + zeros + ' '
    + macdict.get('dev1mac2') + zeros + ' ip')
    # dev2mac2 dev4mac2
    command6 = ('remark N1:' + devlist[1] + ', N2:' + devlist[3])
    command7 = ('permit ' + macdict.get('dev2mac2') + zeros + ' '
    + macdict.get('dev4mac2') + zeros + ' 0x806')
    command8 = ('permit ' + macdict.get('dev4mac2') + zeros + ' '
    + macdict.get('dev2mac2') + zeros + ' 0x806')
    command9 = ('permit ' + macdict.get('dev2mac2') + zeros + ' '
    + macdict.get('dev4mac2') + zeros + ' ip')
    command10 = ('permit ' + macdict.get('dev4mac2') + zeros + ' '
    + macdict.get('dev2mac2') + zeros + ' ip')
    # dev3mac2 dev4mac2
    command11 = ('remark N1:' + devlist[2] + ', N2:' + devlist[3])
    command12 = ('permit ' + macdict.get('dev3mac2') + zeros + ' '
    + macdict.get('dev4mac2') + zeros + ' 0x806')
    command13 = ('permit ' + macdict.get('dev4mac2') + zeros + ' '
    + macdict.get('dev3mac2') + zeros + ' 0x806')
    command14 = ('permit ' + macdict.get('dev3mac2') + zeros + ' '
    + macdict.get('dev4mac2') + zeros + ' ip')
    command15 = ('permit ' + macdict.get('dev4mac2') + zeros + ' '
    + macdict.get('dev3mac2') + zeros + ' ip')
    return [command0, command1, command2, command3, command4, command5,
    command6, command7, command8, command9, command10, command11,
    command12, command13, command14, command15]

def command_list(*x):
    print('The commands to be sent are: \n')
    for command in x:
        for c in command:
            print(c)
    confirm = input('Would you like to connect to devices and \
send these commands? (y/n)' )
    if confirm == 'y':
        return print('Okay then. Fasten your seatbelts.')
    else:
        print('Have a nice day!')
        quit()


def connect(acl_commands):
    for device in switches_ch_all:
        print('*******   Connecting to ', device.get('ip'))
        net_connect = ConnectHandler(**device)
        output_acl = net_connect.send_config_set(acl_commands, exit_config_mode=False)
        print(output_acl + '\n')
        sleep(5)

if len(devlist) == 2 and len(macdict) == 2:
    command_list(output_d2m1())
    connect(output_d2m1())
elif len(devlist) == 2 and len(macdict) == 4:
    command_list(output_d2m1(), output_d2m2())
    connect(output_d2m1())
    connect(output_d2m2())
elif len(devlist) == 3 and len(macdict) == 3:
    command_list(output_d2m1(), output_d3m1())
    connect(output_d2m1())
    connect(output_d3m1())
elif len(devlist) == 3 and len(macdict) == 6:
    command_list(output_d2m1(), output_d2m2(), output_d3m1(), output_d3m2())
    connect(output_d2m1())
    connect(output_d2m2())
    connect(output_d3m1())
    connect(output_d3m2())
elif len(devlist) == 4 and len(macdict) == 4:
    command_list(output_d2m1(), output_d3m1(), output_d4m1())
    connect(output_d2m1())
    connect(output_d3m1())
    connect(output_d4m1())
else:
    command_list(output_d2m1(), output_d2m2(), output_d3m1(), output_d3m2(),
output_d4m1(), output_d4m2())
    connect(output_d2m1())
    connect(output_d2m2())
    connect(output_d3m1())
    connect(output_d3m2())
    connect(output_d4m1())
    connect(output_d4m2())
