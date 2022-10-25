from flask import render_template
from app import app


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/favorite")
def favorite():
    actor_links = ["https://m.media-amazon.com/images/M/MV5BMjAwNTE2MDMyMl5BMl5BanBnXkFtZTgwMjAyODM3MTI@._V1_.jpg","https://m.media-amazon.com/images/M/MV5BMjI4NjM1NDkyN15BMl5BanBnXkFtZTgwODgyNTY1MjE@._V1_.jpg","https://phantom-marca.unidadeditorial.es/a86c01082aa1fb89d8c532b6431694e7/resize/1320/f/jpg/assets/multimedia/imagenes/2022/06/13/16551416152226.jpg","https://static.wikia.nocookie.net/bakerstreet/images/7/78/Robert_Downey_Jr._%282022\%29.jpg/revision/latest?cb=20220526032213","https://cdn.britannica.com/66/103066-050-B89D5EAF/Will-Smith-actor-musician-2006.jpg"]
    pop_artists = ["Selena Gomez", "Taylor Swift", "Justin Beiber", "Ed Sheeran","Lil Nas X"]
    actors = ["Selena Gomez", "Emma Stone", "Chris Evans" , "Robert Downey Jr.","Will Smith"]
    return render_template("favorite.html", act=actors,pop=pop_artists, links=actor_links)