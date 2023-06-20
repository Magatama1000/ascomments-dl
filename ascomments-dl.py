import asyncio
import websockets
import sys
import re
import os

count = 10000

args = sys.argv
pageurl = args[1]

def extract_info_from_url(pageurl):
    pattern = r"https://asobistage.asobistore.jp/event/([^/]+)/archive/([^/]+)"
    match = re.match(pattern, pageurl)
    if match:
        eventname = match.group(1)
        day = match.group(2)
        return eventname, day
    else:
        raise ValueError("Invalid URL format\nUsage:ascomments-dl [ASOBISTAGE LIVE Archive Page URL]")

async def download():
    print("Connecting comment server (archive) via WebSocket...")
    async with websockets.connect(uri) as websocket:
        await websocket.recv()
        nonecount=0
        for i in range(count):
            sendtxt="{\"func\":\"archive-get\",\"time\":\""+str(5*i)+"\"}"
            await websocket.send(sendtxt)
            comment=await websocket.recv()
            comment_nakami=comment[12:-2]

            if i>0 and len(comment_nakami)!=0:
                f.write(",")

            f.write(str(comment_nakami))

            

            if len(comment_nakami)==0:
                nonecount=nonecount+1
            else:
                nonecount=0
            if nonecount>19:
                break

            print("Downloading... Count:",i,"Sending:",sendtxt,"Empty:",nonecount, end="\r", flush=True)

        print()
        print("Closing and Saving...")

print("This is a software that downloads comments from ASOBISTAGE's broadcast live archives.")
print("The page URL is ",pageurl)
eventname, day = extract_info_from_url(pageurl)
uri = "wss://replay.asobistore.jp/"+eventname+"_"+day+"_ch1/archive"

print("Downloading from ",uri)

filename=eventname+"_"+day+"_comments.json"

if os.path.exists(filename):
    overwrite = input("File already exists. Do you want to overwrite it? (y/N): ")
    if overwrite.lower() == "y":
        print("Overwriting", filename)
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write("[")
            asyncio.run(download())
            f.write("]")
    else:
        print("File not overwritten.")
else:
    print("Saving into", filename)
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write("[")
        asyncio.run(download())
        f.write("]")