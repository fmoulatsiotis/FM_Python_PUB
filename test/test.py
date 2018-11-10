s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
a1 = "abcdefghijklmnopqrstuvwxyz"

for c in s[:]:
    if c != ' ' and c != '.' and c != "'" and c != '(' and c != ')':
        x = a1.index(c)
        ## print(x, end=', ')
        x += 2
        ##print(x, end = '. ')
        c1 = a1[x:x + 1]
        print(c1, end = '')
print(s)
print(s)
str.maketrans()
