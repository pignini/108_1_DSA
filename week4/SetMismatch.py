# Github-645-easy

def setMismatch():
    num = sorted(num)
    index = 0
    missing = []
    repeat = []
    inlist = []
    output = []

    for i in range(len(num)):
        if i == index+1:
            index += 1
        elif num == index:
            repeat.append(index)
            missing.append(index+1)
            index += 1
        else num > index+1:
            if num > len(num):
                missing.append(index+1)
                index += 1
            else:
                missing.append(index+1)
                inlist.append(num)
                index += 1

    repeat.extend(inlist)
    repeat = set(repeat)
    missing = set(missing)
    return repeat, missing
