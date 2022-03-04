from functools import partial
import knapsack
from analyze import timer
import genetic

things = knapsack.generate_things(22)

things = knapsack.second_example

weight_limit = 3000

print("Weight Limit: %dkg" % weight_limit)
print("")

print("GENETIC ALGORITHM")
print("----------")
with timer():
    result = genetic.bruteforce(things, weight_limit)
with timer():
	population, generations = genetic.run_evolution(
		populate_func=partial(genetic.generate_population, size=10, genome_length=len(things)), # partial to reset the parameters which is specific to our code.
		fitness_func=partial(knapsack.fitness, things=things, weight_limit=weight_limit),
		fitness_limit=result[0],
		generation_limit=100)	

sack = knapsack.from_genome(population[0], things)
knapsack.print_stats(sack)


##1.The algorithm begins by creating a random initial population.
##2.The algorithm then creates a sequence of new populations. At each step, the algorithm uses the individuals in the current generation to create the next population. To create the new population, the algorithm performs the following steps:
##a)Scores each member of the current population by computing its fitness value. These values are called the raw fitness scores.
##b)Scales the raw fitness scores to convert them into a more usable range of values. These scaled values are called expectation values.
##c)Selects members, called parents, based on their expectation.
##d)Some of the individuals in the current population that have lower fitness are chosen as elite. These elite individuals are passed to the next population.
##e)Produces children from the parents. Children are produced either by making random changes to a single parent—mutation or by combining the vector entries of a pair of parents—crossover.
##f)Replaces the current population with the children to form the next generation.
##3.The algorithm stops when one of the stopping criteria is met.
