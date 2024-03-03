import re 

class FiniteStateAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = initial_state
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def reset(self):
        self.current_state = self.initial_state


    def process_input(self, inseq):
        pattern = r'(?P<INT>[+\-]?\d+)|(?P<ON>[Oo][nN])|(?P<OFF>[Oo][Ff]{2})|(?P<EQ>\=)|(?P<SKIP>\s+)|(?P<UNKNOWN>.)'
        sum = 0
        i = 0
        while (i < len(inseq)):
            match = re.search(pattern, inseq[i:])
            token = match.groupdict()
            i += match.end()

            if token["INT"] and self.current_state == 'ON':
                sum += int(token["INT"])
            elif token["EQ"]:
                print(sum)
            elif token["ON"]:
                self.current_state = self.transitions[self.current_state]["ON"]
            elif token["OFF"]:
                self.current_state = self.transitions[self.current_state]["OFF"]
            elif token["SKIP"] or token["UNKNOWN"]:
                pass


# Example usage:

# Define states, alphabet, transitions, initial state, and accepting states
states = {'ON', 'OFF'}
alphabet = {'num', 'on', 'off', '='}
transitions = {'ON': {'INT': 'ON', 'ON': 'ON', 'OFF': 'OFF', 'EQ': 'ON', 'SKIP':'ON', 'UNKNOWN':'ON'},
                'OFF': {'INT': 'OFF', 'ON': 'ON', 'OFF': 'OFF', 'EQ': 'OFF', 'SKIP':'OFF', 'UNKNOWN':'OFF'}}

initial_state = 'ON'
accepting_states = {'ON', 'OFF'}

# Create the Finite State Automaton
fsa = FiniteStateAutomaton(states, alphabet, transitions, initial_state, accepting_states)

# Process input sequences
input_sequence1 = """1iMRE7r=HtzkAon8o2sdXVtM0oLoffzNxZi4t5eqOpZNEqCJaLonK1mMTy3d22W
offaJ8uH6sgDxy2xMJoNRQZ7aAmkmhF4N91eTqqzequb4eYpA34DIojequZtnvw
6LyrPxme0eqZbYZPon82fFbYKoffQXTonOnjjAAzS4=eq1tKe0VQuS89yuoffL
oNCs8rV24P3Eeq1GeAtonjvTK0A5KmKAEaOon1=deqQcZrZ5MBu58HzkequWQ5
XC9Fon83ctoffFHaEQFtN9aIonfjAq9eqW0L6F9W4=eq=2pOQRUgAM56DKoffZ
6BYeq7sYononKZV=eq0K9KdW=VononAid6Uon6GeoffW=onD=OffonEQ=offG=3
9MoNyOn=EQOff7offOn5DSOffOn9OnW=43Uk=OffOnON"""

result1 = fsa.process_input(input_sequence1)