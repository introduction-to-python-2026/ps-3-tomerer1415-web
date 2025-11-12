def approximate_pi(n_terms):
    pi = 0
    for i in range(n_terms):
        pi += ((-1)**i)/(2*i + 1)
    return (4 * pi)
