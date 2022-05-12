from set_up import ask_ask_bid
import asyncio
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient

class arbitrage:
  def __init__(self):
    self.usdt_cash = 23
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

a = arbitrage()

async def main():
 
  async def deal_msg(msg):

    if msg['topic'] == '/spotMarket/level2Depth5:BTC-USDT':
      a.ask_btcusdt = msg["data"]['asks'][1][0]

    elif msg['topic'] == '/spotMarket/level2Depth5:DASH-BTC':
      a.ask_dashbtc = msg["data"]['asks'][1][0]
    
    elif msg['topic'] == '/spotMarket/level2Depth5:DASH-USDT':
      a.bid_dashusdt = msg["data"]['asks'][1][0]

    elif msg['topic'] == '/spotMarket/level2Depth5:LUNA-BTC':
      a.ask_lunabtc = msg["data"]['asks'][1][0]
    
    elif msg['topic'] == '/spotMarket/level2Depth5:LUNA-USDT':
      a.bid_lunausdt = msg["data"]['asks'][1][0]

    #elif msg['topic'] == '/spotMarket/level2Depth5:BTC-USDT':
            #print(msg["data"])
    
    stat = ask_ask_bid(a.ask_btcusdt, a.ask_dashbtc, a.bid_dashusdt, "DASH",a.usdt_cash, a.fee, a.rate)
    print(stat)
    stat = ask_ask_bid(a.ask_btcusdt, a.ask_lunabtc, a.bid_lunausdt, "LUNA",a.usdt_cash, a.fee, a.rate)
    print(stat)
    
  # is public
  client = WsToken()
  #is private
  # client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')

  ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
  symbols = "BTC-USDT,DASH-BTC,DASH-USDT,LUNA-BTC,LUNA-USDT"
  #await ws_client.subscribe(f'/market/ticker:{symbols}')
  await ws_client.subscribe(f'/spotMarket/level2Depth5:{symbols}')
  while True:
      await asyncio.sleep(60, loop=loop)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())