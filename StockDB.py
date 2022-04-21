import json
import pprint
import numpy


class StockDB:
    def __init__(self):
        with open("database.json") as db:
            file = db.read()
            self.data = json.loads(file)
        self.removeDupes()
        self.remove_nan()
        self.rank()


    def get_info(self, ticker):
        for record in self.data:
            if record["ticker"].lower() == ticker.lower():
                return(self.data[ticker])
            else:
                print("Ticker value not found")

    def save(self, name, ticker, pct, volume, account):
        x = {
            "name": name,
            "ticker": ticker,
            "pctvi": pct,
            "volumevi": volume,
            "rank": -1,
            "account": account
        }
        self.data.append(x)
        self.removeDupes()
        self.remove_nan()
        self.rank()
        self.dump()

    def rank(self):
        holder = sorted(self.data, key=lambda k: k["pctvi"], reverse=True)
        i = 1
        for record in holder:
            record["rank"] = i
            i += 1
        self.data = sorted(holder, key=lambda k: k["rank"])

    def rankByVol(self):
        holder = sorted(self.data, key=lambda k: k["volumevi"], reverse=True)
        i = 1
        for record in holder:
            record["rank"] = i
            i += 1
        self.data = sorted(holder, key=lambda k: k["rank"])

    def output(self):
        pprint.pprint(self.data)

    def removeDupes(self):
        seen = []
        new = []
        for record in self.data:
            if record["name"] not in seen:
                seen.append(record["name"])
                new.append(record)

        self.data = new

    def remove_nan(self):
        new = []
        for record in self.data:
            if not (numpy.isnan(record["volumevi"]) or numpy.isnan(record["pctvi"])) :
                new.append(record)
        self.data = new

    def dump(self):
        with open("database.json", "r+") as db:
            db.truncate(0)
            db.close()

        with open("database.json", "w") as db:
            db.write(json.dumps(self.data))

    def get_by_rank(self, number):
        for record in self.data:
            if record["rank"] == number:
                return(record)

    def getVol_by_rank(self, number):
        self.rankByVol()
        for record in self.data:
            if record["rank"] == number:
                return(record)
