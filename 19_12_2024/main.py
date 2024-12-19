class Account:
    def __init__(self, saldo, tranzakcja):
        self.saldo = saldo
        self.tranzakcja = tranzakcja

        def tranz(tranzakcja):
            if tranzakcja == 'przelew miedzy kontami':
                return 1
            elif tranzakcja == 'przelew zewnetrzny':
                return 2
            elif tranzakcja == 'wplata':
                return 3
            elif tranzakcja == 'wyplata':
                return 4
            else:
                return 'Try again'

a = Account(20,)

print(a)


