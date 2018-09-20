# 读取原始文件，过滤无效行

# !/usr/bin/env python
# -*- coding:utf:8 -*-

tags = ("FN", "VR", "PT", "AU", "AF",
        "TI", "SO", "LA", "DT", "AB",
        "C1", "RP", "EM", "FU", "FX",
        "NR", "TC", "Z9", "U1", "U2",
        "PU", "PI", "PA", "SN", "EI",
        "J9", "JI", "PD", "PY", "VL",
        "IS", "BP", "EP", "DI", "PG",
        "WC", "SC", "GA", "UT", "ER",
        "DE", "PM", "RI", "OI", "DA",
        "OA", "AR", "HC", "HP")
needTags = ("AF", "C1", "UT", "RP")

f = open("./9-top.txt", 'r', encoding="UTF-8")
toFile = open("./C1-RP-AF.txt", "a")
flag = False
try:
    for line in f:
        if line.startswith(tags):
            if line.startswith(needTags):
                flag = True
            else:
                flag = False
        if flag:
            toFile.writelines(line)
finally:
    f.close()
    toFile.close()



