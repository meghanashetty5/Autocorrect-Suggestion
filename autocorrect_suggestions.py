
word_list = open('words.txt').read().split()

import string
#IMPORTING STRING
#THIS SECTION CONTAINS FOR,WHILE,CONDITION,ERROR HANDLING
def str_input_type():
	while True:
		try:
			user_input = float(input("Press 1 to enter type in the text, Press 2 to input text file: "))
			while True:
				if user_input == 1:
					str_input_value = input("Enter your string/sentenance/essay here and press enter: ")
					str_input = str_input_value
					return str_input
					break
				elif user_input == 2:
					try:
						str_input_file = input("Enter the name of your file: ")
						str_input = " ".join((open('{}.txt'.format(str_input_file)).read().split()))
						return str_input
						break
					except FileNotFoundError:
						print("File not found. Enter correct file name and ensure it is a .txt file")
				else:
					print("User input not found. Enter number 1 or 2: ")
					break
		except ValueError:
			print("Invalid input. Please enter number 1 or 2: ")
			
#USING CLASSES			
class Autocorrect:
	def __init__(self):
		self.suggested_words = []
		
	def swap(self,str_input):
			for i in range(0,len(str_input)-1):
				words_list = []
				val_1 = str_input[i] 
				val_2 = str_input[i+1]
				for char in str_input:
					 words_list.append(char)  
				check_str = words_list
				check_str[i] = 	val_2
				check_str[i+1] = val_1
				check_str = "".join(check_str)
				if check_str.lower() in word_list:
					if check_str not in self.suggested_words:
						self.suggested_words.append(check_str)
				
	def replace(self,str_input):
			for i in range(0,len(str_input)):
				for j in string.ascii_lowercase:
					str_input_copy = str_input[:i]+j+str_input[i+1:]
					check_str = str_input_copy
					if check_str.lower() in word_list:
						if check_str not in self.suggested_words:
								self.suggested_words.append(check_str)
	
	def remove(self,str_input):
			for i in range(0,len(str_input)):
				if str_input[i].lower() in string.ascii_letters:
					for j in range(0,len(str_input)):
						check_str = str_input[:j]+str_input[j+1:]
						if check_str.lower() in word_list:
							if check_str not in self.suggested_words:
								self.suggested_words.append(check_str)
							
	def find_possible_words(self,str_input):
		self.suggested_words = []
		self.swap(str_input)
		self.replace(str_input)
		self.remove(str_input)
		return self.suggested_words
							
#USER DEFINEED FUNCTION			
def get_chosen_word(str_input,possible_words):
		print("You spelled this word incorrectly: ",word,".Did you mean to spell it like this: ",possible_words)
		value = input("Enter one of the corrected words or enter ignore to keep the word as is: ")
		if value.lower() == 'ignore':
			choosen_word = str_input
		else:
			choosen_word = value
		return choosen_word

#READING A FILE
word_list = open('words.txt').read().split()
input_string = str_input_type()
start_index = 0
autocorrector = Autocorrect()
output_string = ""
if input_string.find(" ") == -1:
	if input_string not in word_list:
			word = input_string
			index = len(input_string)
			possible_words = autocorrector.find_possible_words(input_string)
			chosen_word = get_chosen_word(input_string,possible_words)
			output_string = chosen_word + input_string[index:]
for index, char in enumerate(input_string):
	if char in string.punctuation or char == " " or char == '\n':
		if input_string[index-1] in string.punctuation or input_string[index-1] == " " or input_string[index-1] == '\n':
			start_index += 1
			output_string = output_string + char
			continue
		else:
			word = input_string[start_index:index]
			if word.lower() not in word_list:
				possible_words = autocorrector.find_possible_words(word)
				chosen_word = get_chosen_word(word,possible_words)
				output_string = output_string + chosen_word + char
			else:
				output_string = output_string + word + char
		if index != len(input_string)-1:
			start_index = index+1

#OUTPUTTING A FILE				
output = open('corrected_words.txt', 'w')					
problem4_output_file = open('corrected_words.txt', 'a')
problem4_output_file.write(output_string)
problem4_output_file.close()












