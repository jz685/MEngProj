import os
import gzip

filename = 'newdata/out.brunson_corporate-leadership_corporate-leadership'

f = open(filename, 'r')
content = f.read()
f.close()
result = ["xxx"]
total = 0
maxnum = 0

lines = content.split('\n')

for line in lines:
	# print line
	if len(line) > 1:
		datas = line.split(' ', 1)
		print datas
		if datas[0] != '%':
			result.append(line + "1")
			total += 1
			for data in datas:
				print data
				maxnum = max(maxnum, data)
			
result[0] = str(maxnum) + ' ' + str(maxnum) + ' ' + str(total)
final = '\n'.join(result)

# f = open(filename + '.xx', 'w+')
# f.write(final)
# f.close()

with gzip.open(filename + '.gz', 'w+') as f:
	f.write(final)
