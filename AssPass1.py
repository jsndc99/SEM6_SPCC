inputList = []
with open("ainput.txt", "r") as f:
    for ip in f:
        inputList.append(ip.strip("\n").strip("\r"))

symtab = open("SymbolTable.txt", "w")

a = (inputList.pop(0)).split(" ")
startaddr = int(a[2])

for item in inputList:
    ins = item.split(" ")
    print "Ins is: ", ins

    if ins[1] == 'USING':
        continue
    else:
        if not ins[0] == "**" :
            symtab.write(ins[0] + " " + str(startaddr) + "\n")
            startaddr += 4
        else:
            startaddr += 4

    
