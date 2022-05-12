
import time
from logging import exception
from api_key import key, secret, passphrase
from kucoin.client import Market, Trade, User
market = Market()
trade = Trade(key, secret, passphrase, is_sandbox= False)
user = User(key, secret, passphrase, is_sandbox= False)

def ask_ask_bid(ask1, ask2, bid, alt, cash_usdt, fee, rate):
    if float(ask1) != 0 and float(ask2)!= 0 and float(bid) != 0:
        cash_btc = cash_usdt / float(ask1) # BTC_cash
        cash_alt = cash_btc / float(ask2) # ALT_cash
        cash = cash_alt * float(bid) # USDT_cash
        ret = ((cash - cash_usdt - 0.3) * 100 ) / cash_usdt
        if ret > rate:
            print("profit is find on: "+ alt)
            write_to_file("profit is predict on: "+ alt + "\n")
            
            id = None
            i = 0
            while id == None and i < 1:
                try:
                    tr = trade.create_market_order("BTC-USDT", side = 'buy', size = str(round(cash_btc, 4))) # step 1
                    print("step 1 has Done ... ... ...")
                    write_to_file("step 1 has Done ... ... ... buy: BTC-USDT" + "\n")
                    id = tr["orderId"]
                except BaseException as error:
                    print(error)
                    print("step 1 hasnot Done!")
                    write_to_file("step 1 hasnot Done!" + "\n")
                    write_to_file(str(error) + "\n")
                    i +=1

            id = None
            i = 0
            while id == None and i < 1:
                try:
                    tr = trade.create_market_order(f"{alt}-BTC", side = 'buy', size = str(round(cash_alt, 4))) #step 2
                    print("step 2 has Done ... ... ...")
                    write_to_file(f"step 2 has Done ... ... ... buy: {alt}-BTC" + "\n")
                    id = tr["orderId"]
                except BaseException as error:
                    print(error)
                    print("step 2 hasnot Done!")
                    write_to_file("step 2 hasnot Done!" + "\n")
                    write_to_file(str(error) + "\n")
                    i +=1

            id = None
            i = 0
            while id == None and i < 1:
                try:
                    tr = trade.create_market_order(f"{alt}-USDT", side = 'sell', size = str(round(cash_alt, 4))) # step 3
                    print("step 3 has Done ... ... ...")
                    write_to_file(f"step 3 has Done ... ... ... sell: {alt}-USDT" + "\n")
                    id = tr["orderId"]
                except BaseException as error:
                    print(error)
                    print("step 3 hasnot Done!")
                    write_to_file("step 3 hasnot Done!" + "\n")
                    write_to_file(str(error) + "\n")
                    #balance = user.get_account_list(f"{alt}", 'trade')
                    #write_to_file("alt_coin balance: " + str(balance[0]['available']) + "cash_alt is:" + str(cash_alt) + "\n")
                    i +=1

            write_to_file("BTC-USDT  ask: " + ask1 + "\n")
            write_to_file("ALT-BTC  ask: " + ask2 + "\n")
            write_to_file("ALT-USDT  bid: " + bid + "\n")
            write_to_file("USDT_amount: " + str(cash_usdt) + "\n" + "BTC_amount: " + str(cash_btc) + "\n" + "alt_amount: " + str(cash_alt) + "\n" + "USDT_cash: " + str(cash) + "\n")
            write_to_file("USDT-BTC-" + alt + "-USDT " + " predict: " + str(round(ret, 4)) + "\n" + "\n" + "\n")
            #time.sleep(600)
            
        
        output = "USDT-BTC-" + alt + "-USDT" + ": " + str(round(ret, 4))
        to_history(output + "\n")
        return output


def write_to_file(text):
    f = open("log_file.txt", "a")
    f.write(text)
    f.close()

def to_history(text):
    f = open("log_history.txt", "a")
    f.write(text)
    f.close()


def ask_bid_bid(ask1, bid2, bid, alt, cash_usdt, fee, rate):
    if float(ask1) != 0 and float(bid2)!= 0 and float(bid) != 0:
        cash_alt = cash_usdt / float(ask1) # ALT_cash
        cash_btc = cash_alt * float(bid2) # BTC_cash
        cash = cash_btc * float(bid) # USDT_cash
        ret = ((cash - cash_usdt - 0.3) * 100 ) / cash_usdt
        if ret > rate:
            print("profit is find on: "+ alt)
            write_to_file("profit is predict on: "+ alt + "\n")
            
            id = None
            i = 0
            while id == None and i < 1:
                try:
                    tr = trade.create_market_order(f"{alt}-USDT", side = 'buy', size = str(round(cash_alt, 4))) # step 1
                    print("step 1 has Done ... ... ...")
                    write_to_file(f"step 1 has Done ... ... ... buy: {alt}-USDT" + "\n")
                    id = tr["orderId"]
                except BaseException as error:
                    print(error)
                    print("step 1 hasnot Done!")
                    write_to_file("step 1 hasnot Done!" + "\n")
                    write_to_file(str(error) + "\n")
                    i +=1

            id = None
            i = 0
            while id == None and i < 1:
                try:
                    tr = trade.create_market_order(f"{alt}-BTC", side = 'sell', size = str(round(cash_alt, 4))) #step 2
                    print("step 2 has Done ... ... ...")
                    write_to_file(f"step 2 has Done ... ... ... buy: {alt}-BTC" + "\n")
                    id = tr["orderId"]
                except BaseException as error:
                    print(error)
                    print("step 2 hasnot Done!")
                    write_to_file("step 2 hasnot Done!" + "\n")
                    write_to_file(str(error) + "\n")
                    i +=1

            id = None
            i = 0
            while id == None and i < 1:
                try:
                    tr = trade.create_market_order("BTC-USDT", side = 'sell', size = str(round(cash_btc, 4))) # step 3
                    print("step 3 has Done ... ... ...")
                    write_to_file("step 3 has Done ... ... ... sell: BTC-USDT" + "\n")
                    id = tr["orderId"]
                except BaseException as error:
                    print(error)
                    print("step 3 hasnot Done!")
                    write_to_file("step 3 hasnot Done!" + "\n")
                    write_to_file(str(error) + "\n")
                    i +=1

            write_to_file("ALT-USDT  ask: " + ask1 + "\n")
            write_to_file("ALT-BTC  bid: " + bid2 + "\n")
            write_to_file("BTC-USDT  bid: " + bid + "\n")
            write_to_file("USDT_amount: " + str(cash_usdt) + "\n" + "BTC_amount: " + str(cash_btc) + "\n" + "alt_amount: " + str(cash_alt) + "\n" + "USDT_cash: " + str(cash) + "\n")
            write_to_file("USDT-" + alt + "-BTC-USDT " + " predict: " + str(round(ret, 4)) + "\n" + "\n" + "\n")
            #time.sleep(600)
            
        
        output = "USDT-BTC-" + alt + "-USDT" + ": " + str(round(ret, 4))
        #to_history(output + "\n")
        return output






































