while True:
    print('''
    This is a calculator for some basic accounting equations. Values it can compute are: Current Ratio, Total Assets
    Turnover, Trade Payables Turnover Ratio, Average Age of Payables, Financial Leverage Ratio, Times Interest Earned,
    Dividend Yield Ratio, Dividend Payout Ratio, Quick Ratio, Inventory Turnover Ratio, and Cash Ratio.
    Enter "quit" to quit the program. 
    ''')
    calc_input = input("What would you like to calculate? (full name OR abbreviation, lowercase only: ")

    if calc_input == "cr" or calc_input == "current ratio":
        current_assets = float(input("Current Assets: "))
        current_liabilities = float(input("Current Liabilities: "))
        cr = round(current_assets / current_liabilities, 4)
        print("Current Ratio = " + str(cr))
    elif calc_input == "tat" or calc_input == "total assets turnover":
        net_sales = float(input("Net Sales/ Revenue: "))
        avg_assets = float(input("Avg Assets: "))
        tat = round(net_sales / avg_assets, 4)
        print("Total Assets Turnover = " + str(tat))
    elif calc_input == "tptr" or calc_input == "trade payables turnover ratio":
        cos = float(input("Cost of Sales: "))
        avg_ap = float(input("Average Accounts Payable: "))
        tptr = round(cos / avg_ap, 4)
        print("Trade Payables Turnover Ratio = " + str(tptr))
    elif calc_input == "aap" or calc_input == "average age of payables":
        year = 365
        tptr  = float(input("Trade Payables Turnover Ratio: "))
        aap = round(year / tptr, 4)
        print("Average Age of Payables = " + str(aap))
    elif calc_input == "flr" or calc_input == "financial leverage ratio":
        avg_assets = float(input("Avg Assets: "))
        avg_equity = float(input("Avg Equity: "))
        flr = round(avg_assets / avg_equity, 4)
        print("Financial Leverage Ratio = " + str(flr))
    elif calc_input == "tie" or calc_input == "times interest earned":
        profit = float(input("Profit Before Interest and Taxes: "))
        int_exp = float(input("Interest Expense: "))
        tie = round(profit / int_exp, 4)
        print("Times Interest Earned = " + str(tie))
    elif calc_input == "dyr" or calc_input == "dividend yield ratio":
        div_per_share = float(input("Dividends per Share: "))
        price_per_share = float(input("Market Price per Share: "))
        dyr = round(div_per_share / price_per_share, 4)
        print("Dividend Yield Ratio = " + str(dyr))
    elif calc_input == "dpr" or calc_input == "dividend payout ratio":
        dividends = float(input("Dividends: "))
        net_inc = float(input("Net Income: "))
        dpr = round(dividends / net_inc, 4)
        print("Dividend Payout Ratio= " + str(dpr))
    elif calc_input == "qr" or calc_input == "quick ratio":
        liquid_asset = float(input("Total Liquid Current Assets: "))
        current_liabilities = float(input("Current Liabilities: "))
        qr = round(liquid_asset / current_liabilities, 4)
        print("Quick Ratio = " + str(qr))
    elif calc_input == "cc" or calc_input == "cash ratio":
        cash_etc = float(input("Cash and equivalents: "))
        current_liabilities = float(input("Current Liabilities: "))
        cc = round(cash_etc / current_liabilities, 4)
        print("Cash Ratio = " + str(cc))
    elif calc_input == "quit":
        break
    else:
        print("¯\_(ツ)_/¯")





