class budget:

    def __init__(self, category):
        self.name= category
        self.balance= 0
    

    def intro(self):
        select_option= int(input('''what would you like to do: 
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Check balance \n'''))
        if select_option==1:
            self.deposit()
        elif select_option==2:
            self.withdraw()
        elif select_option==3:
            self.transfer()
        elif select_option==4:
            self.check_balance()
        else:
            print('you have entered an incorrect option. please try again')


    def deposit(self):
        inputed_amount= int(input('how much do you want to deposit: '))
        amount= self.balance + inputed_amount
        print(f'Your new balance is {amount}')
        self.end()

    def withdraw(self):
        while True:
            withdrawal_amount= int(input('How much would you like to withdraw: '))
            
            if withdrawal_amount < self.balance:
                print("Your withdrawal is successful")
                self.end()
                break
            elif withdrawal_amount > self.balance:
                print("Insufficient funds")
                self.end()
                break
            else:
                print("you've inputed the wrong option")
                
    def transfer(self):
        while True:
            transfer_category= int(input('''what category would you like to transfer to: 
            1. Food
            2. Entertainment
            3. Clothing \n'''))
            transfer_amount= int(input('amount: '))
            if transfer_category==1:
                print(f'You have transferred {transfer_amount} to Food category')
                self.end()
                break
            elif transfer_category==2:
                print(f'You have transferred {transfer_amount} to Entertainment category')
                self.end()
                break
            elif transfer_category==3:
                print(f'You have transferred {transfer_amount} to Clothing category')
                self.end()
                break
            else:
                print('You have inputed the wrong option. Please try again.')

    def check_balance(self):
        print(f'Your balance is {self.balance}')
        self.end()

    def end(self):
        while True:
            ending_note= int(input('''would you like to perform another operation? 
            1. Yes
            2. No \n'''))
            if ending_note==1:
                self.intro()
                break
            elif ending_note==2:
                print('thank you for using this app ')
                exit()
                break
            else:
                print('You have inputed the wrong option. Please try again.')

                


food=budget('food')
entertainment=budget('entertainment')
clothing=budget('clothing')

print("+++WELCOME TO THE BUDGET APP+++")
print('''Here are your categories:
1. Food
2. Entertainment
3. Clothing
''')
while True:
    category= int(input('Please select preferred category: \n'))
    if category==1:
        print(f'{(food.name)}')
        food.intro()
        break
    elif category==2:
        print(f'{(entertainment.name)}')
        entertainment.intro()
        break
    elif category==3:
        print(f'{(clothing.name)}')
        clothing.intro()
        break
    else:
        print('You have entered an incorrect option')