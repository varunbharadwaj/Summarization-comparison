import wikipedia


def summarize(content,num):
	#Step 1: Make an intersection function which forumulates the intersection between two sentences, as in, takes two sentences and finds the number of common words between them.
	#Step 2: Split the content into sentences, and find the intersection of each sentence with all the other sentences in the content.
	matrix = []
	sentences = content.split('.')
	sentences.remove('')
	for x in range(0,len(sentences)):
		sentences[x] = sentences[x].strip();
	final_arr = sentences[:]
	
	for l in range(0,len(sentences)):
		matrix.append([])
		for m in range(0,len(sentences)):
			matrix[l].append(0)
	for i in range(0,len(sentences)):
		for j in range(i+1,len(sentences)):
			val = intersection(sentences[i],sentences[j])
			matrix[i][j] = val
			matrix[j][i] = val
	sum_matrix = []
	for b in range(0,len(sentences)):
		sum_matrix.append(0)
		for c in range(0,len(sentences)):
			sum_matrix[b]+=matrix[b][c]
	
	selection_sort(sentences,matrix,sum_matrix)
	index_array = []
	for x in sentences[0:num]:
		index_array.append(final_arr.index(x))
	sentences = sentences[0:num]
	selection_sort_asc(sentences,index_array)
	return sentences




def intersection(line1,line2):
	words1 = line1.split(' ')
	words2 = line2.split(' ')
	val = 0
	for i in words1:
		for j in words2:
			if(i == j):
				val+=1
	return val


def selection_sort(sentences,words_matrix,matrix):
	for i in range(0,len(matrix)-1):
		maximum = matrix[i]
		key = i
		for j in range(i+1,len(matrix)):
			if(maximum<matrix[j]):
				maximum = matrix[j]
				key = j
		swap(matrix,i,key)
		swap(words_matrix,i,key)
		swap(sentences,i,key)


def selection_sort_asc(sentences,matrix):
	for i in range(0,len(matrix)-1):
		minimum = matrix[i]
		key = i
		for j in range(i+1,len(matrix)):
			if(minimum>matrix[j]):
				minimum = matrix[j]
				key = j
		swap(matrix,i,key)
		swap(sentences,i,key)


def swap(matrix,i,j):
	temp = matrix[i]
	matrix[i] = matrix[j]
	matrix[j] = temp
			


def print_summ(summary):
	for i in range(0,len(summary)):
		print('-> ',summary[i])
	
	print()

topic = input('Enter the topic you want to summarize: ')
num_sentences = int(input('Enter the number of sentences in your summary: '))
content = wikipedia.summary(topic)
extraction_summary = summarize(content,num_sentences)
print('Your topic summary is:')
print_summ(extraction_summary)
