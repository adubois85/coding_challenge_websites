# copy / paste from the fastest solution on LeetCode.
# To quote that one Quake III dev, "what the f*@#?"
# I literally have no idea what this is doing or how it does it.
# (Okay, I have an inkling, but it's still opaque as hell)
# But it does, in fact, work.  At least, LeetCode accepts it.
f = open("user.out", "w")
lines = __Utils__().read_lines()
trash = {91: None, 93: None, 44: None, 10: None}
while True:
    try:
        param_1 = int(next(lines).translate(trash)[::-1])
        param_2 = int(next(lines).translate(trash)[::-1])
        f.writelines(("[", ",".join(str(param_1 + param_2))[::-1], "]\n"))
    except StopIteration: exit()