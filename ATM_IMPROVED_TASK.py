from datetime import datetime 
Today = datetime.today()
import random

Database = {
    2116973294: ['ed@gmail.com', 'edikan', 'akpan', 'edikan', 0 ]
    }

def init():
    print('Welcome to EDK bank')
    print('Today =', Today)
        
    haveAccount = int(input('Do you have an account with us 1.Yes, 2.No \n'))
    
    if(haveAccount == 1):

            login()
    elif(haveAccount == 2):
    
            register()

    else:
            print('Pls enter a valid option')
            init()


def login():

    print('login your acccount')       
        
    accountNumberFromUser = input('What is your account number \n')
    
    isValidAccountNumber = userAccountNumberValidation(accountNumberFromUser)
    
    if isValidAccountNumber:

        password = input('enter your password \n')
        
        for accountNumber, userdetails in Database.items():

           if(accountNumber == int(accountNumberFromUser)):
               if(userdetails[3] == password):
                   print('Welcome %s %s' %(userdetails[1], userdetails[2] ) )
                  

                   bankOperation(userdetails)  
        print('Invalid account or password')      
        login() 
    
    else:
        login()                  

def userAccountNumberValidation(accountNumber):
    if accountNumber:
        if len(str(accountNumber)) == 10:
            try:
                int(accountNumber)
                return True
            except ValueError:
                print('Invalid account number, account number most be integers')
                return False
            except TypeError:
                print('Invalid account type, pls enter a valid account number')
        else:
            print('Account number cannot be more than 10')
            return False
    else:
        print('Account number is a required field')
        return False


         
def register():

    print('Register')
    email = input('What is your email? \n')
    firstName = input('What is your first name? \n')
    surname = input('What is your last name? \n')
    password = input('Create your password? \n')

    accountNumber = generateAccountNumber()

    Database[accountNumber] = [email,firstName,surname,password]

    print('Your account has been created')
    print('Your account number is: %d' %accountNumber )
    login()
 

def bankOperation(user):
    

    selectedOption = int(input("What would you like to do? (1) withdrawal (2) deposit (3) account balance (4) exit \n"))

    if(selectedOption == 1):
        withdrawalOperation(user)

    elif(selectedOption == 2):
        depositOperation(user)

    elif(selectedOption == 3):
        accountBalance(user)
    
    elif(selectedOption == 4): 
        exit()
    
    else:  
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation(user):
    print("Withdrawal")
    amountToWithdraw = int(input('How much would you like to withdraw\n'))

    if(amountToWithdraw <= user[4]):
        print('Take your cash\n')
        print('Would you like to perform another transaction? 1. yes 2. no')
        selectedoption = int(input( ))
        if(selectedoption == 1):
            return login()
        if(selectedoption == 2):
                exit()

    else:
        print('Insufficient balance')

def depositOperation(user):
    print("Deposit")
    amountToDeposit = int(input('How much would you like to deposit\n'))
    
    if(amountToDeposit > 0):


        user[4] = (amountToDeposit + user[4])


        print('Current Account Balance is\n', user[4])
        print('Would you like to perform another transaction? 1. yes 2. no')
        selectedoption = int(input( ))
        if(selectedoption == 1):
            return login()
        if(selectedoption == 2):
                exit()


        else:
            print('Enter a correct amount')

   

def accountBalance(user):

    print(user[4])
    print('Would you like to perform another transaction? 1. yes 2. no')
    selectedoption = int(input( ))
    if(selectedoption == 1):
        return login()
        if(selectedoption == 2):
                exit()
  

def generateAccountNumber(): 
    return random.randrange(1111111111,9999999999) 

   
init()

