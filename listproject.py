#creating product list
product=[]

#creating product list
product_price=[]

status = True

while status:
    menu="""
           1)press 1 for Prduct Manager
           2)press 2 for customer
           3)press 3 for exit


     """
    print(menu)

    user_choice=int(input("Enter your choice: "))

    if user_choice==1:
        user_status=True

        while user_status:
            name=input("Enter the product name:  ")
            product.append(name)
            price=int(input("Enter Product price: "))
            product_price.append(price)

            choice=input("Do you want to add more more products?press y for yes and n for no:  ")
            if choice=='y' or choice=='Y':
                user_status=True

            else:
                user_status=False

    elif user_choice==2:
        print("Customer Panel") 

        for i in range(0,len(product)):
            print(f"{product[i]} Rs. {product_price[i]}")

    else:
        print("Thank you for using")
        status=False                        