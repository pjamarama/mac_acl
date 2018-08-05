ch1n5k1 = {
    ip = ''
    username = ''
}


numdev = int(input('How many devices? '))
nummac = int(input('How many MAC addresses per device? '))

# Number of next string
start_string = 1000
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

print (macdict)
print (devlist)



def output_d2m1():
    command1 = (str(start_string+10) + ' remark N1:' + devlist[0]
    + ', N2:' + devlist[1])
    command2 = (str(start_string+20) + ' permit ' + macdict.get('dev1mac1')
    + quad0 + ' ' + macdict.get('dev2mac1') + quad0 + ' 0x806')
    command3 = (str(start_string+30) + ' permit ' + macdict.get('dev2mac1')
    + quad0 + ' ' + macdict.get('dev1mac1') + quad0 + ' 0x806')
    command4 = (str(start_string+20) + ' permit ' + macdict.get('dev1mac1')
    + quad0 + ' ' + macdict.get('dev2mac1') + quad0 + ' ip')
    command5 = (str(start_string+30) + ' permit ' + macdict.get('dev2mac1')
    + quad0 + ' ' + macdict.get('dev1mac1') + quad0 + ' ip')
    return [command1, command2, command3, command4, command5]

cmd_d2m1 = output_d2m1()
print (cmd_d2m1)
