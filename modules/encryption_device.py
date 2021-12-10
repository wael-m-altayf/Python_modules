from math import log
from random import choice
'''
--------------------------------------------------------------------------
------------------------------Update Log----------------------------------
Date: 19 Nov 2020_______V 0.3
*found a bug that prevents the program from decrypting the character that has the 0th index
 and fixed it.
____________________________
Date: 18 Nov 2020_______V 0.25
*fixed the decrypt method.
____________________________
Date: 17 Nov 2020_______V 0.2
*Added the decrypt method, it's still bugy.
____________________________ 
Date: 16 Nov 2020_______V 0.1
*Made the program.
---------------------------------How to use-------------------------------
--------------------------------           -------------------------------
1. make sure you have a 32 element list representing the encryption key; if you dont know 
   what to choose, that's ok, the program will Generate a random key for you, just dont provide
   the key parameter, the program will give the 'key' attribute to the object after an encryption.

2. The self.key attribute stores the text that you pass into the programm, declaring a self.encrypt
   method will encrypt that text, *Notice that encryption require text and decryption. 

3.if you dont have a key, the programm will generate a random key and assaign it to self.key. 

4.all letters must be written in upper case
--------------------------------------------------------------------------
--------------------------------------------------------------------------
'''
class encryption_device:
	'''initialization method, nothing fancy to look at here my friend...'''
	def __init__(self, text, key = dict()):
		self.text = text
		self.key = key
	'''the binary methond will convert an integer to a corresponding list of powers of two
	for example 17 is [4,0] while 7 is [2,1,0], the methond will add the length of the list -1 to the end of the list'''
	def __binary(self, number):
		'''to make a list for storing the powers of two'''
		loop_log_list = []
		'''to have a variable that stores the remanider of the logarithm'''
		remainder = number
		'''a loop to divide the number untill all the powers of two are found'''
		while remainder != 0:
			'''a variable to store the floor value of the log of 2'''
			loop_log = int(log(remainder,2))
			'''the program then adds the floor of the logarithm to the log list'''
			loop_log_list.append(loop_log)
			'''the remainder then gets updated in every end of the loop untill it reaches 0 and all powers of two are found'''
			remainder = remainder - 2**loop_log 
		'''the methond then returns the list plus the length of the list - 1  (to spice things up)'''
		return loop_log_list + [len(loop_log_list) - 1] 
	'''the inverse binary method will undo what the nasty binary method did'''
	def __inverse_binary(self, power_list):
		'''adding the number that will be added the value of every iteration'''
		number = 0
		'''a loop for adding the powers in the list'''
		for i in power_list:
			'''nothing complicated here..., just adding the powers of 2 for every number in the list'''
			number += 2**i
		'''and the method finally returns the value of the summation'''
		return number
	''' a method that returns the inverse of the characters of the set of numbers given a key'''
	def __nums_to_character(self, power_list):
		'''declaring a string that contains the characters used in encryption'''
		alphabet_str = "*ABCDEFGHIJKLMNOPQRSTUVWXYZ /#@&"
		'''this loop will check for every entry of the power list and see the matching index in the self.key dictionary'''
		for i in alphabet_str:
			'''going through the whole encrypted message and looking for a matching number'''
			for j in range(0,len(power_list)):
				'''checking if the values match...., Ahhh'''
				if power_list[j] ==  self.key[i]:
					'''setting the index value to that character'''
					power_list[j] = i 
		'''returning the modified power list ''' 
		return power_list
	'''the main method of encryption in the class, it returns an encrypted text that can be transmitted'''
	def encrypt (self):
		'''declaring a an inverse key dictionary to use in order to tangle every numercal representation of the litters and then have some fun'''
		lit_dict_inverse = { 1:'A',2:'B',3:'C',4:'D',
				     5:'E',6:'F',7:'G',8:'H',
				     9:'I',10:'J',11:'K',12:'L',
				     13:'M',14:'N',15:'O',16:'P',
				     17:'Q',18:'R',19:'S',20:'T',
				     21:'U',22:'V',23:'W',24:'X',
				     25:'Y',26:'Z',27:' ',28:'/',
				     29:'#',30:'@',31:'&',0:'*'}
		'''this is to declare an empty  encryption text that will get filled along the running'''
		encryption_text = []
		'''the following is to create a variable that stores the value of self.text and manipulate it'''
		text_string = self.text
		'''the condition under is to check if the user didn't provide a key or provided incorrect key, if 
		that was the case, the conditional will generate a random index list calling it [encryption_key]-notice that it's a list representaion of the key dictionary
		that random dictionary will then be stored in the self.key attribute'''
		if (self.key == []) or (len(self.key) != 32):
			'''again. this is to create an initial state in which the program will try to tangle things up.....hehehe'''
			lit_dict_inverse = { 1:'A',2:'B',3:'C',4:'D',
				     			 5:'E',6:'F',7:'G',8:'H',
				  	   			 9:'I',10:'J',11:'K',12:'L',
				    			 13:'M',14:'N',15:'O',16:'P',
				    			 17:'Q',18:'R',19:'S',20:'T',
				    			 21:'U',22:'V',23:'W',24:'X',
				    			 25:'Y',26:'Z',27:' ',28:'/',
				    			 29:'#',30:'@',31:'&',0:'*'}
			'''a variable that changes its value over every iteration of the below loop, it loses the element that the choice method "chooses"'''
			index_set = {0,1,2,3,4,5,6,7,8,9,10,
			     11,12,13,14,15,16,17,18,19,20,
			     21,22,23,24,25,26,27,28,29,30,31}
			'''declaring a variable to store a static value of len(index_key), that will be helpful during the action'''
			number = index_set
			'''emptying the box for new toys!'''
			encryption_key = []
			'''a loop thorough all the characters of the the self.key and tangling them along the way '''
			for i in range(0, len(number)):
				'''the main random choice function'''
				random_factor = choice(list(index_set))
				'''assaigning a value at the ith index at self.key'''
				self.key[lit_dict_inverse[i]] = random_factor
				'''removing the used index from the index set'''
				index_set = index_set - {random_factor}
				'''adding another toy toy to the box, did u think I'll forget about my own variable puns?'''
				encryption_key.append(random_factor)
		'''checking for every character and then applying the encryption'''		
		for i in range(0,len(text_string)):
			'''assaigning every encryption index number to its binary counterpart'''
			encryption_text += self.__binary(self.key[text_string[i]])
		return encryption_text
	'''the main methond of decryption in the class, it returns a decrypted text that can be read'''
	def decrypt(self, small_code = []):
		'''this is to add the little cropped code that the other side (Hopefully) sent'''
		self.text += small_code
		'''reversing the encrypted text will make stuff way more easier - wink* wink*'''
		self.text.reverse()
		'''an empty numbers index is all what you need to have some fun filling in the information'''
		numbers_index = []
		'''main loop of the method, it just uses some simple logic and stuff to generate a list of the numbers used in the encrypted message'''		
		encrypted_text = self.text
		for i in range(0,len(encrypted_text)):
			'''if i is zero then move on to the next one, it's as simple as that'''
			if (encrypted_text[i] == 'N'):
				continue
			'''preparing another empty list to have some fun...'''
			binary_list = list()
			'''now, this is where the 'fun' happens it checks for the cool stuff and then sets the next element that are in the range of the size - 1 thing to zero...'''
			for j in range(1, encrypted_text[i] + 2):
				'''adding the element to the once-empty list...'''				
				binary_list.append(encrypted_text[i + j])
				'''seting that elememt to zero, this will stop it from running any code below the if-i-is-zero conditional'''
				encrypted_text[i + j] = 'N'
			'''this will fill the once-empty list of numbers_index with the inverse_binary return value'''
			numbers_index.append(self.__inverse_binary(binary_list))
		'''after the loop concludes, it's time to reverse the list of the numbers_index'''
		numbers_index.reverse()
		'''declaring a variable for storing the value of decrypted message, after converting it to string'''
		result_text = ""
		'''the loop to fill the result_text variable '''
		for i in self.__nums_to_character(numbers_index):
			result_text += str(i)
		'''returning the value of the decrypted message'''
		return result_text
'''-----------------------------------------------------------------------
--------------------------------------------------------------------------'''
'''______________End of the calss, go grab a cup of tea......_____________'''
