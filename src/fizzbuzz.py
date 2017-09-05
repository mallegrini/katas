
class Checker:
    def __init__(self, numero, testo):
        self.numero = numero
        self.testo = testo
    def check(self, numero):
        if numero % self.numero == 0:
            return self.testo

class FizzBuzzer:
    def __init__(self, checkers):
        self.checkers = checkers

    def say(self, numero):
        res = []
        for checker in self.checkers:
            n = checker.check(numero)
            if n: res.append(n)

        if not res: return str(numero)
        return "".join(res)
