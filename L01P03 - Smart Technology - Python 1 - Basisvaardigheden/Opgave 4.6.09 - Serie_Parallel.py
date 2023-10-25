weerstand1 = float(input("Geef weerstand 1: "))
weerstand2 = float(input("Geef weerstand 2: "))

serie = weerstand1 + weerstand2
if serie == 0.0:
    parallel = 0.0
else:
    parallel = weerstand1 * weerstand2 / serie

print("serie    : ", serie)
print("parallel : ", parallel)