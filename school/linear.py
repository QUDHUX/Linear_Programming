import pulp 

L = pulp.LpVariable('L', lowBound=0)
S = pulp.LpVariable('S', lowBound=0)

min_z = pulp.LpProblem("Minimize_Z", pulp.LpMinimize)
min_z += 800*L + 600*S 

min_z += L + S <= 9
min_z += 50*L + 40*S >= 400

min_z.solve()

print(L.varValue)
print(S.varValue)
print(pulp.value(min_z.objective))



