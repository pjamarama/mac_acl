import re

# formating a MAC address to Cisco notation
def format_mac(mac: str) -> str:
    mac = re.sub('[.:-]', '', mac).lower()
    mac = ''.join(mac.split())
    assert len(mac) == 12
    assert mac.isalnum()
    mac = ".".join(["%s" % (mac[i:i+4]) for i in range(0, 12, 4)])
    return mac
# generating a list of commands
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
    for a in result:
        print(a)
    return result

macaddr = input('Enter a MAC address: ')
print(format_mac(macaddr))

numdev = int(input('How many devices? '))
nummac = int(input('How many MAC addresses per device? '))

quad0 = ' 0000.0000.0000'

devlist = []
for i in range(numdev):
    dl = \
    input('Enter the CI\'s name ')
    devlist.append(dl)

macdict = {}
for nd in range (1, numdev+1):
    for nm in range (1, nummac+1):
        macdict['dev{0}mac{1}'.format(nd, nm)] = \
        input('Enter MAC address in Cisco notation (aaaa.bbbb.cccc) \
in the same order you entered MAC addresses: ')

#print (macdict)
#print (devlist)




print (output_d2m1())
