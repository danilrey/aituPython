purchStock = 32.87
purchNum = 1000
sumForBuy = purchStock * purchNum
percent = sumForBuy * 0.02


soldStock = 33.92
sumForSell = soldStock * purchNum
percent2 = sumForSell * 0.02


print("Joe paid for stock: ", sumForBuy-percent,"\n")
print("Comission: ", percent, "\n")
print("Sold: ", sumForSell- percent2, "\n")
print("Sold: ", percent2, "\n")


print(" ", sumForSell-sumForBuy-percent-percent2, "\n")