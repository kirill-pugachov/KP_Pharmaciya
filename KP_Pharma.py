# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import time
import json



pause = 120
file_path = 'C:/Users/Кирилл/Documents/MDM/Компендиум/Геоаптека/Аптека КП Фармация/famac104.json'
url_to_send = 'https://skynet.morion.ua/data/add?key=sysdba'
headers = {'content-type':'application/json; charset=utf-8; hashtag=data.geostore', 'Content-Encoding':'gzip', 'Connection':'close'}
data = {
"Meta":{
"Code":"23",
"Head":"КП Фармация",
"Name":"Аптека №001, Володимирська, 51/ 53",
"Addr":"01034, м.Київ, вул.Володимирська, 51/ 53",
"EGRPOU":"05415852",
"DateTimeZone":"24.10.2016 17:33:16",
"Version":"1",
"Agent":"1С.БР"
},
"Data":[
{
"Code":"001752",
"Name":"Спринцівка т. А-16(700мл) КУ(ПДВ) Альпіна-пласт ТОВ Росія",
"Desc":"",
"Addr":"",
"Price":117.05,
"Price_cntr":120.05,
"Quant":50
},
{
"Code":"001753",
"Name":"Спринцівка т. Б-13(483мл) КУ(ПДВ) Альпіна-пласт ТОВ Росія",
"Desc":"",
"Addr":"",
"Price":102.55,
"Price_cntr":99.55,
"Quant":50
},
{
"Code":"001754",
"Name":"Спринцівка т. А-13(317мл) КУ(ПДВ) Альпіна-пласт ТОВ Росія",
"Desc":"",
"Addr":"",
"Price":81.65,
"Price_cntr":81.65,
"Quant":50
},
{
"Code":"F03045",
"Name":"Деквадол таб. д/розсмокт. №18 Київський вітамінний з-д ПАТ м.Київ",
"Desc":"",
"Addr":"",
"Price":59.15,
"Price_cntr":64.15,
"Quant":50
},
{
"Code":"F03046",
"Name":"Деквадол таб. д/розсмокт. №30 Київський вітамінний з-д ПАТ м.Київ",
"Desc":"",
"Addr":"",
"Price":96.55,
"Price_cntr":106.55,
"Quant":50
},
{
"Code":"F01647",
"Name":"Нурофєн експрес форте капс. м\"які 400мг №10 ** Реккітт Бенкізер Хелскер Інтернешнл Лімітед Велика Британія",
"Desc":"",
"Addr":"",
"Price":105.435,
"Price_cntr":105.435,
"Quant":50
},
{
"Code":"F01472",
"Name":"Нурофєн д/дит. форте сусп. полунич. 200мг/5мл 100мл ** Реккітт Бенкізер Хелскер (ЮКей) Лімітед Велика Британія",
"Desc":"",
"Addr":"",
"Price":98.65,
"Price_cntr":108.65,
"Quant":50
},
{
"Code":"003428",
"Name":"Нурофєн експрес таб. в/о 200мг №12 ** Реккітт Бенкізер Хелскер Інтернешнл Лімітед Велика Британія",
"Desc":"",
"Addr":"",
"Price":78.57,
"Price_cntr":70.65,
"Quant":50
}
]}

#files = {'file': open(file_path,'rb')}
while True:
    res = requests.post(url_to_send, headers=headers, data=data, verify=False)
#    res = requests.post(url_to_send, headers=headers, files=files, verify=False)
    print(res.status_code)
    print(res.headers)
    print(res.text)
    for i in range(pause):
        time.sleep(1)

    