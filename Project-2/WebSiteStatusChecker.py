import time as _time
from Consts import *
from datetime import datetime as _date
import schedule as _sch
import argparse as _parser
import requests as _req

parser = _parser.ArgumentParser(description="Website_Status_Checker")
subparser = parser.add_subparsers(dest="command",help="komutlar")

urlparser = subparser.add_parser("Checkuri",help="Her 5 saniyede bir kontrol edilecek bir URL verin")
urlparser.add_argument("uri",type=str,help="her 5 saniyede bir kontrol edilecek web sitesi bağlantısı")
txtparser = subparser.add_parser("Checktxt",help="txt dosyasındaki web sitesi bağlantıları her 5 saniyede bir kontrol eder")
txtparser.add_argument("path",type=str,help="Web sitesi bağlantılarını içeren bir txt dosyası verin ve her 5 saniyede bir kontrol yapın")
args = parser.parse_args()
listed = args._get_kwargs()

def LinkChecker(uri:str):
        if len(uri) >0 and uri.startswith("https://"):
            try:
                ans = _req.get(uri,timeout=OutTime)
                print(f"url:[{uri}],[{_date.now().strftime("%Y-%m-%d %H:%M:%S")}]"
                      ,f"🟢 Ok({ans.status_code})"if ans.status_code ==200 else f"🔴 DOWN ({ans.status_code}-{ans.reason})")
            except BaseException as err:
                print(f"url:[{uri}],[{_date.now().strftime("%Y-%m-%d %H:%M:%S")}]",f",🔴 DOWN({err.__class__.__name__})")
    

def CheckAlink(uri:str):
    LinkChecker(uri)


def CheckFileUri(filepath:str):
    if filepath.endswith(".txt"):
        with open(file=filepath,mode="r",encoding="utf-8") as fs:
            lines = fs.readlines()
            for line in lines:
                if(line.startswith("https://")):
                    LinkChecker(line)
            print("ends....")
            fs.close()


if(listed[0][1] =="Checkuri"):
    _sch.every(delay).seconds.do(CheckAlink,uri=args.uri)
elif(listed[0][1] =="Checktxt"):
    _sch.every(delay).seconds.do(CheckFileUri,filepath=args.path)       
else:
    _sch.cancel_job(CheckAlink)
    _sch.cancel_job(CheckFileUri)
        
while(True):
    _time.sleep(sleep)
    _sch.run_pending()