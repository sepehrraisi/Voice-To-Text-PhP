#!/usr/bin/env python3

import speech_recognition as sr
import subprocess

def convert_and_split(filename):
    command = ['ffmpeg', '-i', filename, '-f', 'segment', '-segment_time', '15', '/var/www/html/Sadoos/out%09d.wav']
    subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)

convert_and_split("/var/www/html/Sadoos/audio.webm")
filename = "/var/www/html/Sadoos/out000000000.wav"
r = sr.Recognizer()
word = ["ضایعات", "وفاداری سازمانی", "کیفیت مواد", "مواد", "قطعات", "بی نظمی پرسنل", "مرجوعی", "کارگر", "نیروی انسانی", "راندمان", "بهره وری", "بهرهوری", "ضرر", "بازاریابی", "فروش", "صادرات", "تامین"]
word2 = ["مکانیک","قالب سازی","سوپر آلیاژ","وایرکات","قطعات خاص","صنایع","ضایعات","بهره وری","راندمان","فرایند","فرآیند","بهینه سازی","بازرگانی","توسعه بازار","فروش","رشد","سود","بازاریابی","مارکتینگ","تبلیغات","واردات","صادرات","زیان","بحران سیستمی","وفاداری سازمانی","بهره وری انسانی","نیروی کار","مدیریت","منابع انسانی","وفاداری سازمانی","وقت کشی","خطای انسانی"]
words = word + word2
words = list(set(words))
RS = []
RP = []
SSS = []
ST1 ="<a href=\"https://www.sid.ir/search/journal/paper/%D9%BE%D8%A7%D9%8A%D8%A7%D9%86%20%D9%86%D8%A7%D9%85%D9%87/fa?str=%d9%be%d8%a7%d9%8a%d8%a7%d9%86+%d9%86%d8%a7%d9%85%d9%87&page=1&sort=0&fgrp=all&ftyp=all&fyrs=1379%2c1402&stg="
ST2 = "\" class=\"button-64\" style=\"background-image: linear-gradient(144deg,#00DDEB, #5B42F3 50%, #26ff73);\">"
ST3 = "</a>"
str1 = ""
str2 = ""
S = ""
for i in RS:
    if i =="ضرر":
        RS.append("زیان")
    elif i =="خنس" | "خنسی":
        RS.append("بهران سیستمی")
    elif i =="ول میکنن":
        RS.append("وفاداری سازمانی")
    elif i =="تنبل":
        RS.append("بهره وری انسانی")
    else:
        RS.append(i)

mohammadi = ["مکانیک","قالب سازی","سوپر آلیاژ","وایرکات","قطعات خاص"]
hasanzadeh = ["صنایع","ضایعات","بهره وری","راندمان","فرایند","فرآیند","بهینه سازی"]
sajadiNaya = ["بازرگانی","توسعه بازار","فروش","رشد","سود","بازاریابی","مارکتینگ","تبلیغات","واردات","صادرات","زیان","بحران سیستمی","وفاداری سازمانی","بهره وری انسانی"]
hosseinpoor = ["نیروی کار","مدیریت","منابع انسانی","وفاداری سازمانی","وقت کشی","خطای انسانی"]
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data, language='fa-IR', show_all=False)
    print(text)
    for ts in words:
        print(ts)
        if ts in text: 
            print(ts)
            print("YAY")
            RS.append(ts)
            print(RS)
        if ts in mohammadi:
            RP.append("محمد محمدی")
        if ts in hasanzadeh:
            RP.append("حسن حسن زاده")
        if ts in sajadiNaya:
            RP.append("سجاد سجادی نیا")
        if ts in hosseinpoor:
            RP.append("حسین حسین پور")
    if RS == []:
        RS = ["مضوع مرتبط یافت نشد"]
    for ele in RS:
        str1 += " / "
        str1 += ele
        str1 += " / "
        S += ele
        S += " "
        S.replace(" ", "+")
    RP = list(set(RP))
    for ele in RP:
        str2 += " / "
        str2 += ele
        str2 += " / "
    link = "<a href=\""
    Site = "https://www.sid.ir/search/journal/paper/%D9%BE%D8%A7%D9%8A%D8%A7%D9%86%20%D9%86%D8%A7%D9%85%D9%87/fa?str=%d9%be%d8%a7%d9%8a%d8%a7%d9%86+%d9%86%d8%a7%d9%85%d9%87&page=1&sort=0&fgrp=all&ftyp=all&fyrs=1379%2c1402&stg="
    Site += S
    link += Site
    link += "\">لیست پایان نامه ها</a>"
    Sites = []
    for ele in RS:
        linki = ST1
        linki += ele
        linki += ST2
        linki += ele
        linki += ST3
        Sites.append(linki)
    with open('/var/www/html/Sadoos/Res.txt', 'w') as f:
        f.write(str1)
    with open('/var/www/html/Sadoos/Site.txt', 'w') as f:
        f.write(Site)
    with open('/var/www/html/Sadoos/Sites.txt', 'w') as f:
        for item in Sites:
        # write each item on a new line
            f.write("%s\n" % item)
    with open('/var/www/html/Sadoos/Amghezi.txt', 'w') as f:
        f.write(str2)
    