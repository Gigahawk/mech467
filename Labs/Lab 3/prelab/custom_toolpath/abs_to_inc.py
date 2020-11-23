with open('./spongebob.gcode', 'r') as f:
    lines = f.readlines()

last_x = 0
last_y = 0
out = []
for l in lines:
    l = l.split()
    x = float(l[1][1:])
    y = float(l[2][1:])
    dx = x - last_x
    dy = y - last_y
    last_x = x
    last_y = y
    nl = f"G1 X{dx} Y{dy}\n"
    out.append(nl)
    print(nl)

out = out[:-1]

with open('./spongebob_inc.gcode', 'w') as f:
    f.writelines(out)
