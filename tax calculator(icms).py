def calc_icms(price:float,tax_rate:float):
    aliq = (tax_rate / 100)*price
    return aliq

def apply_icms(price:float,tax_rate:float):
    final_price = price + calc_icms(price,tax_rate)
    return final_price

def tax_calculator():
    while True:
        price = float(input("Insert the price, please: "))
        print("")
        tax_rate = float(input("Now, you can put the tax rate: ").replace("%",""))
        print("")
        print(f"ICMS: R${calc_icms(price,tax_rate).__round__(2)}")
        print("")
        print(f"Final Price: R${apply_icms(price,tax_rate).__round__(2)}")
        print("")

if __name__ == "__main__":
    tax_calculator()
