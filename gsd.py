import yahoo_fin.stock_info as si
import pandas as pd
import finviz
from flask import app

def getA(ticker):
    return finviz.get_stock(ticker)

def getStockData(ticker):
    val = si.get_stats_valuation(ticker)
    val = val.iloc[:, :2]
    val.columns = ["Attribute", "Recent"]
    psratio = str(float(val[val.Attribute.str.contains("Price/Sales")].iloc[0, 1]))
    a = finviz.get_stock(ticker)
    marketCap = a['Market Cap']
    debtEquity = a['Debt/Eq']
    returnOnAssets = a['ROA']
    returnOnEquity = a['ROE']
    grossMargin = a['Gross Margin']
    quote = si.get_quote_table(ticker)
    sheet = si.get_balance_sheet(ticker)
    income = si.get_income_statement(ticker)
    cash = si.get_cash_flow(ticker)
    print("EPS  " + str(quote["EPS (TTM)"])) #TRUE
    m = {'K': 3, 'M': 6, 'B': 9, 'T': 12}
    marketCap = int(float(marketCap[:-1]) * 10 ** m[marketCap[-1]])
    print("Market Cap  " + str(marketCap)) #FALSE, WHOLE NUMBER NEEDED
    st = str(quote["Forward Dividend & Yield"])
    c = st[st.rfind('(') + 1: st.rfind(')') - 1]
    c = float(c) / 100
    b = st[: st.rfind('(') - 1]
    dvd = str(b) + "; " + str(c)
    print("Dividend & Yield  " + dvd) #Yield need to be 0.01
    print("P/E  " + str(quote["PE Ratio (TTM)"])) #TRUE
    print("Price-to-Cashflow  " + a["P/FCF"]) #TRUE
    print("Price/Sales  " + psratio) #TRUE
    print("Debt/Equity  " + debtEquity) #TRUE
    print("Return-On-Assets  " + returnOnAssets) #False, need to be 0.0
    print("Return-On-Equity  " + returnOnEquity) #False, same as above
    print("Gross Margin  " + grossMargin) #False
    print("Net Income  " + str(income.iloc[4, 0]))
    print("Operating Income  " + str(income.iloc[8, 0]))
    print("Gross Profit  " + str(income.iloc[6, 0]))
    print("Total Assets  " + str(sheet.iloc[3, 0]))
    print("Total Liabilities  " + str(sheet.iloc[0, 0]))
    print("Total Shareholder Equity  " + str(sheet.iloc[1, 0]))
    print("Net Cashflow  " + str(cash.iloc[8, 0]))

#getStockData('AAPL')

def getStockData_string(ticker):
    val = si.get_stats_valuation(ticker)
    val = val.iloc[:, :2]
    val.columns = ["Attribute", "Recent"]
    psratio = str(float(val[val.Attribute.str.contains("Price/Sales")].iloc[0, 1]))
    a = finviz.get_stock(ticker)
    marketCap = a['Market Cap']
    debtEquity = a['Debt/Eq']
    returnOnAssets = a['ROA']
    returnOnEquity = a['ROE']
    grossMargin = a['Gross Margin']
    quote = si.get_quote_table(ticker)
    sheet = si.get_balance_sheet(ticker)
    income = si.get_income_statement(ticker)
    cash = si.get_cash_flow(ticker)
    one = ("EPS " +"\n"+ str(quote["EPS (TTM)"]))
    m = {'K': 3, 'M': 6, 'B': 9, 'T': 12}
    marketCap = int(float(marketCap[:-1]) * 10 ** m[marketCap[-1]])
    two = ("Market Cap "+"\n" + str(marketCap))
    st = str(quote["Forward Dividend & Yield"])
    if 'N' not in st:
        c = st[st.rfind('(') + 1: st.rfind(')') - 1]
        c = float(c) / 100
        b = st[: st.rfind('(') - 1]
        dvd = str(b) + "; " + str(c)
        st = dvd
    else:
        pass


    three = ("Dividend & Yield "+"\n" + st)
    f = ("P/E "+"\n" + str(quote["PE Ratio (TTM)"]))
    f_2 = ("Price-to-Cashflow  "+"\n" + a["P/FCF"])
    five = ("Price/Sales "+"\n" + psratio)
    six = ("Debt/Equity "+"\n" + debtEquity)
    if "-" not in returnOnAssets:
        rroa = returnOnAssets[: returnOnAssets.rfind('%') - 1]
        rroa = str(float(rroa) / 100)
    else:
        rroa = returnOnAssets

    if "-" not in returnOnEquity:
        rroe = returnOnEquity[: returnOnEquity.rfind('%') - 1]
        rroe = str(float(rroe) / 100)
    else:
        rroe = returnOnEquity

    seven = ("Return-On-Assets "+"\n" + rroa)

    eight = ("Return-On-Equity "+"\n" + rroe)
    gmm = grossMargin[: grossMargin.rfind('%') - 1]
    gmm = str(float(gmm) / 100)
    nine = ("Gross Margin "+"\n" + gmm)
    ten = ("Net Income "+"\n" + str(income.iloc[4, 0]))
    eleven = ("Operating Income "+"\n" + str(income.iloc[8, 0]))
    twelve = ("Gross Profit "+"\n" + str(income.iloc[6, 0]))
    t_2 = ("Total Assets  "+"\n" + str(sheet.iloc[3, 0]))
    thirteen = ("Total Liabilities "+"\n" + str(sheet.iloc[0, 0]))
    fourteen = ("Total Shareholder Equity "+"\n" + str(sheet.iloc[1, 0]))
    fifteen = ("Net Cashflow "+"\n" + str(cash.iloc[8, 0]))

    return one + "\n" + two + "\n" + three + "\n" + f + "\n"+ f_2+ "\n" + five + "\n" + six + "\n" + seven + "\n" + eight + "\n" + nine + "\n" + ten + "\n" + eleven + "\n" + twelve + "\n" + t_2 + "\n" + thirteen + "\n" + fourteen + "\n" + fifteen
#a = getStockData_string('aapl')
#print(a)

