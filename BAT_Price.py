import requests
from bs4 import BeautifulSoup
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Real Time")
        self.geometry("250x150")

        self.text = tk.Label(self, text="BAT PRICE", font=("Courier", 20, 'bold'))
        self.text.place(relx=0.5,
                        rely=0.25,
                        anchor='center')

        self.price = tk.Label(self, text=self.get_crypto_price(), fg="green", borderwidth=2, relief="groove")
        self.price.config(font=("Courier", 20, 'bold'))
        self.price.place(relx=0.5,
                         rely=0.5,
                         anchor='center')

        self.price.after(3000, self.update_price)

    def update_price(self):
        self.price.configure(text=self.get_crypto_price())

        # schedule another timer
        self.price.after(30000, self.update_price)

    @staticmethod
    def get_crypto_price():

        # <span class="no-wrap" data-coin-id="677" data-coin-symbol="bat"
        # data-price-btc="0.0000120725054143013" data-target="price.price">

        url = 'https://www.coingecko.com/en/coins/basic-attention-token'
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        # print(soup.prettify())
        text = soup.find('span', attrs={'class': 'no-wrap'}).get_text(strip=True)
        return text


if __name__ == "__main__":
    root = App()
    root.mainloop()
