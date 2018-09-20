# !/usr/bin/env python
# -*- coding:utf:8 -*-

import re
import csv

csvfile = open("./C1-final.csv","w")
writer = csv.writer(csvfile)
writer.writerow(["id", "wos", "rank","author", "address"])
with open("C1-RP-AF.txt", "r", encoding="UTF-8") as f:
    id = 1
    af = []     # AF作者
    rp = []     # RP作者
    auaddr = {}     # C1：AF作者地址
    rpauaddr = {}   # RP作者地址
    optionflag = False
    line = f.readline()
    while line:
        if line.startswith("AF"):
            # 去掉Tag：AF后的作者姓名
            line = line.split(" ", 1)[-1]
            while True:
                if line.startswith("C1"):
                    break
                af.append(line.strip())
                line = f.readline()
        # 从C1中得到【作者-地址】字典
        while True:
            if '[' in line:
                author = re.search("\[.*\]", line).group()[1:-1].split(";")
                author = [a.strip() for a in author]
                addr = line.split(']')[-1].strip().split('.')[0]
                for a in author:
                    if a in auaddr:
                        auaddr[a] = auaddr[a]+ ";" + addr
                    else:
                        auaddr[a] = addr
            else:
                if not optionflag:
                    addrdefault = line.strip().split('.')[0]
                else:
                    addrdefault = addrdefault + ";" + line.strip().split('.')[0]
                optionflag = True
            line = f.readline()
            if line.startswith("RP") or line.startswith("UT"):
                break
        # 处理RP行
        if line.startswith("RP"):
            line = line.split(" ", 1)[-1][:-1]
            sp = line.split(".;")
            sp = [s.strip() for s in sp]
            for s in sp:
                rpAuthor = s.split("(", 1)[0].split(";")
                rpaddr = s.split("),")[-1].strip().split('.')[0]
                for a in rpAuthor:
                    a = a.strip()
                    if a not in rp:
                        rp.append(a)
                    if a not in rpauaddr.keys():
                        rpauaddr[a] = rpaddr
                    else:
                        rpauaddr[a] = rpauaddr[a] + ';' + rpaddr
            line = f.readline()
        # UT行： wos号
        wos = line.split(" ")[-1].strip()
        # 写入文件
        for i, author in enumerate(af):
            addr = auaddr[author] if author in auaddr.keys() else addrdefault if optionflag else "null"
            writer.writerow([id, wos, i+1, author, addr])
        for i, author in enumerate(rp):
            writer.writerow([id, wos, "RP" + '%02d' % (i + 1), author, rpauaddr[author] if author in rpauaddr.keys() else "null"])
        # 准备处理下一条信息
        id = id + 1
        af.clear()
        rp.clear()
        auaddr.clear()
        rpauaddr.clear()
        optionflag = False
        line = f.readline()
csvfile.close()






