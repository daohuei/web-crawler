import re
import _io
postnum = 1
global f
kwrd = list()
totalweight = 0
gradecomparelist = list()
while True:
    k = input('Input Keyword:')
    w = input('Input weight of keyword:')
    if k != '':
        kwrd.append([k, w])
        totalweight += int(w)
    else:
        break
while True:
    try:
        f = open('Post'+str(postnum)+'.txt', 'r')
    except FileNotFoundError:
        break
    text = f.read()
    postdata = list()
    l = text.split("----------------")
    n = 0
    for i in l:
        if i != l[0]:
            popdata = ['', '', '', '']
            allcon = ['', '', '']
            t1 = i.split("Post Number:\n")
            t2 = t1[1].split("\nPost Likes Count:")
            pn = t2[0]
            t1 = i.split("Post Likes Count:\n")
            t2 = t1[1].split("\nPost Comments Count:")
            plc = t2[0]
            t1 = i.split("Post Comments Count:\n")
            t2 = t1[1].split("\nPost Shares Count:")
            pcc = t2[0]
            t1 = i.split("Post Shares Count:\n")
            t2 = t1[1].split("\nPopular Number:")
            psc = t2[0]
            t1 = i.split("Popular Number:\n")
            t2 = t1[1].split("\nLink of the Post:")
            popn = t2[0]
            popdata = [plc, pcc, psc, popn]
            t1 = i.split("Link of the Post:\n")
            t2 = t1[1].split("\nPost Content:")
            lp = t2[0]
            t1 = i.split("Post Content:\n")
            t2 = t1[1].split("\nPost Picture:")
            pcon = t2[0]
            t1 = i.split("Post Picture:\n")
            t2 = t1[1].split("\nShare Link:")
            t3 = t2[0].split("\n")
            ppic = list()
            for t3pic in t3:
                ppic.append(t3pic)
            t1 = i.split("Share Link:\n")
            t2 = t1[1].split("\nShare Link Content:")
            sl = t2[0]
            t1 = i.split("Share Link Content:\n")
            t2 = t1[1].split("\nShare Post Content:")
            slcon = t2[0]
            t1 = i.split("Share Post Content:\n")
            t2 = t1[1].split("\nComments:")
            spcon = t2[0]
            allcon = [pcon, slcon, spcon]
            t1 = i.split("Comments:\n")
            t2 = t1[1].split("End of Post")
            commlist = t2[0].split("\n\n")
            an = ''
            al = ''
            comcon = ''
            comm = list()
            for commm in commlist:
                if commm != '':
                    co = commm.split("\n")
                    for c in co:
                        if 'Account:' in c:
                            an = c.split('Account:')[1]
                        if 'Account Link:' in c:
                            al = c.split('Account Link:')[1]
                        if 'Comment Content:' in c:
                            comcon = c.split('Comment Content:')[1]
                    comm.append([an, al, comcon])
            paralist = [pn, allcon, lp, sl, ppic, popdata, comm]
            postdata.append(paralist)
            n += 1

    ksinglecount = 0
    sortlist = list()
    for j in range(len(postdata)):
        teststr = ''
        for r in range(len(postdata[j][1])):
            teststr += postdata[j][1][r]
        for c in range(len(postdata[j][6])):
            teststr += postdata[j][6][c][2]
        kcount = 0
        for z in range(len(kwrd)):
            m = re.findall(kwrd[z][0], teststr, re.I)  # re.I is to ignore upper/lower cases
            kcount += (len(m) * int(kwrd[z][1]))
            if len(m) > 0:
                ksinglecount += int(kwrd[z][1])
        if kcount > 1:
            sortlist.append([postdata[j], kcount])
            # print('Post Number: '+postdata[j][0])
            # print('Mention '+str(len(m))+' times\n')

    y = 0
    for sort in sortlist:
        if y > 0:
            sort2 = sortlist[y]
            for u in range(y):
                sort1 = sortlist[y - u - 1]
                if sort2[1] > sort1[1]:
                    sortlist[y - u - 1] = sort2
                    sortlist[y - u] = sort1

                u += 1
        y += 1
    outputfile = open('HJLrelevance.txt', 'w')
    for sort in sortlist:
        print('Post Number: ' + sort[0][0])
        print('Post Link: ' + sort[0][2])
        print('Relevance Point: ' + str(sort[1]) + ' points\n')
        outputfile.write(sort[0][2] + '\n')
    print('Totally ' + str(y) + ' Data')
    gradestr = '0.0'
    try:
        gradestr = str(round((float(ksinglecount) / (float(len(postdata)) * float(totalweight)) * 100), 2))
    except ZeroDivisionError:
        pass
    print("Total Relevance of the Post: " + gradestr + "%")
    gradecomparelist.append(["Post"+str(postnum),float(gradestr)])
    f.close()
    postnum += 1
comparecount1 = 0
for gradecompare in gradecomparelist:
    if comparecount1 > 0:
        sort2 = gradecomparelist[comparecount1]
        for comparecount2 in range(comparecount1):
            sort1 = gradecomparelist[comparecount1 - comparecount2 - 1]
            if sort2[1] > sort1[1]:
                gradecomparelist[comparecount1 - comparecount2 - 1] = sort2
                gradecomparelist[comparecount1 - comparecount2] = sort1
            comparecount2 += 1
    comparecount1 += 1
m=1
for gradecompare in gradecomparelist:
    print(str(m)+". "+gradecompare[0]+": Relevance "+str(gradecompare[1])+" points")
    m+=1