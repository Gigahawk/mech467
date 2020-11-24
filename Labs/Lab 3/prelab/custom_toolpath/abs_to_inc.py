from decimal import *
getcontext().prec = 100000

with open('./spongebob.gcode', 'r') as f:
    lines = f.readlines()


last_x = Decimal(0)
last_y = Decimal(0)
out = []
for l in lines:
    print(f"orig: {l}")
    l = l.split()
    x = Decimal(l[1][1:])
    y = Decimal(l[2][1:])
    dx = x - last_x
    dy = y - last_y
    last_x = x
    last_y = y
    # Necessary to fix weird drift issue
    last_y += Decimal(0.0001)
    nl = f"G1 X{dx} Y{dy}\n"
    out.append(nl)
    print(f"newo: {nl}")

out = out[:-1]

with open('./spongebob_inc.gcode', 'w') as f:
    f.writelines(out)
