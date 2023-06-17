import json
import sys
import datetime
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

print("Converting ASOBISTAGE comments json to niconico comments xml...")
args = sys.argv
filename=str(args[1])
json_file = open(filename, 'r', encoding='UTF-8')
f = open(filename+".xml", 'x', encoding='UTF-8')

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<packet>\n")

json_object = json.load(json_file)

for i in range(len(json_object)):
    f.write("<chat thread=\"\" no=\""+str(i+1)+"\" ")

    #vpos変換
    vpos=str(Decimal(str(float(json_object[i]['playtime'])*100)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
    f.write("vpos=\""+vpos+"\" ")

    #日時変換
    dte = datetime.datetime.strptime(str(json_object[i]['time'])[:-3], '%Y-%m-%d %H:%M:%S.%f')
    date=int(dte.timestamp())

    username=str(json_object[i]['data']['userName']).replace("\\u3000","　").replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("\"","&quot;").replace("\'","&apos;")

    f.write("date=\""+str(date)+"\" mail=\"184\" user_id=\"\" user_name=\""+username+"\" user_color=\""+str(json_object[i]['data']['color'])+"\" anonymity=\"1\" ")

    f.write("date_usec=\""+dte.strftime('%f')+"\">")

    f.write(str(json_object[i]['data']['comment'])[2:-2].replace("\\u3000","　").replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("\"","&quot;").replace("\'","&apos;"))
    f.write("</chat>\n")

f.write("</packet>")