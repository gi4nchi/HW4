import string


def checkOrder(line):
    position=1;
    check=True
    newline=''
    list=[]
    for char in line:
        if line[position]>char:
            position+=1
            newline+=char
        else:
            position+=1
            list.append(newline)
            newline=''

    return list



string='sfdvoierylbabcdeffkeuyvr'
list = checkOrder(string)
print(list.sort(key=len))
