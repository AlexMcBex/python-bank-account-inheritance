class BankAccount():
  def __init__(self):
    self.balance = 0
  def deposit(self, amount):
    self.balance+= amount
    # print(f'depositing {amount} into the account\nYour new balance is {self.balance}')
  def withdraw(self, amount):
    self.balance-= amount
    # print(f'withdrawing {amount} from the account\nYour new balance is {self.balance}')
  def accumulate_interest(self):
    self.balance = self.balance+(self.balance/100*2)

class ChildrensAccount:
  def __init__(self):
    self.balance = 0
  def deposit(self, amount):
    self.balance+= amount
  def withdraw(self, amount):
    self.balance-= amount
  def accumulate_interest(self):
    self.balance += 10

class OverdraftAccount:
  def __init__(self):
    self.balance = 0
    self.overdraft_penalty = 40
  def deposit(self, amount):
    self.balance+= amount
  def withdraw(self, amount):
    if amount > self.balance:
      self.balance-= self.overdraft_penalty  
    else:
      self.balance-= amount
  def accumulate_interest(self):
    if self.balance <= 0:
      self.balance = self.balance
    else:
      self.balance = self.balance+(self.balance/100*2)

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
