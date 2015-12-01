import os
import gzip
# import math

# filename = 'newdata/out.brunson_corporate-leadership_corporate-leadership'

filenames = os.listdir('newdata')
for filename in filenames:
	if (filename[0] != '.'):
		filename = 'newdata/' + filename
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
				datas = line.split()
				# print datas
				if datas[0] != '%':
					if(len(datas) < 3):
						result.append(line + "1")
					else:
						result.append(line)
					total += 1
					for data in datas:
						# print data
						maxnum = max(maxnum, int(data))
					
		result[0] = str(maxnum + 1) + ' ' + str(maxnum + 1) + ' ' + str(total)
		final = '\n'.join(result)

		# f = open(filename + '.xx', 'w+')
		# f.write(final)
		# f.close()

		with gzip.open(filename + '.smat.gz', 'w+') as f:
			f.write(final)

# filename = 'out.brunson_club-membership_club-membership'

# filename = 'newdata/' + filename
# f = open(filename, 'r')
# content = f.read()
# f.close()
# result = ["xxx"]
# total = 0
# maxnum = 0

# lines = content.split('\n')

# for line in lines:
# 	print line
# 	if len(line) > 1:
# 		datas = line.split()
# 		print datas
# 		if datas[0] != '%':
# 			result.append(line + "1")
# 			total += 1
# 			for data in datas:
# 				print data
# 				maxnum = max(maxnum, int(data))
# 				print 'max is: ' + str(maxnum)
			
# result[0] = str(maxnum) + ' ' + str(maxnum) + ' ' + str(total)
# final = '\n'.join(result)

# # f = open(filename + '.xx', 'w+')
# # f.write(final)
# # f.close()

# with gzip.open(filename + '.gz', 'w+') as f:
# 	f.write(final)