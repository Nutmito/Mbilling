import time 
import subprocess
import signal

title = """
-------------------------------------------------------------
                          MBILLING                  
-------------------------------------------------------------
"""
name_list={} 
login_data={}
item_list={}
item_serial={}
bill={}
no_of_dish=1


def add_item():
    subprocess.call("cls", shell=True)
    print("---------------------------Add Item--------------------------")
    name=input("Enter Name of Dish :")
    price=int(input("Enter Price :"))
    item_list[name]=price
    global no_of_dish
    item_serial[no_of_dish]=name 
    no_of_dish+=1
    print("-------------------------------------------------------------")
    print("\nItem Added Successfully")
    subprocess.call("cls", shell=True)

def display_menu():
    print("---------------------------FOOD MENU-------------------------")
    if(len(item_list))==0:
        print("Nothing to Show for now")
    else:
        number=1
        for i in item_list.keys():
            print(number,".",i,"\t= ",item_list[i])
            number+=1       
    print("-------------------------------------------------------------")
        
def order_food():
    display_menu()
    if(len(item_list))==0:
        print("Oops...Nothing to order for now!")
        order=False
    else:
        order=True
    while order==True:
        dish_number=int(input("Enter dish number :-"))
        quantity=int(input("Enter Quantity :-"))
        bill[item_serial[dish_number]]=quantity  
        cont=input("Want to add more ?(y/n): ")
        if cont=='Y' or cont=='y':
            order=True
        else:
            order=False
    print("\nFood Ordered successfuly\n\n")
    subprocess.call("cls", shell=True)
    return generate_bill()

def animate_bill():
    for i in range(4):
        print("\rGenerating your BILL    ",end="");
        time.sleep(0.1)
        print("\rGenerating your BILL.   ",end="");
        time.sleep(0.1)
        print("\rGenerating your BILL..  ",end="");
        time.sleep(0.1)
        print("\rGenerating your BILL... ",end="");
        time.sleep(0.1)
        print("\rGenerating your BILL....",end="");
        time.sleep(0.1)
    subprocess.call("cls", shell=True)
    
    
def generate_bill():
    animate_bill()
    print("\n-------------------------Bill-------------------------")
    number=1
    t_bill=0
    for i in bill.keys():
        one_tbill=bill[i]*item_list[i]
        print(number,".",i,"\t",bill[i],"x",item_list[i]," = ",one_tbill)
        t_bill+=one_tbill
        number+=1
    print("------------------------------------------------------")
    print("TOTAL BILL   =      ",t_bill)
    print("Tax 7%       =      "+"{:.2f}".format((t_bill/100)*7))
    t_bill+=t_bill/10
    print("Total        =     ",t_bill)
    print("------------------------------------------------------")   
    return True
    
def main():
    print("1.Add Item")
    print("2.Order Food")
    print("3.Bill")
    print('CTRL+C Exit!')
    choice=int(input("Enter your choice :"))
    if choice==1:
        add_item(),main()
    elif choice==2:
        display_menu(),main()
    elif choice==3:
        order_food(),main()
    else:
        main()

def handler(signum, frame):
    subprocess.call("cls", shell=True)
    print(subprocess.call("cls", shell=True), exit(1), flush=True)  
        
signal.signal(signal.SIGINT, handler)
print(title)
main()