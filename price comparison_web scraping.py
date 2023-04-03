import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import Scrollbar
import webbrowser

global user_search 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def amazon(user_search):
    
    try:  
        global amazon_url
        global amazon_price
        user_search1 = user_search.replace(' ','+')          
        amazon_url = f"https://www.amazon.in/s?k={user_search1}&ref=nb_sb_noss_1"

        r = requests.get(amazon_url, headers = headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        amazon_list = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_list))


        for i in range(0,amazon_page_length):  

            user_search = user_search.lower()
            amazon_id = amazon_list[i].getText().strip().lower()            

            if any(x in amazon_id for x in user_search.split()):
                amazon_id = amazon_list[i].getText().strip()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip()                 
                break     

        return f"{amazon_id}\n\nPrice : {amazon_price}"
    
    except:
        amazon_price = '-'
        return 'Product not found'
        
# print(amazon('Apple iphone 11'))
 #############################################################################################   
 
def flipkart(user_search):
    
    try:  
        global flipkart_url
        global flipkart_price
        user_search1 = user_search.replace(' ','+')
        flipkart_url = f'https://www.flipkart.com/search?q={user_search1}' 
                       
        r = requests.get(flipkart_url, headers = headers)        
        soup = BeautifulSoup(r.text, 'html.parser')     
        
        flipkart_list = soup.select('._4rR01T') 
        flipkart_page_length = int(len(flipkart_list))
        
        for i in range(0,flipkart_page_length):  

            user_search = user_search.lower()
            flipkart_id = flipkart_list[i].getText().strip().lower()                       

            if any(x in flipkart_id for x in user_search.split()):
                flipkart_id = flipkart_list[i].getText().strip()
                flipkart_price = soup.select('._1_WHN1')[i].getText().strip()                 
                break     

        return f"{flipkart_id}\n\nPrice : {flipkart_price}"  

    except:
        flipkart_price = '-'
        return 'Product not found'    
    
# print(flipkart('apple iphone 11'))
############################################################################################

def vijaysales(user_search):
    
    try:  
        global vijaysales_url
        global vijaysales_price
        user_search1 = user_search.replace(' ','-')
        vijaysales_url = f'https://www.vijaysales.com/search/{user_search1}'         
                       
        r = requests.get(vijaysales_url, headers = headers)        
        soup = BeautifulSoup(r.text, 'html.parser')     
        
        vijaysales_list = soup.select('.Dynamic-Bucket-ProductName') 
        vijaysales_page_length = int(len(vijaysales_list))
        
        for i in range(0,vijaysales_page_length):  

            user_search = user_search.lower()
            vijaysales_id = vijaysales_list[i].getText().strip().lower()                       

            if any(x in vijaysales_id for x in user_search.split()):
                vijaysales_id = vijaysales_list[i].getText().strip()
                vijaysales_price = soup.select('.Dynamic-Bucket-vsp')[i].getText().strip()                 
                break     

        return f"{vijaysales_id}\n\nPrice : {vijaysales_price}"  

    except:
        vijaysales_price = '-'
        return 'Product not found'    
    
# print(vijaysales('apple iphone 11'))
#############################################################################################

def urls():  
    return f"{flipkart_url}\n\n\n{vijaysales_url}\n\n\n{amazon_url}\n\n\n"

def open_url(event):        
        webbrowser.open_new(flipkart_url)
        webbrowser.open_new(vijaysales_url)
        webbrowser.open_new(amazon_url)
#############################################################################################

def convert(price):
    d = {' ':'', 'INR':'', ',':'','₹':''}
    for x,y in d.items():
        price = price.replace(x,y) 
           
    try:
        price = int(float(price))
        l.append(price)
        return price
    except:
        pass      

    # b=a.replace(" ",'')
    # c=b.replace("INR",'')
    # d=c.replace(",",'')
    # f=d.replace("₹",'')
    # g=int(float(f))
    # return g
   
def compare():
    
    global l    
    l = []
    
    ap = convert(amazon_price)
    fp = convert(flipkart_price)
    vsp = convert(vijaysales_price)  
      
    # print(l)    
    try:        
        min_price = min(l)
        if min_price == fp:
            l1.config(fg = 'red2')
        elif min_price == vsp:
            l2.config(fg = 'red2')
        elif min_price == ap:
            l3.config(fg = 'red2')
        else:
            pass 
    except:                                # when the list is empty
        pass 

####################################################################################################
def search():
    box1.insert(1.0,"LOADING...")
    box2.insert(1.0,"LOADING...")
    box3.insert(1.0,"LOADING...")
    box4.insert(1.0,"LOADING...")

    # search_button.place_forget()

    box1.delete(1.0,"end")
    box2.delete(1.0,"end")
    box3.delete(1.0,"end")
    box4.delete(1.0,"end")
    
    l1.config(fg = 'black')
    l2.config(fg = 'black')
    l3.config(fg = 'black')
   
    t1=flipkart(product_name.get())
    box1.insert(1.0,t1)

    t2=vijaysales(product_name.get())
    box2.insert(1.0,t2)

    t3=amazon(product_name.get())
    box3.insert(1.0,t3)

    t4 = urls()
    box4.insert(1.0,t4)    
    
    compare()
    
    
    
##############################################################################################

window = Tk()
window.wm_title("PRICE COMPARISON")
window.minsize(1500,700)
window.configure(bg = 'light blue')

lable_one =Label(window, text="Enter Product Name :", font=("Times New Roman", 18), bg = 'light blue')
lable_one.place(relx=0.3, rely=0.1, anchor="center")

product_name = StringVar()
product_name_entry = Entry(window, textvariable=product_name, width=30, font=("courier", 13))
product_name_entry.place(relx=0.5, rely=0.1, anchor="center")

search_button =  Button(window, text="SEARCH", width=12, command= search, font = ("Times New Roman", 15))
search_button.place(relx=0.7, rely=0.1, anchor="center")


l1 =  Label(window, text="FLIPKART", font=("Times New Roman", 20), bg = 'light blue')
l2 =  Label(window, text="VIJAYSALES", font=("Times New Roman", 20), bg = 'light blue')
l3 =  Label(window, text="AMAZON", font=("Times New Roman", 20), bg = 'light blue')
l4 =  Label(window, text="Click on the URLs to visit the websites (top results)", font=("Times New Roman", 20), bg = 'light blue')


l1.place(relx=0.2, rely=0.25, anchor="center")
l2.place(relx=0.5, rely=0.25, anchor="center")
l3.place(relx=0.8, rely=0.25, anchor="center")
l4.place(relx=0.5, rely=0.6, anchor="center")

scrollbar = Scrollbar(window)

box1 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set, font=("Times New Roman", 12) )
box2 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set, font=("Times New Roman", 12) )
box3 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set, font=("Times New Roman", 12) )


box1.place(relx=0.2, rely=0.4, anchor="center")
box2.place(relx=0.5, rely=0.4, anchor="center")
box3.place(relx=0.8, rely=0.4, anchor="center")

box4 =  Text(window, height=12, width=50, yscrollcommand=scrollbar.set, fg="blue", cursor="hand2")
box4.place(relx=0.5, rely=0.8, anchor="center")
box4.bind("<Button-1>", open_url)

window.mainloop()


