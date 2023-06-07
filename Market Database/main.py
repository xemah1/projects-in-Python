import oversight

oversight.create()
print("-"*75)
print("Products Available in:",end=" ")
categories = oversight.control()
for i in categories :
    print(i,end=" | ")
print()
print("-"*75)
end,customer = True,False
basket = 0
while end :
    if customer == False :
        print("customer|oversight|end")
        choice = input().lower()
    else :
        print("customer|end")
        choice = input().lower()

    if choice[0] == "c" :
        basket = oversight.customer(basket)
        if basket != 0 :
            customer = True
            print("Basket:",f"{basket:.2f}")
    elif choice[0] == "o" and customer == False :
        oversight.main()
    else :
        end = False