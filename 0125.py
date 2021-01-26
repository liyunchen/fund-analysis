# -*- coding: utf-8 -*-
import json
import requests

def test1():
    code = 161725
    size = 365
    url = "https://danjuanapp.com/djapi/fund/nav/history/"+str(code)+"?size="+str(size)+"&page=1"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
              }
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    s = json.loads(res.text)
    s = s['data']['items']
    f = ((s[len(s)-1]['date']).split("-"))[1]

    for j in range(len(s)-1,-1,-1):
        i = s[j]
        m = (i['date'].split("-"))
        if m[1] == f:
            try:
                date = i['date']
                percentage = i['percentage']
                value = i['value']
                print("date=" + str(date) + ",percentage=" + str(percentage) + ",value=" + str(value))
            except:
                pass
        else:
            f = m[1]
            try:
                date = i['date']
                percentage = i['percentage']
                value = i['value']
                print("date=" + str(date) + ",percentage=" + str(percentage) + ",value=" + str(value))
            except:
                pass
            print("---------------")

def test():

    code = 161725
    size = 365
    url = "https://danjuanapp.com/djapi/fund/nav/history/"+str(code)+"?size="+str(size)+"&page=1"


    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
              }

    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    s = json.loads(res.text)
    s = s['data']['items']
    f = ((s[len(s)-1]['date']).split("-"))[1]
    print("月份=" + str(((s[len(s)-1]['date']).split("-"))[0]+"-"+((s[len(s)-1]['date']).split("-"))[1]))
    max=float(s[len(s)-1]['percentage'])
    min =float(1000)
    start=s[len(s)-1]['value']
    end=0

    maxlist=[]
    minlist=[]
    startlist=[]
    endlist=[]
    reslist=[]
    mlist=[]
    mlist.append(str(((s[len(s)-1]['date']).split("-"))[0]+"-"+((s[len(s)-1]['date']).split("-"))[1]))

    for j in range(len(s)-1,-1,-1):
            i = s[j]

            m = (i['date'].split("-"))
            if m[1] ==f:

                if float(i['percentage']) > float(max):
                    max = float(i['percentage'])
                if float(i['percentage']) < float(min):
                    min = float(i['percentage'])
                if j!=0 and ((s[j-1]['date']).split("-"))[1]!=f:
                    end = i['value']
                # try:
                #     date = i['date']
                #     percentage = i['percentage']
                #     value = i['value']
                #     print("date="+str(date)+",percentage="+str(percentage)+",value="+str(value))
                # except:
                #     pass
            else:
                print("max="+str(max)+",min="+str(min))
                maxlist.append(float(str(max)))
                minlist.append(float(str(min)))
                max=float(0)
                min=float(1000)
                print("start="+str(start)+",end="+str(end)+",差值="+str(round(float(end)-float(start),4)))
                startlist.append(float(str(start)))
                endlist.append(float(str(end)))
                reslist.append(float(str(round(float(end)-float(start),4))))
                f = m[1]

                start = i['value']
                #max = i['value']
                #max=0
                print("---------------")
                print("月份="+str(m[0]+"-"+m[1]))
                mlist.append(str(m[0]+"-"+m[1]))
                # try:
                #     date = i['date']
                #     percentage = i['percentage']
                #     value = i['value']
                #     print("date="+str(date)+",percentage="+str(percentage)+",value="+str(value))
                # except:
                #     pass
            if j==0:
                print("max="+str(max)+",min="+str(min))
                maxlist.append(float(str(max)))
                minlist.append(float(str(min)))
                print("start=" + str(start) + ",end=" + s[j]['value']+",差值="+str(round(float(s[j]['value'])-float(start),4)))
                startlist.append(float(str(start)))
                endlist.append(float(s[j]['value']))
                reslist.append(float(str(round(float(s[j]['value'])-float(start),4))))


    #print(maxlist)
    #print(minlist)
    #print(startlist)
    #print(endlist)
    print(reslist)
    print(mlist)
    ###1.月初、月末
    #analysis1(mlist,startlist,endlist)
    ###2.当月最高涨、最低跌
    #analysis2(mlist, maxlist, minlist)
    ###3.当月波动值（最高涨、最低跌之差）
    #analysis3(mlist, maxlist, minlist)
    ###4.月差值(月末减月初，该月是否盈亏）
    #analysis4(mlist, reslist)


# 绘制多个条形图
from matplotlib import pyplot as plt
from matplotlib import font_manager

###4.月差值(月末减月初，该月是否盈亏）
def analysis4(x,y):
    myfont = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simhei.ttf")

    # 设置图形大小
    plt.figure(figsize=(20, 8), dpi=80)
    plt.plot(x,y, label="月末-月初")

    # 设置图例
    plt.legend(prop=myfont)
    plt.xlabel("月份", fontproperties=myfont)
    plt.ylabel("值", fontproperties=myfont)
    plt.savefig("./mutiy.png")
    plt.show()

###3.当月波动值（最高涨、最低跌之差）
def analysis3(x,y1,y2):
    myfont = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simhei.ttf")
    a=x
    y=[]
    for i in range(0,len(y1)):
        y.append(float(y1[i]-y2[i]))
    # 设置图形大小
    plt.figure(figsize=(20, 8), dpi=80)
    plt.plot(a,y, label="波动差值")

    # 设置图例
    plt.legend(prop=myfont)
    plt.xlabel("月份", fontproperties=myfont)
    plt.ylabel("值", fontproperties=myfont)
    plt.savefig("./mutiy.png")
    plt.show()

###2.当月最高涨、最低跌
def analysis2(x,y1,y2):
    myfont = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simhei.ttf")
    a=x
    b_14=y1
    b_15=y2

    bar_width = 0.25
    x_14 = list(range(len(a)))
    x_15 = list(i + bar_width for i in x_14)

    # 设置图形大小
    plt.figure(figsize=(20, 8), dpi=80)
    plt.bar(range(len(a)), b_14, width=bar_width, label="当月最高涨")
    plt.bar(x_15, b_15, width=bar_width, label="当月最低跌")

    # 设置图例
    plt.legend(prop=myfont)
    #
    plt.xlabel("月份",fontproperties=myfont)
    plt.ylabel("值",fontproperties=myfont)
    # 设置x轴刻度
    plt.xticks(x_15, a, fontproperties=myfont)
    plt.savefig("./mutiy.png")
    plt.show()

###1.月初、月末
def analysis1(x,y1,y2):
    myfont = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simhei.ttf")
    a=x
    b_14=y1
    b_15=y2

    bar_width = 0.25
    x_14 = list(range(len(a)))
    x_15 = list(i + bar_width for i in x_14)

    # 设置图形大小
    plt.figure(figsize=(20, 8), dpi=80)
    plt.bar(range(len(a)), b_14, width=bar_width, label="月初")
    plt.bar(x_15, b_15, width=bar_width, label="月末")

    # 设置图例
    plt.legend(prop=myfont)
    #
    plt.xlabel("月份",fontproperties=myfont)
    plt.ylabel("值",fontproperties=myfont)
    # 设置x轴刻度
    plt.xticks(x_15, a, fontproperties=myfont)
    plt.savefig("./mutiy.png")
    plt.show()



if __name__ == '__main__':

    test()


