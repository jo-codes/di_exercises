# Daily challenge :
# DNA

# This challenge is about Biology.

#     Build a DNA object. DNA is composed of chromosomes who is itself composed of Genes.
#         A Gene is a single value 0 or 1, it can mutate (flip).
#         A Chromosome is a serie of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
#         A DNA is a serie of 10 chromosome, and it can also mutate the same way Chromosomes can.

#     Implement these classes as you see fit.
#     Create a new class called `Organismè that accepts a DNA object and a environement parameter that sets the probability for its DNA to mutate.
#     Instantiate a number of Organims and let them mutate until one gets to a DNA is only made of 1s. Then stop and record the number of generations (iterations) it took.

# Write your results in you personal biology research notebook and tell us your conclusion :).

# gene x 10. let's just code a gene class
import random


class Gene():
    flipped = 42

    def __init__(self):
        pass

    def mutate(self):
        if random.choice([0, 1]):
            self.flipped = 1
        else:
            self.flipped = 0

        return self.flipped


class Chromosome(Gene):
    genes = []
    i = 0
    while i < 10:
        gene = Gene()
        genes.append(gene)
        i += 1

    def __init__(self):
        pass

    def mutate(self):  # overiding other mutate
        x = 0

        while x < 10:
            if random.choice([0, 1]):
                self.genes[x] = 1
            else:
                self.genes[x] = 0
            x += 1

        return self.genes
