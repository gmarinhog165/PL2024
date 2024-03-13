import csv

produtos = {}

#### Ler CSV e armazenar no dicionário
with open('produtos.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    next(spamreader, None)
    for row in spamreader:
        produtos[row[0]] = (row[1],row[2],row[3])



##### Analex
import ply.lex as lex
from vendingAFD import ChangeCalculatorFSA


tokens = (
    'OPERATOR',
    'DINHEIRO',
    'PRODUTO',
)

t_OPERATOR = r'\b(LISTAR|MOEDA|SELECIONAR|SAIR)\b'
t_DINHEIRO = r'\b((1|2|5|10|20|50)c|(1|2)e)\b|\.'
t_PRODUTO = r'\bA\d{1,2}\b'

def t_newline(t):
    r'\n+'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore  = ' |, '


lexer = lex.lex()


# Classe da vending machine
class VendingMachine:
    def __init__(self):
        self.euros = 0
        self.cents = 0
        self.lastOp = None

    def process_token(self, token):
        if token.type == 'DINHEIRO':
            if self.lastOp != 'MOEDA':
                print(f"Illegal character: {token.value}")
            elif token.value == '.':
                print(f'Saldo = {str(self.euros) + "e" if self.euros > 0 else ""}{str(self.cents) + "c" if self.cents > 0 else ""}')
            else:
                self._convert_to_cents(token.value)


        elif token.type == 'PRODUTO':
            if self.lastOp != 'SELECIONAR':
                print(f"Illegal character: {token.value}")
            else:
                troco = self.calculate_change(float(produtos[token.value][2])*100)
                if troco > 0:
                    print(f'Pode retirar o produto dispensado "{produtos[token.value][0]}"')
                    print(f"Saldo = {str(self.euros) + 'e' if self.euros > 0 else ''}{str(self.cents) + 'c' if self.cents > 0 else ''}")
                else:
                    print("Saldo insufuciente para satisfazer o seu pedido")
                    print(f"Saldo = {str(self.euros) + 'e' if self.euros > 0 else ''}{str(self.cents) + 'c' if self.cents > 0 else ''}; Pedido = {produtos[token.value][2]}c")


        elif token.type == 'OPERATOR':
            self.lastOp = token.value
            if token.value == 'SAIR':
                coins = self.calculate_coins()
                print(f"Pode retirar o troco: {coins}")
                print("Até à próxima")
                return -1
            elif token.value == 'LISTAR':
                print("cod | nome | quantidade | preço")
                print("--------------------------------")
                for key, value in produtos.items():
                    print(f"{key}\t\t{value[0]}\t\t{value[1]}\t\t{value[2]}")

        return 1

    def _convert_to_cents(self, value):
        if value.endswith('e'):
            self.euros += int(value[:-1])
        elif value.endswith('c'):
            cents = int(value[:-1])
            if self.cents + cents >= 100:
                self.cents = (self.cents + cents)%100
                self.euros += 1
            else:
                self.cents += cents

    def calculate_change(self, spent):
        if self.cents - spent > 0:
            self.cents -= spent
        else:
            if self.euros > 0:
                self.cents -= spent 
                self.cents += 100
                self.euros -= 1
            else:
                return -1
        return 1

    
    def calculate_coins(self):
        change_calculator_fsa = ChangeCalculatorFSA()
        total = self.euros*100 + self.cents
        success, message = change_calculator_fsa.process_input(total)
        ret = ""
        if success:
            for coin_value, num_coins in change_calculator_fsa.coins.items():
                if num_coins > 0:
                    if coin_value >= 100:
                        ret += str(num_coins) + "x" + str(coin_value/100) + "e\t"
                    else:
                        ret += str(num_coins) + "x" + str(coin_value) + "c\t"
        return ret



i = 1
vd = VendingMachine()
while(i > 0):
    data = input()
    lexer.input(data)
    for tok in lexer:
        i = vd.process_token(tok)
        if(i < 0): break
