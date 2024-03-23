# -*- coding: utf-8 -*-
from linepy import *
from token import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import*
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import  pafy, tweepy, wikipedia, time, timeit, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib3.connection, urllib.parse,antolib,subprocess,unicodedata,GACSender
_session = requests.session()
#from gtts import gTTS
from googletrans import Translator
import youtube_dl
import requests
from pafy import new
from urllib.parse import urlencode
#==============================================================================#
botStart = time.time()
#================EvVcY4Nk9hKiJZYdRMW3.TAVOkm2wqPizxdXz1JiGmW.4QUmFeBLiOjPKtdV7+ddmEw6IuVk/aIHke+OWKLmu/Q===============================================================#
line = LINE()
#line = LINE('')
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(lin.tl.channelAccessToken))

print ("✯͜͡𝔪𝔞𝔡𝔞𝔪𝔨𝔢𝔢 𝔰𝔢𝔩𝔣𝔟𝔬𝔱❂✯͜͡✯͜͡𝔬𝔫𝔩𝔦𝔫𝔢")

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()
zxcv = lineMID
oepoll = OEPoll(line)
#call = Call(line)

Rfu = [line]
Exc = [line]
lineMID = line.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID]
Family=["u6d443c0753fcf1af5bcf6ea9b01c776a",lineMID]
admin=['u6d443c0753fcf1af5bcf6ea9b01c776a',lineMID]
adminMID="u6d443c0753fcf1af5bcf6ea9b01c776a"
RfuFamily = RfuBot + Family
msg_dict = {}
msg_image={}
msg_video={}
msg_sticker={}
unsendchat = {}
temp_flood = {}
wbanlist = []
wblacklist = []
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
tokenz = {}
setback = ()
#==============================================================================#

settings = {
    "autoAdd": False,
    "autoBlock": True,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":10},	
    "autoLeave": False,
    "autoRead": False,
    "autoReply": False,
    "botcancel": False,
    "leaveRoom": False,
    "detectMention": False,
    "checkSticker": False,
    "checkContact": False,
 False,
    "checkPost": False,
    "kickMention": False,
    "potoMention": True,
    "delayMention": False,
    "lang":"JP",
    "Wc": True,
    "Lv": True,
    "Nk": True,
    "Api": True,
    "Aip": True,
    "selfbot": True,
    "blacklist":{},
    "wbanlist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "detectMentionPM": False,
    "dwhitelist": False,
    "gift": {},
    "likeOn": True,
    "autolike": True,
    "comment": "Autolike by SELFBOT-BY:MAX 🕵",
    "timeline": False,
    "commentOn":True,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "changeGroupPicture": [],
    "changePictureProfile": False,
    "changeProfileVideo": False,
    "kickContact": False,
    "changeVideo": False,
    "chatMessage": "dih",
    "unsendMessage": False,
    "autoJoinTicket": False,
    "welcome":"คุณยังไม่ได้ตั้งข้อความคนเข้า",
    "kick":"คุณยังไม่ได้ตั้งข้อความคนลบ",
    "bye":"คุณยังไม่ได้ตั้งข้อความคนออก",
    "Respontag":"สำหรับคนสำคัญ ยากแค่ไหนก้จะทำ 🕵",
    "eror":"คุณใช้คำสั่งผิด กรุณาศึกษาวิธีใช้ หรือสอบถามกับผู้สร้าง โดยพิมคำสั่ง *.ผส*เพื่อแสดง คท ของผู้สร้าง",
    "spam":{},
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "notag": False,
    "pcancel": False,
    "pinvite": False,
    "pmMessage": "ว่างเดื้ยวเห็นข้อความจะมาตอบนะ",
    "qrp": False,
    "readerPesan": " แอบทมายเดะจิ้มตาบอด",
    "replyPesan": "Sorry , i'm busy right now.",
    "responGc": True,
    "responcall": False,
    "responcallgc": False,
    "restartPoint": "c07540238e0ddffa5187313406f7f3c67",
    "server": "VPS",
    "ksticker": False,
    "userMentioned": False,
    "timeRestart": "18000",
    "message1":"🕵  [ 𝓑𝔂 ] 𝖒𝖆𝖉𝖆𝖒𝖐𝖊𝖊 𝖘𝖊𝖑𝖋𝖇𝖔𝖙🕵",
    "message":"🕵 [ 𝓑𝔂 ] 𝖒𝖆𝖉𝖆𝖒𝖐𝖊𝖊 𝖘𝖊𝖑𝖋𝖇𝖔𝖙 🕵",
#    "comment":"""🕵 [ 𝓑𝔂 ] 𝖒𝖆𝖉𝖆𝖒𝖐𝖊𝖊 𝖘𝖊𝖑𝖋𝖇𝖔𝖙🕵""",
    "comment1":"""🕵 [ 𝓑𝔂 ] 𝖒𝖆𝖉𝖆𝖒𝖐𝖊𝖊 𝖘𝖊𝖑𝖋𝖇𝖔𝖙🕵""",
"userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "addPesan": "🙏สวัสดีครับ🙏เพื่อนใหม่\n👉สนใจทำเซลบอท แก้ไฟลเซล เพิ่มไฟลเซล สอนทำเซล กด1\n👉สนใจทำปก ทำดิส กด2\n👉สนใจสั่งตั๋วสิริ ลงบอทสิริ บอทapi กด3\n👉สนใจเช่าเซิฟ Vps กด4\n👉สนใจสั่งซื้อสติ๊กเกอร์ ทีมไลน์ กด5\n👉แอดมาเก็บคท กด6\n👉แอดแล้วไม่พูดไม่ทัก กดบล็อค\n👉แต่ถ้าทักแล้วไม่ตอบ. หรือตอบช้า โทรมาเบอร์นี้เลยคับ 094 634 5913 @!",
    "addSticker": {
        "name": "",
        "status": False,
    },
    "mentionPesan": " ว่าไง? ที่รัก􀄃􀈻",
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "addSticker": {
                "STKID": "409",
                "STKPKGID": "1",
                "STKVER": "100"
            },
            "leaveSticker": {
                "STKID": "51626533",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "kickSticker": {
                "STKID": "123",
                "STKPKGID": "1",
                "STKVER": "100"
            },
            "readerSticker": {
                "STKID": "51626530",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "responSticker": {
                "STKID": "52002738",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "sleepSticker": "",
            "welcomeSticker": {
                "STKID": "51626527",
                "STKPKGID": "11538",
                "STKVER": "1"
            }
        }
    },
    "mimic": {
       "copy": False,
       "status": False,
       "target": {}
    }
}
