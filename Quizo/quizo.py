import requests
import json
import sys

all_urls = {}
all_urls['GEOGRAPHY'] = "https://opentdb.com/api.php?amount=1&category=22&type=multiple"
all_urls['HISTORY'] = "https://opentdb.com/api.php?amount=1&category=23&type=multiple"
all_urls['POLITICS'] = "https://opentdb.com/api.php?amount=1&category=24&type=multiple"
all_urls['ART'] = " https://opentdb.com/api.php?amount=1&category=27&type=multiple"
all_urls['GENERAL KNOWLEDGE'] = "https://opentdb.com/api.php?amount=1&type=multiple"

class Player:

	def __init__(self, name):	#Initial values
		self.name = name
		self.score = 0
		self.level = 0
		self.level_increaser = 20

	def play(self):   #return user uppercase input in the gane
		user_move = input("""Enter your response: 

			""")
		user_move.upper()
		return user_move

	def show_score(self):			#display the score when asked
		return self.score

	def show_level(self):			#display the level
		return self.level

	def increase_score(self):			#increase_score after a win turn
		self.score += 10
		self.increase_level()
		print("================================================")
		print("Your score incrised to : {}".format(self.score))
		
	def increase_level(self):		#increase level after a win turn
		if self.score == self.level_increaser:
			self.level += 1
			self.level_increaser = self.level_increaser * 2
			print("================================================")
			print("Your level incrised to : {}".format(self.level))
	def getName(self):
		return self.name
		
	def __str__(self):
		return ("Hello, my name is {}". format(self.name))

possible_players = {}

def  players ():
	number_of_player = 0
	
	user_input = int(input("""How many players: """))

	while number_of_player < user_input:
		name_of_the_player = input ("Enter the {} player: ".format(number_of_player + 1))
		possible_players[number_of_player] = Player(name_of_the_player)
		number_of_player += 1
	
def choose_url (choice, url_dic):

	""" Return topic's url to play """

	for key, value in url_dic.items():
		if choice == key:
			return value
	if choice not in url_dic.keys():
		print ("No questions found")
		exit_input = input (""" Enter R to restart or enter E to exit: 

		""")
		exit_input.upper()
		if exit_input == "R": 
			pass
		else:
			sys.exit(0)

def mixt(correct, incorrect):   #mixt all the answers
	lst = []
	lst.append(correct.upper())
	for item in incorrect:
		lst.append (item.upper())
	new_lst = sorted(lst, key = lambda x : x[1:3], reverse = True)
	return new_lst


def get_answers(dico):						#get correct and incorect answers
	correct_answer = dico['correct_answer']
	incorrect_answers = dico['incorrect_answers']
	choices = mixt (correct_answer, incorrect_answers) 
	return correct_answer, incorrect_answers, choices

def get_question():
	pass

def game_play (dico):
	lst = list(dico.keys)

	for element in lst():
		print(element)

#game_play(all_urls)

game_to_play = input(""" Choose one topic to play :

	Geography
	Histpry
	Politics
	Art
	General Knowledge 

	""")

game_to_play = game_to_play.upper()   #the game to play in upper  to match keys in the dictionary

round_turn = 1

end_round = 2

players()

while round_turn <= end_round:	

	for people in possible_players.values():

		print ("Round : {}".format(round_turn))

		game_url = choose_url(game_to_play, all_urls)

		response = requests.get(url = game_url)

		data_questions = response.text

		data_questions = json.loads(data_questions)
		
		question = data_questions['results'][0]['question'] #capturing the question
		
		good_answer, bad_answers, multiple_choice = get_answers (data_questions['results'][0])  
		
		good_answer = good_answer.upper()

		count = 0
		for item in bad_answers:
			item.upper()
			bad_answers[count] = item
			count += 1

		count = 0
		for item in multiple_choice:
			item.upper()
			multiple_choice[count] = item
			count += 1

		print("This is your question {}" .format(people.getName()))

		print("================================================")

		print(question)

		#print(good_answer)

		count = 1

		for answer in multiple_choice:
			print("Choice {}: {}".format(count, answer.upper()))
			count += 1

		print ("Please use numbers: Ex: 1, 2, 3 or 4")

		user_answer = int(input(""" Give use your Answer: 

			"""))

		
		if multiple_choice.index(good_answer) + 1 == user_answer:
			print("Your answer is correct : {}".format(good_answer))
			people.increase_score()
			people.increase_level()
			break 
		else:
			print("================================================")
			print('The correct answer is : {}'.format(good_answer))
			print("Sorry, Try to do better next time")
			
		
	print ("score so far: ==================================== ")

	for people in possible_players.values():
		print("{} : Your score is: {} and Your level is {}".format(people.getName(), people.show_score(), people.show_level()))
	
	if round_turn == end_round:
		user_input = input(""" Do you want to continue or play again?:
			Yes/No 

			""")
		user_input = user_input.upper()

		if user_input == "YES":
			round_turn = 0	

	round_turn += 1
		
#choose the player who will play









write_doc = True
while write_doc == True:
	with open("text/questions.txt", "r") as file:
		text_file = requests.get("https://opentdb.com/api.php?amount=10&type=multiple")
		text_file = text_file.text
		#print(text_file)
		#file.write(text_file)
	write_doc = False


#===================== Variables ===================================
""" 
data_questions = url to retrieve all the data
game_to_play = a topic to play choosed by the user
Player = class for all the player
mixt = function that mixt all the answers
let_play = verify the interest of the player

""" 

#======================Funcyions ===================================
"""
players = function that determine the number of players
get_answer = function that get all the answers
choose_url = a function that returns the url
game_url = the function that retrieve data from the web 

"""

#======================Class=======================================
"""
Players

"""
#=======================Method ======================================
"""
show_level = display the level of a class instance
shw_score = display the score of a class instance
increase_level = increase the level of a class instance
increase_score = increase the score of a class instance

"""