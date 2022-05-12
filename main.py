from set_up import ask_ask_bid, ask_bid_bid
import asyncio
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient

class arbitrage:
  def __init__(self):
    self.usdt_cash = 250
    self.rate = 20
    self.fee = 0.1 / 100
    self.ask_btcusdt = 0
    self.ask_dashbtc = 0
    self.bid_dashusdt = 0
    self.ask_lunabtc = 0
    self.bid_lunausdt = 0
    self.ask_hbarbtc = 0
    self.bid_hbarusdt = 0
    self.ask_derobtc = 0
    self.bid_derousdt = 0
    self.ask_solvebtc = 0
    self.bid_solveusdt = 0
    self.ask_sensobtc = 0
    self.bid_sensousdt = 0
    self.ask_reqbtc = 0
    self.bid_requsdt = 0
    self.ask_dagbtc = 0
    self.bid_dagusdt = 0
    #
    self.bid_btcusdt = 0
    self.bid_rlcbtc = 0
    self.ask_rlcusdt = 0
    self.bid_bnbbtc = 0
    self.ask_bnbusdt = 0
    self.bid_injbtc = 0
    self.ask_injusdt = 0
    self.bid_pondbtc = 0
    self.ask_pondusdt = 0
    self.bid_iostbtc = 0
    self.ask_iostusdt = 0
    self.bid_glmbtc = 0
    self.ask_glmusdt = 0
    self.bid_dgbbtc = 0
    self.ask_dgbusdt = 0
    self.bid_xnobtc = 0
    self.ask_xnousdt = 0
    

a = arbitrage()

async def main():
 
  async def deal_msg(msg):
    
    if msg['topic'] == '/market/ticker:BTC-USDT':
      a.ask_btcusdt = msg["data"]['bestAsk']
      a.bid_btcusdt = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:DASH-BTC':
      a.ask_dashbtc = msg["data"]['bestAsk']
    
    elif msg['topic'] == '/market/ticker:DASH-USDT':
      a.bid_dashusdt = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:LUNA-BTC':
      a.ask_lunabtc = msg["data"]['bestAsk']
    
    elif msg['topic'] == '/market/ticker:LUNA-USDT':
      a.bid_lunausdt = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:HBAR-BTC':
      a.ask_hbarbtc = msg["data"]['bestAsk']
    
    elif msg['topic'] == '/market/ticker:HBAR-USDT':
      a.bid_hbarusdt = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:DERO-BTC':
      a.ask_derobtc = msg["data"]['bestAsk']
    
    elif msg['topic'] == '/market/ticker:DERO-USDT':
      a.bid_derousdt = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:SOLVE-BTC':
      a.ask_solvebtc = msg["data"]['bestAsk']
    
    elif msg['topic'] == '/market/ticker:SOLVE-USDT':
      a.bid_solveusdt = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:SENSO-BTC':
      a.ask_sensobtc = msg["data"]['bestAsk']
    
    elif msg['topic'] == '/market/ticker:SENSO-USDT':
      a.bid_sensousdt = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:REQ-BTC':
      a.ask_reqbtc = msg["data"]['bestAsk']
    
    elif msg['topic'] == '/market/ticker:REQ-USDT':
      a.bid_requsdt = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:DAG-BTC':
      a.ask_dagbtc = msg["data"]['bestAsk']
    
    elif msg['topic'] == '/market/ticker:DAG-USDT':
      a.bid_dagusdt = msg["data"]['bestBid']

    ###
    #elif msg['topic'] == '/market/ticker:BTC-USDT': ###
      #a.bid_btcusdt = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:RLC-BTC':
      a.bid_rlcbtc = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:RLC-USDT':
      a.ask_rlcusdt = msg["data"]['bestAsk']

    elif msg['topic'] == '/market/ticker:BNB-BTC':
      a.bid_bnbbtc = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:BNB-USDT':
      a.ask_bnbusdt = msg["data"]['bestAsk']

    elif msg['topic'] == '/market/ticker:INJ-BTC':
      a.bid_injbtc = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:INJ-USDT':
      a.ask_injusdt = msg["data"]['bestAsk']

    elif msg['topic'] == '/market/ticker:POND-BTC':
      a.bid_pondbtc = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:POND-USDT':
      a.ask_pondusdt = msg["data"]['bestAsk']

    elif msg['topic'] == '/market/ticker:IOST-BTC':
      a.bid_iostbtc = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:IOST-USDT':
      a.ask_iostusdt = msg["data"]['bestAsk']

    elif msg['topic'] == '/market/ticker:GLM-BTC':
      a.bid_glmbtc = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:GLM-USDT':
      a.ask_glmusdt = msg["data"]['bestAsk']

    elif msg['topic'] == '/market/ticker:DGB-BTC':
      a.bid_dgbbtc = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:DGB-USDT':
      a.ask_dgbusdt = msg["data"]['bestAsk']

    elif msg['topic'] == '/market/ticker:XNO-BTC':
      a.bid_xnobtc = msg["data"]['bestBid']

    elif msg['topic'] == '/market/ticker:XNO-USDT':
      a.ask_xnousdt = msg["data"]['bestAsk']

    #elif msg['topic'] == '/spotMarket/level2Depth5:BTC-USDT':
            #print(msg["data"])
    
    stat = ask_ask_bid(a.ask_btcusdt, a.ask_dashbtc, a.bid_dashusdt, "DASH",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_ask_bid(a.ask_btcusdt, a.ask_lunabtc, a.bid_lunausdt, "LUNA",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_ask_bid(a.ask_btcusdt, a.ask_hbarbtc, a.bid_hbarusdt, "HBAR",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_ask_bid(a.ask_btcusdt, a.ask_derobtc, a.bid_derousdt, "DERO",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_ask_bid(a.ask_btcusdt, a.ask_solvebtc, a.bid_solveusdt, "SOLVE",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_ask_bid(a.ask_btcusdt, a.ask_sensobtc, a.bid_sensousdt, "SENSO",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_ask_bid(a.ask_btcusdt, a.ask_reqbtc, a.bid_requsdt, "REQ",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_ask_bid(a.ask_btcusdt, a.ask_dagbtc, a.bid_dagusdt, "DAG",a.usdt_cash, a.fee, a.rate)
    print(stat)
    ###
    stat = ask_bid_bid(a.ask_rlcusdt, a.bid_rlcbtc, a.bid_btcusdt, "RLC",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_bid_bid(a.ask_bnbusdt, a.bid_bnbbtc, a.bid_btcusdt, "BNB",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_bid_bid(a.ask_injusdt, a.bid_injbtc, a.bid_btcusdt, "INJ",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_bid_bid(a.ask_pondusdt, a.bid_pondbtc, a.bid_btcusdt, "POND",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_bid_bid(a.ask_iostusdt, a.bid_iostbtc, a.bid_btcusdt, "IOST",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_bid_bid(a.ask_glmusdt, a.bid_glmbtc, a.bid_btcusdt, "GLM",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_bid_bid(a.ask_dgbusdt, a.bid_dgbbtc, a.bid_btcusdt, "DGB",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_bid_bid(a.ask_dgbusdt, a.bid_dgbbtc, a.bid_btcusdt, "XNO",a.usdt_cash, a.fee, a.rate)
    print(stat)
  # is public
  client = WsToken()
  #is private
  # client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')

  ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
  symbols1 = "BTC-USDT,DASH-BTC,DASH-USDT,LUNA-BTC,LUNA-USDT,HBAR-BTC,HBAR-USDT,DERO-BTC,DERO-USDT,SOLVE-BTC,SOLVE-USDT,SENSO-BTC,SENSO-USDT,REQ-BTC,REQ-USDT,DAG-BTC,DAG-USDT"
  symbols2 = "RLC-BTC,RLC-USDT,BNB-BTC,BNB-USDT,INJ-BTC,INJ-USDT,POND-BTC,POND-USDT,IOST-BTC,IOST-USDT,GLM-BTC,GLM-USDT,DGB-BTC,DGB-USDT,XNO-BTC,XNO-USDT"
  symbols = symbols1+","+symbols2
  await ws_client.subscribe(f'/market/ticker:{symbols}')
  #await ws_client.subscribe('/spotMarket/level2Depth5:BTC-USDT')
  while True:
      await asyncio.sleep(60, loop=loop)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
