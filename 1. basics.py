from tkinter import * 
from tkinter import messagebox
import random

screen_1 = Tk()
screen_1.title("Blitz Pizza App")
screen_1.geometry("900x650") 
screen_1.config(background="DarkOrange1")


frame_1 = Frame(screen_1, bg="yellow")
frame_1.pack(fill="x")
title = Label(frame_1, text="Blitzer's Pizza", bg="yellow", fg="black", font=("Brush Script MT", 40, "bold"))
title.pack()

main_frame = Frame(screen_1, bg="orange red")
main_frame.pack(fill="both", expand=True)

left_frame = Frame(main_frame, bg="sienna2", padx=10)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = Frame(main_frame, bg="IndianRed1", padx=10)
right_frame.pack(side="right", fill="both", expand=True)

order_number=random.randint(10000, 99999)

pizza_options = [("Margherita", 25), ("Veggie", 32), ("Ranch", 28), ("BBQ", 34), ("Pepperoni", 34), ("Pineapple", 31)]
size_options = [("Small", 0), ("Med", 10), ("Large", 30), ("XL", 40), ("Party", 60)]
crust_options = [("Thin", 0), ("Classic", 0), ("Thick", 7.5), ("Stuffed", 12.5), ("GF", 5.0)]
extra_toppings = ["Cheese", "Olives", "Jalapenos", "Tomatoes", "Basil", "Mushrooms", "Onions"]

selected_pizza = StringVar(value="Margherita")
selected_size = StringVar(value="Small")
selected_crust = StringVar(value="Classic")
topping_vars = {topping: BooleanVar() for topping in extra_toppings}
quantity = IntVar(value=1)


pizza_price=dict(pizza_options)
size_price=dict(size_options)
crust_price=dict(crust_options)


Label(right_frame, text="ORDER SUMMARY", font=("Arial", 16, "bold"), bg="IndianRed1").pack(pady=10)
summary_label = Label(right_frame, text="No items added", font=("Courier", 12), 
                      bg="white", fg="black", justify="left", width=30, height=10, relief="sunken")
summary_label.pack(pady=10)

def add_order():
    pizza=selected_pizza.get()
    size=selected_size.get()
    crust=selected_crust.get()
    Quantity=quantity.get()
    total_price=(pizza_price[pizza]+size_price[size]+crust_price[crust])*Quantity
    summary = (f"ITEM: {selected_pizza.get()}\n"
               f"SIZE: {selected_size.get()}\n"
               f"QTY:  {quantity.get()}\n"
               f"BASE: {selected_crust.get()}\n"
               f"TOTAL PRICE: {total_price}")            
    summary_label.config(text=summary)

def clear_order():
    summary_label.config(text="")   

def placing_order():
    summary_label.config(text="")
    messagebox.showinfo("Order Placed!", f"Please wait for ten minutes!,\n Your Order Number is {order_number}")

def create_section(parent, text, options, variable, is_radio=True):
    Label(parent, text=text, font=("Arial", 11, "bold"), bg="sienna2").pack(anchor="w", pady=(5, 0))
    frame = Frame(parent, bg="sienna2")
    frame.pack(anchor="w")

    if is_radio:
        for i, (name, price) in enumerate(options):
            Radiobutton(frame, text=name, variable=variable, value=name, bg="orange", font=("Arial", 9)).grid(row=i//3, column=i%3, sticky="w", padx=2)
    else:
        for i, topping in enumerate(extra_toppings):
            Checkbutton(frame, text=topping, variable=topping_vars[topping], bg="orange", font=("Arial", 9)).grid(row=i//4, column=i%4, sticky="w", padx=2)


create_section(left_frame, "1. Pizza Type:", pizza_options, selected_pizza)
create_section(left_frame, "2. Size:", size_options, selected_size)
create_section(left_frame, "3. Crust:", crust_options, selected_crust)
create_section(left_frame, "4. Toppings:", None, None, is_radio=False)


action_frame = Frame(left_frame, bg="sienna2")
action_frame.pack(pady=15, fill="x")


Label(action_frame, text="Qty:", font=("Arial", 11, "bold"), bg="sienna2").pack(side="left")
Spinbox(action_frame, from_=1, to=10, textvariable=quantity, width=3, font=("Arial", 12)).pack(side="left", padx=5)

Button(action_frame, text="ADD TO ORDER", bg="green", fg="white", font=("Arial", 10, "bold"), 
       command=add_order, padx=10).pack(side="left", padx=10)

Button(right_frame, text="Clear", bg="blue", fg="white", font=("Arial", 10, "bold"), 
       command=clear_order, padx=10).pack(side="left", padx=10)

Button(right_frame, text="Place Order", bg="red", fg="white", font=("Arial", 10, "bold"), 
       command=placing_order, padx=10).pack(side="right", padx=10)

screen_1.mainloop()