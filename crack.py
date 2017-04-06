from random import randint

# Choose random z0:
z = [randint(0,990881) for _ in range(4)]

# Define "coefficients"
x_coe = [977, 607, 1069, 547]

def calc_roll(possible_valid, face, x, u = 0):
	""" For 'cracking' possible states.
	possible_valid: List of possible z for a certain 'position' (x),
	face: the face of the card visible at same position
	x: the value of x (x1,x2,x3,x4) """
	valid = []
	for val in possible_valid:
		if ((val - 1) * x + u) % 14 == face - 1:
			valid.append(val)

	# Prepare for next step:
	return [(val*607) % 990881 for val in valid]

def do_roll(u):
	""" Actually doing a 'roll' and updating global (secret) z """
	global z
	z = [(val*607) % 990881 for val in z] # update z
	r = [(((z[i] - 1) * x_coe[i] + u[i]) % 14) + 1 for i in range(4)]
	return r

# Initially we guess u=0 and any value is possible for each position in z:
possible_z = [range(990881) for _ in range(4)]
u = [0, 0, 0, 0]

for spin in range(10):
	cards = do_roll(u)

	print("Spin %d (u = %s). Cards: [%s]" % (spin+1, u, "|".join(str(card) for card in cards) ))

	# Update possible z for each position:
	for i in range(4):
		possible_z[i] = calc_roll(possible_z[i], cards[i], x_coe[i], u[i])
		assert len(possible_z[i]) >= 1, "one or more z should always be found!"
		for u_candidate in range(14):
			if ((possible_z[i][0] - 1) * x_coe[i] + u_candidate) % 14 == 0:
				u[i] = u_candidate
	#print("I have [%s] possible z.\n" % "|".join(str(len(pos_z)) for pos_z in possible_z))
