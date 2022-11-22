from flask import Flask, request, render_template
import random
import requests
import json

from character_dictionary import characters

app = Flask(__name__)
api_url = "https://swapi.py4e.com/api/"

@app.route('/starwars')
def starwars_facts():    
    character_fact = 'None.'
    character_id = request.args.get('character_id')
    if character_id:
        character_url = api_url + 'people/' + character_id
        response_api = requests.get(character_url)
        character_object = json.loads(response_api.content)
        film_list = character_object['films']
        films = []
        for film in film_list:
            film_response_api = requests.get(film)
            film_content = json.loads(film_response_api.content)
            films.append(film_content['title'])
        context = {
        'character_list': characters,
        'film_list': films,
        'character_object': character_object
        }
        return render_template('starwars.html', **context)


    context = {
        'character_list': characters,
    }
    return render_template('starwars.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
