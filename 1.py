from string import maketrans

alpha = maketrans("", "")[97:123]
combin = list(alpha*2)
lista = combin[2:28]
fake = ''.join(lista)
faketable = maketrans(alpha, fake)
string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print string.translate(faketable)