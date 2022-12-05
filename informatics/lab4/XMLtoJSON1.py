iv = 0
def XMLtoJSON():
    f = open("data.xml",encoding = "utf-8")
    f = f.read()
    if '<?xml version="1.0" encoding="UTF-8"?>' in f:
        f = f.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
    isName = False
    isData = False
    name = ""
    datal = ""
    data = []
    names = []

    for i in range(len(f)):
        if isData:
            datal += f[i]
        if f[i] == ">":
            isName = False
            isData = True
            names.append(name)
            name = ""
        if f[i] == "<":
            isData = False
            data.append(datal[:-1])
            datal = ""
        if f[i-1] == "<" and f[i] != "/":  
            isName = True
        if isName:
            name += f[i]
    newData = []
    for i in data:
        if i.replace("\n","").replace(" ","") == "":
            newData.append("")
        else:
            newData.append(i)
    data = newData
    def parse(s):
        global iv
        if iv < len(names):
            while names[iv] != "":
                iv+=1
                s.append(parse([names[iv-1],data[iv]]))
            else:
                if iv == len(names)-1:
                    return s
                iv += 1
        return s
    p = parse([])[0]
    def toJSON(s,h,deep,isLast):
        s += "    "*deep + '"' + h[0] + '": '
        if len(h) == 2:
            s += '"' + h[1] + '"'
        else:
            s += "{\n"
            isLastLoc = False
            for i in range(2,len(h)):
                if len(h)-1 == i:
                    isLastLoc = True
                s += toJSON("",h[i],deep+1,isLastLoc)
            s += "    "*deep + "}"
        if not isLast:
            s+=",\n"
        if isLast:
            s+="\n"
        return s
    #print(toJSON("{\n",p,1,True)+"}")
    global iv
    iv = 0