import numpy as np

def DE(test_function, dimension, bounds, F_scale, cross_prob, popsize, max_evals):
    """
    Differential Evolution algorithm

    Args:
    test_function -- function to conduct
    bound_lower -- lower bound of the test function
    bound_upper -- upper bound of the test function
    F_scale -- scale factor on mutation
    cross_prob -- the probability of 2 individuals to do crossover
    popsize -- the population size
    max_evals -- the maximum fitness evaluation for the algorithm
    seed_number -- value of seed we want to run

    Returns:
    results -- best results after finishing the algorithm
    all_pops -- all the population 
    """
    eps = 0.00001

    bound_lower, bound_upper = np.asarray(bounds).T

    diff = np.fabs(bound_lower - bound_upper)

    pop = bound_lower + diff * np.random.rand(popsize, dimension)

    fitness = np.asarray([test_function(ind) for ind in pop])
    num_eval = 1
    
    best_idx = np.argmin(fitness)
    best = pop[best_idx]

    results = []
    all_pops = []
    results.append((np.copy(best), fitness[best_idx], num_eval))
    all_pops.append(np.copy(pop))
    generation_count = 0
    
    while True:
        # max_evals = 10000 if popsize >= 512 else 5000
        if num_eval > max_evals:
            break
        for i in range(popsize):
            # Mutation step
            idxes = [idx for idx in range(popsize) if idx != i]
            a, b, c = pop[np.random.choice(idxes, 3, replace=False)]
            mutant = np.clip(F_scale*(b - c) + a, bound_lower, bound_upper)

            # Create cross point
            cross_points = np.random.rand(dimension) < cross_prob
            if not np.any(cross_points):
                cross_points[np.random.randint(0, dimension)] = True
            
            # Offspring
            trial = np.where(cross_points, mutant, pop[i])

            # Evaluate fitness
            f = test_function(trial)
            num_eval += 1

            if f < fitness[i]:
                pop[i] = trial
                fitness[i] = f 
                if f < fitness[best_idx]:
                    best = trial
                    best_idx = i

        results.append((np.copy(best), fitness[best_idx], num_eval))
        all_pops.append(np.copy(pop))

        if test_function(best) < eps:
            num_eval += 1
            break

        generation_count += 1

    return results, all_pops, generation_count


def ES(test_function, bounds, sigma_init, c_inc, c_dec, popsize, max_evals, dimension):
    eps = 0.00001

    bound_lower, bound_upper = np.asarray(bounds).T

    diff = np.fabs(bound_lower - bound_upper)

    mu = bound_lower + diff * np.random.rand(dimension)
    mu_fitness = test_function(mu)
    num_eval = 0

    results = []
    all_pops = []
    results.append((np.copy(mu), mu_fitness, num_eval))
    generation_count = 0
    sigma = sigma_init
    
    while True:
        max_evals = 10000 if popsize >= 512 else 5000
        if num_eval > max_evals:
            break
        epsilon = np.random.randn(popsize, dimension)
        offspring = mu + sigma * epsilon
        offspring = np.clip(offspring, bound_lower, bound_upper)
        offspring_fitness = np.asarray([test_function(offspring[i]) for i in range(popsize)])
        num_eval += popsize
        
        best_idx = offspring_fitness.argmin()
        best_fitness = offspring_fitness[best_idx]
        best_offspring = offspring[best_idx]

        if best_fitness <= mu_fitness:
            mu = best_offspring.copy()
            mu_fitness = best_fitness
            sigma *= c_inc 
        else:
            sigma *= c_dec
        
        results.append((np.copy(mu), mu_fitness, num_eval))
        all_pops.append(np.copy(offspring))
        if abs(mu_fitness) < eps:
            break
        generation_count += 1

    return results, all_pops, generation_count


def CEM(test_function, dimensions, bounds, popsize, num_elite, sigma_init, seed_number, max_evals):
    np.random.seed(seed_number)
    eps = 1e-4
    bound_lower, bound_upper = np.asarray(bounds).T
    sigma = sigma_init * np.eye(dimensions)

    diff = np.fabs(bound_lower - bound_upper)
    n_evals = 0
    num_evals = []
    # mu = np.random.rand(dimensions) - (bound_upper + 1)
    mu = bound_lower + diff * np.random.rand(dimensions)
    generation_count = 0
    all_mu = []
    all_sigma = []
    all_offspring = []
    all_pops = []
    all_sigma = []
    all_elite = []
    all_fitness = []
    
    while True:
    # for i in range(10000):
        if n_evals > max_evals:
            break
        all_mu.append(mu)
        all_sigma.append(sigma)

        x = np.random.multivariate_normal(mu, sigma, popsize)
        all_pops.append(np.copy(x))
        # print(np.sum(x))
        all_offspring.append(x)
        fitness = np.array([test_function(x[i]) for i in range(popsize)])
        n_evals += popsize
        best_fitness = max(fitness) 
        all_fitness.append(best_fitness)
        # print(x)
        if best_fitness < eps or np.sum(x) > 1e150 or np.sum(x) < -1e150:
            break

        elite_idx = fitness.argsort()[:num_elite]
        all_elite.append(elite_idx)
        mu = np.mean(x[elite_idx], axis=0)

        sigma = np.zeros_like(sigma)
        for i in range(num_elite):
            z = x[elite_idx[i]] - mu
            z = z.reshape(-1, 1)
            # print(num_evals)
            # sigma += tf.matmul(z.T, z)
            # sigma += (z.T * z)
            sigma += (z.T @ z)

        all_sigma.append(sigma)
        sigma *= (1/num_elite)
        generation_count += 1
        num_evals.append(n_evals)

    all_mu.append(mu)
    best_results = mu.copy()
    best_fitness = test_function(mu)
    return all_pops, all_sigma, all_mu, all_fitness, num_evals, generation_count

def CEMv2(test_function, dimensions, bounds, popsize, num_elite, sigma_init, extra_std, seed_number, max_evals):
    np.random.seed(seed_number)
    eps = 1e-4
    bound_lower, bound_upper = np.asarray(bounds).T
    sigma = sigma_init * np.eye(dimensions)

    diff = np.fabs(bound_lower - bound_upper)
    n_evals = 0
    num_evals = []
    mu = np.random.rand(dimensions) - (bound_upper + 1)
    generation_count = 0
    all_mu = []
    all_sigma = []
    all_offspring = []
    all_pops = []
    all_sigma = []
    all_elite = []
    all_fitness = []
    while True:
    # for i in range(10000):
        if n_evals > max_evals: 
            break
        all_mu.append(mu)
        all_sigma.append(sigma)

        x = np.random.multivariate_normal(mu, sigma, popsize)
        all_pops.append(np.copy(x))
        if np.sum(x) > 1e150 or np.sum(x) < -1e150:
            break
        all_offspring.append(x)
        fitness = np.array([test_function(x[i]) for i in range(popsize)])
        n_evals += popsize
        best_fitness = max(fitness) 
        all_fitness.append(best_fitness)
        if best_fitness < eps:
            break

        elite_idx = fitness.argsort()[:num_elite]
        all_elite.append(elite_idx)

        sigma = np.zeros_like(sigma)

        for i in range(num_elite):
            z = x[elite_idx[i]] - mu
            z = z.reshape(-1, 1)
            # sigma += tf.matmul(z.T, z)
            sigma += (z.T @ z)

        sigma += np.eye(dimensions)*extra_std
        
        all_sigma.append(sigma)
        sigma *= (1/num_elite)
        mu = np.mean(x[elite_idx], axis=0)

        generation_count += 1
        num_evals.append(n_evals)

    all_mu.append(mu)
    best_results = mu.copy()
    best_fitness = test_function(mu)
    return all_pops, all_sigma, all_mu, all_fitness, num_evals, generation_count
