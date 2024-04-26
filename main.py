import random
class User:
    content_of_mesasage = []
    message = str(input())
    content_of_mesasage.append(message)
    id = int(input())
    username = str(input())
    user_id_to_mesasage = []
    user_id_to_mesasage.append(id)
    user_id_to_mesasage.append(username)

    status = random.randint(0, 1)
    current_con_mess = message
    amount = 0
    qw = 0
    def __init__(self, id, user_name, status, amo, Maravin):
        self.id = id
        self.username = user_name
        self.status = status
        self.amount = amo
        self.Maravind = Maravin
    if current_con_mess != message:
        mod = 0
        def Amount(self, mod):
            self.amount = mod+1
            self.qw = self.amount

            return self.amount
            return self.qw

    def info(self, user_name, mod):
        self.id = print(id)
        self.username = print(user_name)
        self.amount = print(self.qw)
    if user_id_to_mesasage == [10, 'name']:
        if status == 1:
            def send_message(self, nort):
                self.content_of_mesasage = nort
                self.Maravind = print(nort)
        else:
            status = 1
    return content_of_mesasage

'''Задача B2'''

class Admin(User):
    def remove(self):
        self.user_id_to_mesasage.clear()
    def clear(self):
        self.content_of_mesasage.clear()
