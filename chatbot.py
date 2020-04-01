import requests,sys,re,os,time
if sys.version[0] == "2":
   input=raw_input
url_encoding={" ":"%20",
"!":"%21",
'"':'%22',
"#":"%23",
"$":"%24",
"%":"%25",
"&":"%26",
"'":"%27",
"(":"%28",
")":"%29",
"*":"%2A",
"+":"%2B",
",":"%2C",
"-":"%D",
".":"%E",
"/":"%F",
}
os.system("clear")
print ("Youtube : JustA Hacker")
time.sleep(10)
os.system("clear")
while True:
   ask = input("\x1b[1;32mYou : ")
   for i in url_encoding:
       ask=ask.replace(i,url_encoding[i])
   url="https://secureapp.simsimi.com/v1/simsimi/talkset?uid=287126054&av=6.8.9.4&lc=id&cc=&tz=Asia%2FJakarta&os=a&ak=pNfLbeQT%2B0cnFY8YHQb7CNHowpg%3D&message_sentence={}&normalProb=8&isFilter=1&talkCnt=2&talkCntTotal=2&reqFilter=1&session=XZzaduTVCSqa6vMtuyFhGv9eCXiyWwKJVETZjpQjc2oLPGBN2XtpzcKRFhLukHd6EAYVWMiSGuPzQV5Vwcdmwz14&triggerKeywords=%5B%5D".format(ask)
   jwb=requests.get(url).text
   print ("\x1b[1;33mBot : "+re.search(r'"origin_answerSentence":"(.*?)"',jwb).group(1))
