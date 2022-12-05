def XMLtoJSON():
    import xmltodict, json
    f = open("data.xml",encoding = "utf-8")
    f = f.read()
    o = xmltodict.parse(f)
    #print(json.dumps(o,sort_keys=False,indent = 4,ensure_ascii = False))