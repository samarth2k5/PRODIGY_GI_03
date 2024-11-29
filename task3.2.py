import random

class MarkovChainWordGenerator:
    def __init__(self, text, order=1):
        self.order = order
        self.model = self.build_model(text.split())
    
    def build_model(self, words):
        model = {}
        for i in range(len(words) - self.order):
            state = tuple(words[i:i+self.order])
            next_word = words[i+self.order]
            if state not in model:
                model[state] = []
            model[state].append(next_word)
        return model

    def generate_text(self, length=50, seed=None):
        if seed is None:
            seed = random.choice(list(self.model.keys()))
        result = list(seed)
        for _ in range(length - self.order):
            state = tuple(result[-self.order:])
            if state not in self.model:
                break
            next_word = random.choice(self.model[state])
            result.append(next_word)
        return ' '.join(result)

# Example usage
text = "this is an example text for the Markov chain word generator."
generator = MarkovChainWordGenerator(text, order=2)
generated_text = generator.generate_text(length=10)
print(generated_text)
