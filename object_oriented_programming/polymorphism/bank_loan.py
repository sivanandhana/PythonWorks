class Rbi:

    def gold_loan_rate(self):

        print("Gold loan rate ",8.5)

    def home_loan_rate(self):

        print("home loan rate",9.2)

    def car_loan_rate(self):

        print("car loan rate",8.5) 


class Hdfc(Rbi):

    def gold_loan_rate(self):
        
        print("gold loan rate",9.5)

    def home_loan_rate(self):
        
        print("home loan rate",10)

    def car_loan_rate(self):
       
        print("car loan rate",9.7)

hdfc_instance = Hdfc()

hdfc_instance.gold_loan_rate()
hdfc_instance.home_loan_rate()
hdfc_instance.car_loan_rate()
