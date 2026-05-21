def goods(*infor,count=0,score=0,express=0):
    price = [goods[1] * goods[2] for goods in infor]
    total_price = sum(price)
    if total_price >= 5000 and count <= total_price:
        total_price -= count
    if total_price >= 5000 and score//100 <= total_price:
        total_price -= score//100
    total_price += express
    return total_price
cost = goods(("鲜花",10,99),("苹果17",17,5),count=2000,score=4000,express=10)
print(cost)