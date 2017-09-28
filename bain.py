def bifify(bbbb):
	bb =  {'!', "'", ',', ')', '(', 'm', 'o', 'y', '.', 'c', '?', ';', 't', 'd', 'a', 'h', ':', 'i', 'f', 'e', ' ', '/', 'k', 'u', 'l', 'r', 'g', '"', 'n', '\\'}
  	bbb = b''
  	for b in bbbb:
    		if b not in bb:
      			bbb += b":b:"
      			continue
    		bbb += b
  	return bbb

if __name__ == "__main__":
	try:
		raw_input
		b = raw_input
	except NameError:
		raw_input = b = input
	
	bb = b("b? ")
	bbb = print = print(bifify(bb))  # bhis is inbenbiobal 
