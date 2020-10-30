import sys

table = [['0', '~)IGV3q[km'], ['1', '!_OHB4w]l,'], ['2', '@+PJN5e\\;', ''], ['3', "#Q{KM6ra'/"], ['4', '$W}L<7tsz'], ['5', '%E|:>8ydx'], ['6', '^RA"?9ufc'], ['7', '&TSZ`0igv'], ['8', '*YDX1-ohb'], ['9', '(UFC2=pjn']]

file = sys.argv[1]
code = open(file).read()

out = ""
for i in code:
	for j in table:
		if i in j[1]:
			out += j[0]

print(out)