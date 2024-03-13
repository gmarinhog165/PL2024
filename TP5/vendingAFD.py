class ChangeCalculatorFSA:
    def __init__(self):
        self.states = {'START', 'CALCULATING', 'DONE'}
        self.alphabet = {'CALCULATE_CHANGE'}
        self.transitions = {
            'START': {'CALCULATE_CHANGE': 'CALCULATING'},
            'CALCULATING': {'CALCULATE_CHANGE': 'CALCULATING', 'DONE': 'DONE'}
        }
        self.current_state = 'START'
        self.initial_state = 'START'
        self.accepting_states = {'DONE'}
        self.change_amount = 0
        self.coins = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def reset(self):
        self.current_state = self.initial_state
        self.change_amount = 0
        for coin in self.coins:
            self.coins[coin] = 0

    def process_input(self, change_amount):
        self.change_amount = change_amount
        for coin_value in sorted(self.coins.keys(), reverse=True):
            while self.change_amount >= coin_value:
                self.coins[coin_value] += 1
                self.change_amount -= coin_value
        if self.change_amount == 0:
            return True, "Change calculated"
        else:
            return False, "Unable to calculate change"




# Example usage:
#change_calculator_fsa = ChangeCalculatorFSA()
#amount_paid = 800  # Amount paid in cents
#amount_due = 400   # Amount due in cents
#
#success, message = change_calculator_fsa.process_input(amount_paid, amount_due)
#if success:
#    print("Change calculated. Euro coins to give as change:")
#    for coin_value, num_coins in change_calculator_fsa.coins.items():
#        if num_coins > 0:
#            print(f"{num_coins}x {coin_value}€")
#else:
#    print("Error:", message)
