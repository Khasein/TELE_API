from bs4 import BeautifulSoup as BS  # pip3 install beautifulsoup
import requests  # pip3 install requests

r = requests.get("https://www.banki.ru/products/currency/cb/")
html = BS(r.content, 'html.parser')

dlr_find = html.find('table', class_="standard-table standard-table--row-highlight").find('tbody').find('tr').text
dlr = dlr_find.split()

eur_find = html.find('table', class_="standard-table standard-table--row-highlight").text
eur = eur_find.split()
EURO = eur[13:18]
AUD = eur[18:24]
AZN = eur[24:30]
AMD = eur[30:36]
BYN = eur[36:42]
BGN = eur[42:48]
BRL = eur[48:54]
HUF = eur[54:60]
KRW = eur[60:67]
HKD = eur[67:73]
DKK = eur[73:79]
INR = eur[79:85]
KZT = eur[85:91]
CAD = eur[91:97]
KGS = eur[97:103]
CNY = eur[103:109]
MDL = eur[109:115]
RON = eur[115:121]
TMT = eur[122:129]
NOK = eur[129:135]
PLN = eur[135:141]
SGD = eur[149:155]
TJS = eur[155:161]
TRY = eur[161:167]
UZS = eur[167:173]
UAH = eur[173:179]
GBP = eur[179:187]
CZK = eur[187:193]
SEK = eur[193:199]
CHF = eur[199:205]
ZAR = eur[205:211]
JPY = eur[211:217]

# print(EURO, AUD, AZN, AMD, BYN, BGN, BRL, HUF, KRW, HKD, DKK, INR, KZT, CAD, KGS, CNY, MDL, RON, TMT, NOK, PLN, SGD,
#      TJS, TRY, UZS, UAH, GBP, CZK, SEK, CHF, ZAR, JPY, sep="\n")

usd = f'{dlr[2]} = {dlr[4]}'
euro = f'{EURO[2]} = {EURO[3]}'
amd = f'{AMD[1]} {AMD[2]} {AUD[3]} = {AUD[4]}'
aud = f'{AUD[2]} {AUD[3]} = {AUD[4]}'
byn = f'{BYN[2]} {BYN[3]} = {BYN[4]}'
bgn = f'{BGN[2]} {BGN[3]} = {BGN[4]}'
brl = f'{BRL[2]} {BRL[3]} = {BRL[4]}'
huf = f'{HUF[1]} {HUF[2]} {HUF[3]} = {HUF[4]}'
krw = f'{KRW[1]} {KRW[2]} {KRW[3]} = {KRW[4]}'
hkd = f'{HKD[1]} {HKD[2]} {HKD[3]} = {HKD[4]}'
dkk = f'{DKK[1]} {DKK[2]} {DKK[3]} = {DKK[4]}'
inr = f'{INR[1]} {INR[2]} {INR[3]} = {INR[4]}'
kzt = f'{KZT[1]} {KZT[2]} {KZT[3]} = {KZT[4]}'
cad = f'{CAD[2]} {CAD[3]} = {CAD[4]} '
kgs = f'{KGS[1]} {KGS[2]} {KGS[3]} = {KGS[4]}'
cny = f'{CNY[1]} {CNY[2]} {CNY[3]} = {CNY[4]}'
mdl = f'{MDL[1]} {MDL[2]} {MDL[3]} = {MDL[4]}'
ron = f'{RON[2]} {RON[3]} {RON[4]} = {RON[5]}'
tmt = f'{TMT[2]} {TMT[3]} {TMT[4]} = {TMT[5]}'
nok = f'{NOK[1]} {NOK[2]} {NOK[3]} = {NOK[4]}'
pln = f'{PLN[2]} {PLN[3]} = {PLN[4]}'
sgd = f'{SGD[2]} {SGD[3]} = {SGD[4]}'
tjs = f'{TJS[1]} {TJS[2]} {TJS[3]} = {TJS[4]}'
trry = f'{TRY[1]} {TRY[2]} {TRY[3]} = {TRY[4]}'
uzs = f'{UZS[1]} {UZS[2]} {UZS[3]} = {UZS[4]}'
uah = f'{UAH[1]} {UAH[2]} {UAH[3]} = {UAH[4]}'
gbp = f'{GBP[1]} {GBP[2]} {GBP[3]} {GBP[4]} {GBP[5]} = {GBP[6]}'
czk = f'{CZK[1]} {CZK[2]} {CZK[3]} = {CZK[4]}'
sek = f'{SEK[1]} {SEK[2]} {SEK[3]} = {SEK[4]}'
chf = f'{CHF[2]} {CHF[3]} = {CHF[4]}'
zar = f'{ZAR[1]} {ZAR[2]} {ZAR[3]} = {ZAR[4]}'
jpy = f'{JPY[1]} {JPY[2]} {JPY[3]} = {JPY[4]}'
