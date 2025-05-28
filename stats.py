def counter(text):
        words = text.split()
        length = len(words)
        return length

def c_counter(text):
	totals = {}	

	for char in text:
		if char.lower() in totals:
			totals[char.lower()] = totals[char.lower()] +1
		else:
			totals[char.lower()] = 1
	return totals

def sort_on(dict):
    return dict["num"]

def sort(dict):
	list = []
	for key, value in dict.items():
		list.append({"char":key,"num":value})
	list.sort(reverse=True,key=sort_on)
	return list
