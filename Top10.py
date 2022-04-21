import StockDB

reporter = StockDB.StockDB()
stats = [{}]
for i in range(1, 11):
    stats.append(reporter.get_by_rank(i))

outputString = "<h2> Top Ten Most Volatile Companies </h2><center><table style='padding:10px; border:1px solid black; border-collapse:collapse;'>"
outputString += "<tr><th style = 'padding:10px; border:1px solid black;'>Rank</th><th style = 'padding:10px; border:1px solid black;'>Name</th><th style = 'padding:10px; border:1px solid black;'>Ticker</th><th style = 'padding:10px; border:1px solid black;'>Price VI</th></tr></th><th style = 'padding:10px; border:1px solid black;'>Volume VI</th></tr></th><th style = 'padding:10px; border:1px solid black;'>Twitter Account</th></tr>"
i = 0
for record in stats:
    if i > 0:
        outputString += "<tr><td style = 'text-align:center; padding:10px; border:1px solid black;'>" + str(record["rank"]) + "</td>"
        outputString += "<td style = 'text-align:center; padding:10px; border:1px solid black;'>" + str(record['name']) + "</td>"
        outputString += "<td style = 'text-align:center; padding:10px; border:1px solid black;'>" + str(record["ticker"]) + "</td>"
        outputString += "<td style = 'text-align:center; padding:10px; border:1px solid black;'>" + str(record["pctvi"]) + "</td>"
        outputString += "<td style = 'text-align:center; padding:10px; border:1px solid black;'>" + str(record["volumevi"]) + "</td>"
        outputString += "<td style = 'text-align:center; padding:10px; border:1px solid black;'>" + str(record["account"]) + "</td></tr>"
    i += 1

outputString += "<tr><td style = 'border:1px solid black;'> </td></tr></center></table>"

print(outputString)