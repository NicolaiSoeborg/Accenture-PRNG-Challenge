#!/usr/bin/env python3
from random import randint
NUM_CARDS = 4

# Random z0 (unknown to attacker):
z = [randint(0, 990881) for _ in range(NUM_CARDS)]

# Define "coefficients" (from pdf):
x_coe = [977, 607, 1069, 547]


def update(v):
    """ 'Arithmetic logic' from pdf """
    return (v * 607) % 990881


def calc_roll(x, face, possible_valid, u=0):
    """ For 'cracking' possible states.
    x: the value of x (x1,x2,x3,x4),
    face: the face of the card visible at 'x',
    possible_valid: list of possible z for a certain 'position' (x) """
    valid = lambda v: ((v - 1) * x + u) % 14 == face - 1  # noqa: ignore=E731
    return [update(val) for val in possible_valid if valid(val)]


def do_roll(u):
    """ Actually do a 'roll' and updating global (secret) z """
    global z
    z = [update(val) for val in z]
    r = [(((z[i] - 1) * x_coe[i] + u[i]) % 14) + 1 for i in range(NUM_CARDS)]
    return r

# Initially we guess u=0 and any value is possible for each position in z:
possible_z = [range(990881) for _ in range(NUM_CARDS)]
u = [0, 0, 0, 0]

for spin in range(10):
    cards = do_roll(u)

    print("Spin %d (u = %s). Cards: [%s]" % (spin + 1, u, "|".join(str(card) for card in cards)))

    # Update possible z for each position:
    for i in range(NUM_CARDS):
        possible_z[i] = calc_roll(x_coe[i], cards[i], possible_z[i], u[i])
        assert len(possible_z[i]) >= 1, "one or more z should always be found!"

        # Find which card (u) that will make the PRNG output the desired card on next turn:
        for u_candidate in range(14):
            if ((possible_z[i][0] - 1) * x_coe[i] + u_candidate) % 14 == 0:
                u[i] = u_candidate
    # print("I have [%s] possible z.\n" % "|".join(str(len(pos_z)) for pos_z in possible_z))
