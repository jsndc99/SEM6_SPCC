with open("codeip.txt", "r") as f:
    contents = f.read().splitlines()
print contents


registers = [0, 0, 0, 0, 0]
usedVal = [None, None, None, None, None]

def isVisisted(val):
    try:
        return (usedVal.index(val))
    
    except:
        return - 1


def giveReg():
    try:
        return (registers.index(0))
    
    except:
        return - 1

with open("codeop.txt", "w") as f:     
    for item in contents:
        if len(item) == 4:
            if isVisisted(item[1]) == -1:
                pos = giveReg()
                usedVal[pos] = item[1]
                registers[pos] = 1
                f.write("MOV" + " " + item[1] + " R" + str(pos) + "\n")
                if isVisisted(item[2]) == -1:
                    if item[0] == "+":
                        f.write("ADD" + " " + item[2] + " R" + str(pos) + "\n")
                    elif item[0] == "-":
                        f.write("SUB" + " " + item[2] + " R" + str(pos) + "\n")
                    elif item[0] == "*":
                        f.write("MUL" + " " + item[2] + " R" + str(pos) + "\n")
                    elif item[0] == "/":
                        f.write("DIV" + " " + item[2] + " R" + str(pos) + "\n")
                    usedVal[pos] = item[3]

                else:
                    pos2 = isVisisted(item[2])
                    if item[0] == "+":
                        f.write("ADD" + " " + "R" + str(pos) + " R" + str(pos2) + "\n")
                    elif item[0] == "-":
                        f.write("SUB" + " " + "R" + str(pos)  + " R" + str(pos2) + "\n")
                    elif item[0] == "*":
                        f.write("MUL" + " " + "R" + str(pos)  + " R" + str(pos2) + "\n")
                    elif item[0] == "/":
                        f.write("DIV" + " " + "R" + str(pos)  + " R" + str(pos2) + "\n")
                    usedVal[pos2] = item[3]
            else:
                pos = isVisisted(item[1])
                if isVisisted(item[2]) == -1:
                    if item[0] == "+":
                        f.write("ADD" + " " + item[1] + " R" + str(pos) + "\n")
                    elif item[0] == "-":
                        f.write("SUB" + " " + item[1]   + " R" + str(pos) + "\n")
                    elif item[0] == "*":
                        f.write("MUL" + " " + item[1]   + " R" + str(pos) + "\n")
                    elif item[0] == "/":
                        f.write("DIV" + " " + item[1]   + " R" + str(pos) + "\n")
                    usedVal[pos] = item[3]

                else:
                    pos2 = isVisisted(item[2])
                    if item[0] == "+":
                        f.write("ADD" + " " + "R" + str(pos) + " R" + str(pos2) + "\n")
                    elif item[0] == "-":
                        f.write("SUB" + " " + "R" + str(pos)  + " R" + str(pos2) + "\n")
                    elif item[0] == "*":
                        f.write("MUL" + " " + "R" + str(pos)  + " R" + str(pos2) + "\n")
                    elif item[0] == "/":
                        f.write("DIV" + " " + "R" + str(pos)  + " R" + str(pos2) + "\n")
                    usedVal[pos2] = item[3]
        else:
            if isVisisted(item[1]):
                pos = isVisisted(item[1])
            
            else:
                pos = giveReg()
                registers[pos] = 1
                usedVal[pos] = item[2]
            f.write("MOV" + " " + "R" + str(pos) + " " + item[2])
            


                    

