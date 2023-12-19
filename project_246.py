from tkinter import *
from web3 import Web3#task1
root = Tk()

root.title("My Ethereum App")
root.geometry("600x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum gas fee in other currencies", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
# block_entry = Entry(root, text="This is Entry Widget", bd=2)
# #
# block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
value_in_ether = Label(root, bg="white", font=("bold", 14))
value_in_ether.place(relx=0.5, rely=0.28, anchor=CENTER)
value_in_dollar = Label(root, bg="white", font=("bold", 10))
value_in_dollar.place(relx=0.5, rely=0.48, anchor=CENTER)
value_in_rupees = Label(root, bg="white", font=("bold", 10))
value_in_rupees.place(relx=0.5, rely=0.58, anchor=CENTER)
value_in_pounds = Label(root, bg="white", font=("bold", 10))
value_in_pounds.place(relx=0.5, rely=0.68, anchor=CENTER)


url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))
# main function
# Start code for Task 1 below
def ethereum_block():
    gas_price = web3.eth.gas_price
    wei_price = gas_price/10**9
    gas_price_ether = wei_price/10**9
    # Start code for Task 2 below   
    gas_price_dollar = gas_price_ether*2232.61
    gas_price_ruppe = gas_price_ether*185817.01
    gas_price_pounds = gas_price_ether*1754.45

    # Start code for Task 3 below
    value_in_ether["text"] = "Value of gas in Ether: "+str(gas_price_ether)+"ETH"
    value_in_dollar["text"] = "Value of gas in Dollar: "+str(gas_price_dollar)+"$"
    value_in_rupees["text"] = "Value of gas in Ruppes: "+str(gas_price_ruppe)+" Ruppes"
    value_in_pounds["text"] = "Value of gas in Pounds: "+str(gas_price_pounds)+" Pounds"


   
    search_btn.destroy()


search_btn = Button(root, text="Search currency fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()