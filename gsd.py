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
    print("EPS  " + str(quote["EPS (TTM)"]))
    print("Market Cap  " + marketCap)
    print("Dividend & Yield  " + str(quote["Forward Dividend & Yield"]))
    print("P/E  " + str(quote["PE Ratio (TTM)"]))
    print("Price-to-Cashflow  " + a["P/FCF"])
    print("Price/Sales  " + psratio)
    print("Debt/Equity  " + debtEquity)
    print("Return-On-Assets  " + returnOnAssets)
    print("Return-On-Equity  " + returnOnEquity)
    print("Gross Margin  " + grossMargin)
    print("Net Income  " + str(income.iloc[4, 0]))
    print("Operating Income  " + str(income.iloc[8, 0]))
    print("Gross Profit  " + str(income.iloc[6, 0]))
    print("Total Assets  " + str(sheet.iloc[3, 0]))
    print("Total Liabilities  " + str(sheet.iloc[0, 0]))
    print("Total Shareholder Equity  " + str(sheet.iloc[1, 0]))
    print("Net Cashflow  " + str(cash.iloc[8, 0]))



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
    two = ("Market Cap "+"\n" + marketCap)
    three = ("Dividend & Yield "+"\n" + str(quote["Forward Dividend & Yield"]))
    f = ("P/E "+"\n" + str(quote["PE Ratio (TTM)"]))
    f_2 = ("Price-to-Cashflow  "+"\n" + a["P/FCF"])
    five = ("Price/Sales "+"\n" + psratio)
    six = ("Debt/Equity "+"\n" + debtEquity)
    seven = ("Return-On-Assets "+"\n" + returnOnAssets)
    eight = ("Return-On-Equity "+"\n" + returnOnEquity)
    nine = ("Gross Margin "+"\n" + grossMargin)
    ten = ("Net Income "+"\n" + str(income.iloc[4, 0]))
    eleven = ("Operating Income "+"\n" + str(income.iloc[8, 0]))
    twelve = ("Gross Profit "+"\n" + str(income.iloc[6, 0]))
    t_2 = ("Total Assets  "+"\n" + str(sheet.iloc[3, 0]))
    thirteen = ("Total Liabilities "+"\n" + str(sheet.iloc[0, 0]))
    fourteen = ("Total Shareholder Equity "+"\n" + str(sheet.iloc[1, 0]))
    fifteen = ("Net Cashflow "+"\n" + str(cash.iloc[8, 0]))

    return one + "\n" + two + "\n" + three + "\n" + f + "\n"+ f_2+ "\n" + five + "\n" + six + "\n" + seven + "\n" + eight + "\n" + nine + "\n" + ten + "\n" + eleven + "\n" + twelve + "\n" + t_2 + "\n" + thirteen + "\n" + fourteen + "\n" + fifteen
