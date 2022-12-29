from aiogram import Bot, Dispatcher, types, executor  # pip3 install aiogram
from config2 import TOKEN_API  # This your BotFather Key
from dlr_info import *  # Parsing with banki.ru

bot = Bot(TOKEN_API)  # Put this your Token
dp = Dispatcher(bot)

commands_list = ''' 
/start - Bots started
/help - Commands lists
/all_rate - Show you All rates
'''
alls = f""""
{dlr[2]} = {dlr[4]}

{EURO[2]} = {EURO[3]}

{AUD[2]} {AUD[3]} = {AUD[4]}

{AMD[1]} {AMD[2]} {AUD[3]} = {AUD[4]}

{BYN[2]} {BYN[3]} = {BYN[4]}

{BGN[2]} {BGN[3]} = {BGN[4]}

{BRL[2]} {BRL[3]} = {BRL[4]}

{HUF[1]} {HUF[2]} {HUF[3]} = {HUF[4]}

{KRW[1]} {KRW[2]} {KRW[3]} = {KRW[4]}

{HKD[1]} {HKD[2]} {HKD[3]} = {HKD[4]}

{DKK[1]} {DKK[2]} {DKK[3]} = {DKK[4]}

{INR[1]} {INR[2]} {INR[3]} = {INR[4]}

{KZT[1]} {KZT[2]} {KZT[3]} = {KZT[4]}

{CAD[2]} {CAD[3]} = {CAD[4]}

{KGS[1]} {KGS[2]} {KGS[3]} = {KGS[4]}

{CNY[1]} {CNY[2]} {CNY[3]} = {CNY[4]}

{MDL[1]} {MDL[2]} {MDL[3]} = {MDL[4]}

{RON[2]} {RON[3]} {RON[4]} = {RON[5]}

{TMT[2]} {TMT[3]} {TMT[4]} = {TMT[5]}

{NOK[1]} {NOK[2]} {NOK[3]} = {NOK[4]}

{PLN[2]} {PLN[3]} = {PLN[4]}

{SGD[2]} {SGD[3]} = {SGD[4]}

{TJS[1]} {TJS[2]} {TJS[3]} = {TJS[4]}

{TRY[1]} {TRY[2]} {TRY[3]} = {TRY[4]}

{UZS[1]} {UZS[2]} {UZS[3]} = {UZS[4]}

{UAH[1]} {UAH[2]} {UAH[3]} = {UAH[4]}

{GBP[1]} {GBP[2]} {GBP[3]} {GBP[4]} {GBP[5]} = {GBP[6]}

{CZK[1]} {CZK[2]} {CZK[3]} = {CZK[4]}

{SEK[1]} {SEK[2]} {SEK[3]} = {SEK[4]}

{CHF[2]} {CHF[3]} = {CHF[4]}

{ZAR[1]} {ZAR[2]} {ZAR[3]} = {ZAR[4]}

{JPY[1]} {JPY[2]} {JPY[3]} = {JPY[4]}
"""  # all_rates info


@dp.message_handler(commands=['start'])
async def started(message: types.Message):
    await message.answer(text='Welcome to convert bot')
    await message.delete()


@dp.message_handler(commands=['help'])
async def started(message: types.Message):
    await message.answer(text=commands_list)
    await message.delete()


@dp.message_handler(commands=['all_rate'])
async def started(message: types.Message):
    await message.answer(text=alls)
    await message.delete()


# Next Decorator is info about Exchange Rates
@dp.message_handler(commands=['usd'])
async def started(message: types.Message):
    await message.answer(text=usd)
    await message.delete()


@dp.message_handler(commands=['euro'])
async def started(message: types.Message):
    await message.answer(text=euro)
    await message.delete()


@dp.message_handler(commands=['aud'])
async def started(message: types.Message):
    await message.answer(text=aud)
    await message.delete()


@dp.message_handler(commands=['amd'])
async def started(message: types.Message):
    await message.answer(text=amd)
    await message.delete()


@dp.message_handler(commands=['byn'])
async def started(message: types.Message):
    await message.answer(text=byn)
    await message.delete()


@dp.message_handler(commands=['bgn'])
async def started(message: types.Message):
    await message.answer(text=bgn)
    await message.delete()


@dp.message_handler(commands=['brl'])
async def started(message: types.Message):
    await message.answer(text=brl)
    await message.delete()


@dp.message_handler(commands=['huf'])
async def started(message: types.Message):
    await message.answer(text=huf)
    await message.delete()


@dp.message_handler(commands=['krw'])
async def started(message: types.Message):
    await message.answer(text=krw)
    await message.delete()


@dp.message_handler(commands=['inr'])
async def started(message: types.Message):
    await message.answer(text=inr)
    await message.delete()


@dp.message_handler(commands=['kzt'])
async def started(message: types.Message):
    await message.answer(text=kzt)
    await message.delete()


@dp.message_handler(commands=['cad'])
async def started(message: types.Message):
    await message.answer(text=cad)
    await message.delete()


@dp.message_handler(commands=['kgs'])
async def started(message: types.Message):
    await message.answer(text=kgs)
    await message.delete()


@dp.message_handler(commands=['cny'])
async def started(message: types.Message):
    await message.answer(text=cny)
    await message.delete()


@dp.message_handler(commands=['mdl'])
async def started(message: types.Message):
    await message.answer(text=mdl)
    await message.delete()


@dp.message_handler(commands=['ron'])
async def started(message: types.Message):
    await message.answer(text=ron)
    await message.delete()


@dp.message_handler(commands=['tmt'])
async def started(message: types.Message):
    await message.answer(text=tmt)
    await message.delete()


@dp.message_handler(commands=['nok'])
async def started(message: types.Message):
    await message.answer(text=nok)
    await message.delete()


@dp.message_handler(commands=['pln'])
async def started(message: types.Message):
    await message.answer(text=pln)
    await message.delete()


@dp.message_handler(commands=['sgd'])
async def started(message: types.Message):
    await message.answer(text=sgd)
    await message.delete()


@dp.message_handler(commands=['tjs'])
async def started(message: types.Message):
    await message.answer(text=tjs)
    await message.delete()


@dp.message_handler(commands=['try'])
async def started(message: types.Message):
    await message.answer(text=trry)
    await message.delete()


@dp.message_handler(commands=['uzs'])
async def started(message: types.Message):
    await message.answer(text=uzs)
    await message.delete()


@dp.message_handler(commands=['uah'])
async def started(message: types.Message):
    await message.answer(text=uah)
    await message.delete()


@dp.message_handler(commands=['gbp'])
async def started(message: types.Message):
    await message.answer(text=gbp)
    await message.delete()


@dp.message_handler(commands=['czk'])
async def started(message: types.Message):
    await message.answer(text=czk)
    await message.delete()


@dp.message_handler(commands=['sek'])
async def started(message: types.Message):
    await message.answer(text=sek)
    await message.delete()


@dp.message_handler(commands=['chf'])
async def started(message: types.Message):
    await message.answer(text=chf)
    await message.delete()


@dp.message_handler(commands=['zar'])
async def started(message: types.Message):
    await message.answer(text=zar)
    await message.delete()


@dp.message_handler(commands=['hkd'])
async def started(message: types.Message):
    await message.answer(text=hkd)
    await message.delete()


@dp.message_handler(commands=['jpy'])
async def started(message: types.Message):
    await message.answer(text=jpy)
    await message.delete()


if __name__ == '__main__':  # Need for launch Telegram API
    executor.start_polling(dp, skip_updates=True)
