class Income():
    def __init__(self):
        self.rental = 0
        self.laundry = 0
        self.storage = 0
        self.misc = 0

    def total_income(self):
        return self.rental + self.laundry + self.storage + self.misc

class Expenses():
    def __init__(self):
        self.tax = 0
        self.insurance = 0
        self.utilities = 0
        self.hoa = 0
        self.lawn_snow = 0
        self.vacancy = 0
        self.repairs = 0
        self.cap_ex = 0
        self.property_manage = 0
        self.mortgage = 0

    def total_expenses(self):
        return self.tax + self.insurance + self.utilities + self.hoa + self.lawn_snow + self.vacancy + self.repairs + self.cap_ex + self.property_manage + self.mortgage

class Cash_Flow():
    
    #def monthly(self):
    #    total = Income().total_income() - Expenses().total_expenses()
    #    return total

    def yearly(self):
        total = 12 * (self.monthly())
        return total

class Investment():
    def __init__(self):
        self.down_payment = 0
        self.closing_costs = 0
        self.rehab_budget = 0
        self.misc = 0

    def total_investment(self):
        total = self.down_payment + self.closing_costs + self.rehab_budget + self.misc
        return total

#class Cash_On_Cash():
    #def return_on_investment(self):
    #    roi = Cash_Flow().yearly() / Investment().total_investment()
    #    return roi

class Main():
    def run():
        inc = Income()
        exp = Expenses()
        c_f = Cash_Flow()
        inv = Investment()
        #c_o_c = Cash_On_Cash()

        inc.rental = int(input('Enter rental income: '))
        inc.laundry = int(input('Enter laundry income: '))
        inc.storage = int(input('Enter storage income: '))
        inc.misc = int(input('Enter misc income: '))

        exp.tax = int(input('Enter tax expense: '))
        exp.insurance = int(input('Enter insurance expense: '))
        exp.utilities = int(input('Enter utilities expense: '))
        exp.hoa = int(input('Enter hoa expense: '))
        exp.lawn_snow = int(input('Enter lawn_snow expense: '))
        exp.vacancy = int(input('Enter vacancy expense: '))
        exp.repairs = int(input('Enter repairs expense: '))
        exp.cap_ex = int(input('Enter cap_ex expense: '))
        exp.property_manage = int(input('Enter property_manage expense: '))
        exp.mortgage = int(input('Enter mortgage expense: '))

        inv.down_payment = int(input('Enter down_payment investment: '))
        inv.closing_costs = int(input('Enter closing_costs investment: '))
        inv.rehab_budget = int(input('Enter rehab_budget investment: '))
        inv.misc = int(input('Enter misc investment: '))

        print(str((inc.total_income() - exp.total_expenses()) * 12 / inv.total_investment() * 100) + "%")

Main.run()