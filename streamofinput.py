item_list = []
final_amt = 0
while True:    
    item = input("Name of the Item (press q to quit) : ")
    if item != "q":
        price = input(f"Price of {item} : ")
        integer_price = int(price)
        item_list.append(item)
        final_amt += integer_price

    else:
        print(item_list)
        print(f"final bill : {final_amt}")
        break

