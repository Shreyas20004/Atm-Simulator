from cardHolder import cardholder

def print_menu():
    """Prints the menu for the user to choose an option."""
    print("Please choose from one of the given options:")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Show Balance")
    print("4.Exit")
    
def Deposit(cardholder):
    try:
        deposit = float(input("Deposit amount:"))
        cardholder.set_balance(cardholder.get_balance()+deposit)
        print("Deposit Successful!\nCurrent Balance:",str(cardholder.get_balance()))
        
    except Exception:
        print("Invalid input")
def Withdraw(cardholder):
    try:
        Withdraw = float(input("Withdraw amount:"))
        if cardholder.get_balance()< Withdraw:
            print("Insufficient balance")
        else:
            print("Processing transaction....")
            cardholder.set_balance(cardholder.get_balance()-Withdraw)
            print("Withdrawal Successful!\nCurrent Balance:",str(cardholder.get_balance()))
            
    except Exception:
        print("Invalid input")
def ShowBalance(cardholder):
    return print("Your current ballence:",cardholder.get_balance())



if __name__=="__main__":
    current_user=cardholder('','','','','')
    
    listOfUsers=[]
    listOfUsers.append(cardholder('0101',0000,'LOKI','Odin',0))
    listOfUsers.append(cardholder('0111',1111,'Thor','Odin',1000))
    
    ## Request Verification
    Debitno=""
    while True:
        try:
            Debitno=str(input("Enter Your Card Number:"))
            debitMatch= [holder for holder in listOfUsers if holder.cardNum==Debitno ]
            if(len(debitMatch)>=0):
                current_user=debitMatch[0]
                print("User Found")
                break
            else:
                print("Card Not Recognized, Try again")
        except:
            print("Error ! Please enter a valid number.")
            
    ### Request pin
    while True:
        try:
            userpin=int(input("Enter  your 4 digit PIN: "))
            if(current_user.get_pin()==userpin):
                print("Pin verified")
                break
            else:
                print("Error Try again!")
        except:
            print("Please Enter Valid pin!")
            
    print("Welcome ",current_user.get_firstname()," :)")
    ch=0
    while ch != 4:
        print_menu()
        try:
            ch = int(input())
        except:
            print("Invalid Input , please enter integer value ")
            
        if  (ch == 1):
            Deposit(current_user)
        elif(ch ==2):
            Withdraw(current_user)
        elif ch==3:
            ShowBalance(current_user)
        elif ch==4:
            break
        else:
            option=0
    
    print("Thank you, Have a nice day!")   
        
            
        