# coding:utf-8
import requests
import re
import concurrent.futures

nextnothing = '12345'
i = 0


def getcontent(path):
    try:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % path
        result = requests.get(url)
        a = re.compile("[\d{4}]")
        nextlist = a.findall(result.content)
        aa = ''.join(nextlist)
        return aa,result.content
    except:
        return


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    while nextnothing:
        aa = executor.submit(getcontent, nextnothing)
        nextnothing = aa.result()[0]
        i += 1
        print i
        print aa.result()[1]
    else:
        print "that's all"