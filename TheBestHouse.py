def best_house(house_prices, max_budget):
    the_best = 0
    for price in house_prices:
        if price <= max_budget and price > the_best:
            the_best = price
    return the_best

prices=input("Enter the prices: ")
max_budget=int(input("Enter the max budget: "))

house_prices_list=[int(x) for x in prices.split(",")]

result=best_house(house_prices_list, max_budget)

print(f"The price of the house closest to your budget: {result}")
