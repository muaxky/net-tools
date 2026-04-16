# net-tools.py

import math

# returns the subnet mask in array form for a provided prefix
def prefixToMaskArray(prefix):
	fillOctCount=math.floor(prefix/8)
	mask=[0,0,0,0]
	octIndex=0
	if fillOctCount>0:
		while octIndex<fillOctCount:
			mask[octIndex]=255
			octIndex+=1
	octBits=prefix%8
	if octBits>0:
		mask[octIndex]+=int(256-math.pow(2,8-octBits))
	return mask

# returns the subnet mask in string form for a given prefix
def prefixToMaskString(prefix):
	maskArray=prefixToMaskArray(prefix)
	maskString=""
	octIndex=0
	while octIndex<4:
		maskString+=str(int(maskArray[octIndex]))
		if octIndex<3:
			maskString+="."
		octIndex+=1
	return maskString
