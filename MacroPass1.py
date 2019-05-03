mnt = {}

mdt = {}

with open("macro.asm", 'r') as f:
    contents = f.read().splitlines()
    count = 1
    for x, line in enumerate(contents):
        # print x, lines
        y = x
        if not line.find("MACRO") == -1:
            print "Found Marco Definition at: ", x
            y += 1
            mnt[contents[y]] = count
            macro_stmt = []
            while not contents[y].find("MEND") == -1:
                macro_stmt.append(contents[y])
                y += 1
            mdt[count] = macro_stmt
            count += 1

print mnt
print mdt