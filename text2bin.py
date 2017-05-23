import sys

if len(sys.argv) != 3:
	print 'Usage: text2bin.py <input text file> <output bin file>'
	exit()

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, 'rb') as f:
	inbuffer = f.read()
	outbuffer = ''
	for i in range(len(inbuffer)):
		binstr = bin(ord(inbuffer[i]))
		binstr = binstr.split('b')[1]
		outbuffer += ('0'*(8 - len(binstr)) + binstr) + '\n'
	with open(outfile, 'wb') as fw:
		fw.write(outbuffer)
