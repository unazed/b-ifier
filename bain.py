def bifify(bbbb):
	bb =  {'!', "'", ',', ')', '(', 'm', 'o', 'y', '.', 'c', '?', ';', 't', 'd', 'a', 'h', ':', 'i', 'e', ' ', '/', 'k', 'u', 'l', 'r', 'g', '"', 'n', '\\'}
	bbb = b''
	for b in bbbb:
		if b not in bb:
			bbb += b":b:"
			continue
		bbb += b
	return bbb

if __name__ == "__main__":
	b = b = raw_input
	bb = b("b? ")
	print(bifify(bb)) 
