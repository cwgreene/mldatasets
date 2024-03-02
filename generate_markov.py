from typing import Dict, List, Tuple
import random
import numpy.random

class Node:
    def __init__(self, name : str, symbols : Dict[str, float]):
        self.name = name
        self.symbols = symbols

    def emit(self):
        if self.symbols == None:
            return None
        return random.choices(list(self.symbols.keys()),
                       weights=self.symbols.values(), k=1)[0]

class Markov:
    def __init__(self,
                states : Dict[Node, List[Dict[Node, float]]]): 
        self.states = states
        
    def sample(self, k, start=None):
        res = []
        if start == None:
            head = random.choice(list(self.states.keys()))
        else:
            head = start
        for _ in range(k):
            adjacent = [node for node in self.states[head]]
            weights = [self.states[head][adj] for adj in adjacent]
            s = head.emit()
            if s == None:
                break
            res.append(s)
            head = random.choices(adjacent, weights=weights, k=1)[0]
        return res

a = Node("a", {"A":.80,"a":.20})
b = Node("b", {"B":.25,"b":.75})

m = Markov({a: {a: .5, b:.5}, b: {a: .5, b:.5}})
for i in range(1024):
    print("".join(m.sample(100)))
