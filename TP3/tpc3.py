import re


string2 = "asdasdonasdasd12asdasd-12asdasdads-3asdasdao'912'2asdasd?ON=asndasdoooekeokkoo192=offasdasda12amsda1asmdkasd32'13asdlasdams==asdasdonasd78asdasd99asdasdoff="
string = """1iMRE7r=HtzkAon8o2sdXVtM0oLoffzNxZi4t5eqOpZNEqCJaLonK1mMTy3d22W
offaJ8uH6sgDxy2xMJoNRQZ7aAmkmhF4N91eTqqzequb4eYpA34DIojequZtnvw
6LyrPxme0eqZbYZPon82fFbYKoffQXTonOnjjAAzS4=eq1tKe0VQuS89yuoffL
oNCs8rV24P3Eeq1GeAtonjvTK0A5KmKAEaOon1=deqQcZrZ5MBu58HzkequWQ5
XC9Fon83ctoffFHaEQFtN9aIonfjAq9eqW0L6F9W4=eq=2pOQRUgAM56DKoffZ
6BYeq7sYononKZV=eq0K9KdW=VononAid6Uon6GeoffW=onD=OffonEQ=offG=3
9MoNyOn=EQOff7offOn5DSOffOn9OnW=43Uk=OffOnON"""
on = True
sum = 0
result = re.findall(r"([+-]?\d+)|(on|off)|(\=)", string, re.IGNORECASE)
matches = []
for tuple_result in result:
    for element in tuple_result:
        if element != '':
            matches.append(element)

for word in matches:
    if word.lower() == 'on':
        on = True
    elif word.lower() == 'off':
        on = False
    elif word == '=':
        print(sum)
    elif on:
        sum += int(word)

