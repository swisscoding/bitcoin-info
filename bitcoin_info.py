#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import requests
from bs4 import BeautifulSoup

# decoration
print(stylize("\n---- | Get Bitcoin information | ----\n", fg("red")))

# class
class Scraper:
    def __init__(self):
        self.url = "https://www.coindesk.com/price/bitcoin"

    # output magic method
    def __repr__(self):
        data = self.scrape(self.url)
        current_price = stylize(data[0], fg("red"))
        change_in_perc = stylize(data[1], fg("red"))
        market_cap = stylize(data[2], fg("red"))
        ath = stylize(data[3], fg("red"))

        return f"Current Bitcoin price: {current_price}\
        \nChange in % (24H): {change_in_perc}\
        \nMarket capital: {market_cap}\nAll time high: {ath}\n"

    # methods
    def scrape(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        targets = ["price-large", "percent-value-text", "price-medium", "price-small"]
        contents = []

        for target in targets:
            result = soup.find(class_=target)
            for info in result:
                contents.append(info)

        contents.pop(0)
        return contents

# main execution
if __name__ == "__main__":
    print(Scraper())
