import random

class MarkovChainTextGenerator:
    def __init__(self, text, order=1):
        self.order = order
        self.model = self.build_model(text)
    
    def build_model(self, text):
        model = {}
        for i in range(len(text) - self.order):
            state = text[i:i+self.order]
            next_char = text[i+self.order]
            if state not in model:
                model[state] = []
            model[state].append(next_char)
        return model

    def generate_text(self, length=100, seed=None):
        if seed is None:
            seed = random.choice(list(self.model.keys()))
        result = seed
        for _ in range(length - self.order):
            state = result[-self.order:]
            if state not in self.model:
                break
            next_char = random.choice(self.model[state])
            result += next_char
        return result

# Example usage
text = "this is an example text for the markov chain text generator."
generator = MarkovChainTextGenerator(text, order=2)
generated_text = generator.generate_text(length=50)
print(generated_text)
