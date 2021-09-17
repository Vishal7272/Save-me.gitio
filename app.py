from flask import Flask,render_template,redirect,request

import function1
import function2
import function3
import function4


app = Flask(__name__) 

secret_word = None
word_set = None
to_display = None
tries = None
blanks = None


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
  
@app.route('/') 
def home(): 
    return render_template('home.html')


@app.route('/fruit_game')
def fruit_game():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	
	secret_word = function1.get_random_word()
	blanks = 0
	to_display = []
	word_set = "abcdefghijklmnopqrstuvwxyz"
	for i,char in enumerate(secret_word):
		if char==" ":
			to_display.append(" ")
			
		else:
			to_display.append("_")
			blanks+=1

	tries = 0
	return render_template('fruit_game.html',secret_word=secret_word,to_display=to_display,tries="/static/img/hangman%d.png"%tries)

@app.route('/sport_game')
def sport_game():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	
	secret_word = function2.get_random_word()
	blanks = 0
	to_display = []
	word_set = "abcdefghijklmnopqrstuvwxyz"
	for i,char in enumerate(secret_word):
		if char==" ":
			to_display.append(char)
		
		else:
			to_display.append("_")
			blanks+=1

	tries = 0
	return render_template('sport_game.html',to_display=to_display,secret_word=secret_word,tries="/static/img/hangman%d.png"%tries)

@app.route('/cricket_personality')
def cricket_personality():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	
	secret_word = function3.get_random_word()
	blanks = 0
	to_display = []
	word_set = "abcdefghijklmnopqrstuvwxyz"
	for i,char in enumerate(secret_word):
		if char==" ":
			to_display.append(" ")
			
		else:
			to_display.append("_")
			blanks+=1

	tries = 0
	return render_template('cricket_personality.html',secret_word=secret_word,to_display=to_display,tries="/static/img/hangman%d.png"%tries)


@app.route('/states')
def states():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	
	secret_word = function4.get_random_word()
	blanks = 0
	to_display = []
	word_set = "abcdefghijklmnopqrstuvwxyz"
	for i,char in enumerate(secret_word):
		if char==" ":
			to_display.append(" ")
			
		else:
			to_display.append("_")
			blanks+=1

	tries = 0
	return render_template('states.html',secret_word=secret_word,to_display=to_display,tries="/static/img/hangman%d.png"%tries)


@app.route('/guess_fruit',methods=["POST"])
def guess_fruit():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	

	letter = request.form["letter"]
	
	chance_lost = True
	for i,char in enumerate(secret_word):
		if char==letter and letter in word_set:
			chance_lost = False
			to_display[i] = letter
			blanks-=1
	word_set = word_set.replace(letter,'')
	if chance_lost==True:
		tries += 1
		if tries==6:
			return redirect('/game_lost')
	if blanks==0:
		return redirect('game_won')
	return render_template('fruit_game.html',to_display=to_display,secret_word=secret_word,tries="/static/img/hangman%d.png"%tries)


@app.route('/guess_sport',methods=["POST"])
def guess_sport():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	

	letter = request.form["letter"]
	
	chance_lost = True
	for i,char in enumerate(secret_word):
		if char==letter and letter in word_set:
			chance_lost = False
			to_display[i] = letter
			blanks-=1
	word_set = word_set.replace(letter,'')
	if chance_lost==True:
		tries += 1
		if tries==6:
			return redirect('/game_lost')

	if blanks==0:
		return redirect('game_won')
	return render_template('sport_game.html',to_display=to_display,secret_word=secret_word,tries="/static/img/hangman%d.png"%tries)


@app.route('/guess_personality',methods=["POST"])
def guess_personality():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	

	letter = request.form["letter"]
	
	chance_lost = True
	for i,char in enumerate(secret_word):
		if char==letter and letter in word_set:
			chance_lost = False
			to_display[i] = letter
			blanks-=1
	word_set = word_set.replace(letter,'')
	if chance_lost==True:
		tries += 1
		if tries==6:
			return redirect('/game_lost')

	if blanks==0:
		return redirect('game_won')
	return render_template('cricket_personality.html',to_display=to_display,secret_word=secret_word,tries="/static/img/hangman%d.png"%tries)


@app.route('/guess_state',methods=["POST"])
def guess_state():
	global secret_word
	global word_set
	global to_display
	global tries
	global blanks	

	letter = request.form["letter"]
	
	chance_lost = True
	for i,char in enumerate(secret_word):
		if char==letter and letter in word_set:
			chance_lost = False
			to_display[i] = letter
			blanks-=1
	word_set = word_set.replace(letter,'')
	if chance_lost==True:
		tries += 1
		if tries==6:
			return redirect('/game_lost')

	if blanks==0:
		return redirect('game_won')
	return render_template('states.html',to_display=to_display,secret_word=secret_word,tries="/static/img/hangman%d.png"%tries)


@app.route('/game_lost')
def game_lost_landing():
	return render_template('game_lost.html')

@app.route('/game_won')
def game_won():
	return render_template('game_won.html')

if __name__ == '__main__': 
    app.run(debug = True) 
