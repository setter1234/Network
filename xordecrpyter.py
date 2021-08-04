import os
def reverse(num):
    if(num == 0):
        return 1
    else:
        return 0
before = input("input file")
key = list(map(int,input("xor key value (4 number)").split()))
after = input("output file")
before = open(before,"rb")
after = open(after,"wb")
keycount = 0
while(True):
    if(keycount == 4):
        keycount = 0
    keyvalues = key[keycount]
    keycount += 1
    value = before.read(1)
    if(value == b''):
        break
    buf = int.from_bytes(value,"little")
    buf = format(buf,"08b")
    keybit = format(keyvalues,"08b")
    seq = 0
    total = 0
    for i in range(7,-1,-1):
        if(keybit[seq] == '0'):
            total += int(buf[seq]) * (2**i)
        else:
            total += reverse(int(buf[seq])) * (2**i)
        seq += 1
    after.write((total).to_bytes(1,"little"))
before.close()
after.close()
