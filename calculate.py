# translate user input and put a hong kong accent on it
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template

from contextlib import closing

# configuration

# application:
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent = True) # if there is no FLASKR_SETTINGS, then run the one below
app.config.from_object(__name__)
     
# variables...
# generate a random question:
question = 'Cu'
   
@app.route('/')
def translate():
    return render_template('translate.html', question_text=question)
    
@app.route('/translate', methods=['POST'])
def add_entry():  


    # question -> answer dict
    q_and_a_dict = {'Cu' : 'Copper', '2H20(l) (dceomposition of hydrogen peroxide)' : '2H2O(l) + O2'}

    # get the answer from the dict
    if question in q_and_a_dict:
	answer = q_and_a_dict[question]
    else:
	answer = "question or answer was incorrect"


    return render_template('translate.html', word=answer)
    
if __name__ == '__main__':
    app.run()
