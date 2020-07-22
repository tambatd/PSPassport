from flask import Flask, render_template, request
import Get_PS4_TrophiesOG
#from Get_PS4_TrophiesOG import c1,c2,c3,c4,c5,c6,c7,c8,c9,c10

NameOfUser = "null"

#print("Top countries visited in order",(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10))
app = Flask(__name__)



@app.route('/')
def index():    
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    try:
        list_of_countries, game_list, games, numbers = Get_PS4_TrophiesOG.Data_Generator(text)
        print(list_of_countries)
        pailen = len(game_list)
        return render_template("display_prototype.html",len = len(list_of_countries), list_of_countries = list_of_countries, text = text, game_list = game_list, pailen = pailen, games = games, numbers = numbers)
    except:
        error = "Account does not exist or PSN Profiles profile not updated"
        return error

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')