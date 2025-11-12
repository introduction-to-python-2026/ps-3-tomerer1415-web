def approximate_pi(n_terms):
    pi_approx = 0
    for i in range(n_terms):
        pi_approx += ((-1) ** k) / (2 * k + 1)
    return 4 * pi_approx
