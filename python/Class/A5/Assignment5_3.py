import Assignment_Accept_String as a





def toString(string):
	return "".join(string)


def permute(string,start,end):
	if start == end:
		print( toString(string))
	else:
		for x in range(start,end+1):
			string[start], string[x] = string[x],string[start]
			permute(string,start+1,end)
			string[start], string[x] = string[x],string[start]






'''
def toString(List): 
    return ''.join(List) 

def permute(a, l, r): 
    if l == r: 
        print(toString(a))
    else: 
        for i in range(l, r + 1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l + 1, r) 
            a[l], a[i] = a[i], a[l] # backtrack 
'''
def main():
	string = list(a.acceptString());
	print(len(string)-1)
	result = permute(string,0,len(string)-1)

if __name__ == "__main__":
	main()
