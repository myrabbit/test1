import sys


def conver(s) : 

	nums = ""
	dot = False
	for c in s :
		if c.isdigit() or c == "." :
			if c == "." :
				if dot is False :
					dot = True 
				else :
					break
			nums += c

	number = round(float(nums),2)
	return "{:.2f}".format(number) 

if __name__ == "__main__" :
	
	if len(sys.argv) == 2 :
                s = sys.argv[1]
	else :
                s = "abc123.456"

	print(conver(s))
 
