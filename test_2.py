from collections import UserList


class AmountPaymentList(UserList):

    def amount_payment(self):
        self.data = [1, -3, 4]
        return sum(map(lambda x: True if x > 0 else False, self.data))


a = AmountPaymentList()
print(a.amount_payment())