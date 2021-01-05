import finviz

filters = ['exch_nasdaq', 'cap_largeover']
results = finviz.Screener(filters=filters)

apple = finviz.get_stock('AAPL')
analyst_targets = finviz.get_analyst_price_targets('AAPL')
news = finviz.get_all_news('AAPL')
insider = finviz.get_insider('AAPL')

print(results)