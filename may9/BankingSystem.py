import json
import os
class CLIBankingSystem(object):
    def __init__(self):        
        self.lastAccountNumber=1000
        # data is a json dictionary to manage the banking data
        self.data=None
        self.dataFile="may9/bankingData.json"
        #cheking if the file already exists
        if os.path.exists(self.dataFile):
            with open(self.dataFile, 'r') as json_file:
                self.data=json.load(json_file)
        else:
            #if json file not exists,this is the basic stucture of the json file
            self.data={
                "lastAccountNumber":self.lastAccountNumber,
                "accounts":{}
            }
            with open(self.dataFile, 'w') as json_file:
                json.dump(self.data, json_file, indent=4)
             
    def createAccount(self):
        #set account number
        accountNumber=self.data["lastAccountNumber"]+1
        self.data["lastAccountNumber"]=accountNumber
        self.data["accounts"][accountNumber]={
            "name":input("Enter your name: "),
            "balance":0
        }
        #rewriting the json file after creating the account
        with open(self.dataFile, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
        print(f"Account created successfully. Your account number is {accountNumber}.")
    def deposit(self):
        accountNumber=(input("Enter your account number: "))
        if accountNumber in self.data["accounts"]:
            amount=float(input("Enter the amount to deposit: "))
            self.data["accounts"][accountNumber]["balance"]+=amount
            with open(self.dataFile, 'w') as json_file:
                json.dump(self.data, json_file, indent=4)
            print(f"Deposited {amount} to account number {accountNumber}.")
        else:
            print("Account not found.")
    def withdraw(self):
        accountNumber=(input("Enter your accout number: "))
        if accountNumber in self.data["accounts"]:
            ammount=float(input("Enter the amount to withdraw: "))
            if (self.data["accounts"][accountNumber]["balance"])>=ammount:
                (self.data["accounts"][accountNumber]["balance"])-=ammount
                with open(self.dataFile, 'w') as json_file:
                    json.dump(self.data, json_file, indent=4)
                print(f"Withdrawn {ammount} from account number {accountNumber}.")
            else:
                print("Insufficient balance.")
    def getAccountDetails(self):
        accountNumber=input("enter your account Number: ")
        if accountNumber in self.data["accounts"]:
            accoutDetails=self.data["accounts"][accountNumber]
            print(f"Account Number: {accountNumber}")
            print(f"Name: {accoutDetails['name']}")
            print(f"Balance: {accoutDetails['balance']}")
        else:
            print("Account not found.")
def main():
    bankingSystem=CLIBankingSystem()
    while True:
        print("Welcome to the Banking System")
        print("1. Create Account")
        print("2. deposit")
        print("3. Withdraw")
        print("4. show Account Details")
        print("5. Exit")
        choice=input("Enter your choice: ")
        if choice=="1":
            bankingSystem.createAccount()
        elif choice=="2":
            bankingSystem.deposit()
        elif choice=="3":
            bankingSystem.withdraw()
        elif choice=="4":
            bankingSystem.getAccountDetails()
        elif choice=="5":
            print("Exiting the Banking System...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__=="__main__":
    main()
        


