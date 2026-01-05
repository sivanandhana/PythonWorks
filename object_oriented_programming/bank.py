class bank:
    acc_num:int

    name:str

    acc_type:str

    balance:int

    def create_account(self,acc_num,name,acc_type,balance):

        self.acc_num=acc_num

        self.acc_type=acc_type

        self.name=name

        self.balance=balance

    def deposit(self,amount):

        self.balance+=amount

        print(f"your account {self.acc_num} creadited with {amount}")
    