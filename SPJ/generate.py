# Procedurally generate the gridgraph instead of doing it by hand

a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'nil']


for n in range(len(a)):
    print("'", a[n+1], " M': [" "'", a[n+1], " L', '", a[n + 2], " M', '", a[n], " M'],", sep='')
