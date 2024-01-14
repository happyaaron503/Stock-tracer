import yfinance as yf
# 股價擷取
stock_name = input('請輸入股票代號: ') # 2330.TW
range = input('請輸入時間: ') # 單日, ex:2024-01-12
df = yf.Ticker(stock_name).history(period=range)
print(df)
