mnt = {'INCR': 1}
mdt = {1: ['AR  2,3', 'MR  1,2', 'ST  1,2']}

mout =  open("macro_out.asm", 'w')
with open("macro.asm", 'r') as f:
    contents = f.read().splitlines()
    out = contents
    macro_loc = []
    for x, line in enumerate(contents):
        #Remove macro definitions from the input
        if not line.find("MACRO") == -1:
            while contents[x].find("MEND") == -1:
                data =  contents[x]
                mout.write(data + "\n")
                contents.pop(x)
            data =  contents[x]
            mout.write(data + "\n")
            contents.pop(x)
        
        #Replace macro calls with code in the contents

        elif line.split(" ")[0] in mnt.keys():
            for keys in mnt:
                if not line.find(keys) == -1:
                    macro_code = mdt[mnt[keys]][:]
                    print macro_code
                    y = x + 1
                    contents.pop(x)
                    contents.insert(x, macro_code[0])
                    mout.write(contents[x] + "\n")
                    macro_code.pop(0)
                    print macro_code
                    for ins in macro_code:
                        print ins
                        contents.insert(y, ins)
                        y += 1
        else:   
            mout.write(contents[x] + "\n")           


           

    print(contents)