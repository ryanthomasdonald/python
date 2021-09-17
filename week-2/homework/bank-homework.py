class AccountHolder:
    def __init__(self, first_name, account_type, status, balance):
        self.first_name = first_name
        self.account_type = account_type
        self.status = status
        self.balance = balance

class Bank:
    def __init__(self, name, address):
        self.name = name 
        self.address = address 
        self.accounts = []
        
# open new account
    def new_account(self, first_name, account_type, status, balance):
        new_member = AccountHolder(first_name, account_type, status, balance)
        self.accounts.append(new_member)
        
# show account holder
    def show_all_members(self):
        index = 0
        for member_obj, index in self.accounts:
            print(f"{index + 1}. {member_obj.first_name}")
            index += 1

# # show bank balance for account holder

# # show total bank deposits or bank balance

# class AccountHolder:
#     def __init__(self, fName, accountType, status, balance):
#         self.fName = fName
#         self.accountType = accountType
#         self.status = status
#         self.balance = balance


# class Bank:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.accounts = []  #[obj, obj,]

#     # open new account
#     def newAccount(self, fName, accountType, status, balance):
        
#         newMember = AccountHolder(fName, accountType, status, balance)
#         self.accounts.append(newMember)
        
#     def showAllMembers(self):
        
#         index = 1 
#         for memberObj in self.accounts: 
#             print(f'{index} {memberObj.fName} ')
#             index+=1
        
#         self.showAccount()
            
#     def showAccount(self): 
#         memberID = int(input(f'Select member to show details'))
        
#         id = memberID - 1 
        
#         print(f'{self.accounts[id].fName}  {self.accounts[id].accountType} {self.accounts[id].status} {self.accounts[id].balance} ')
        
    
#     def showTotalBankDeposits(self): 
#         balance = 0 
        
#         for member in self.accounts: 
            
#             balance += member.balance
            
#         print(f'Bank Balance : {balance}')
        
        

#     # show account holder

#     # show bank balance for account holder

#     # show total bank deposits or bank balance

# nationalBank = Bank('Wells Fargo', '123 sesame st')
                    
# nationalBank.newAccount('Matt', 'savings', 'open', 500)

# nationalBank.newAccount('Victoria', 'checking', 'open', 1000)

# nationalBank.newAccount('Andrew', 'checking', 'open', 400)

# nationalBank.showAllMembers()

# nationalBank.showTotalBankDeposits()