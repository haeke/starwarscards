from flask import Flask, render_template
from swapidata import Swapidata

app = Flask(__name__)

data = Swapidata('starwars')

#store all the information that I want to query
infom =  data.get_data()

count = 0
names = []
height = []
mass = []
eyecolor = []
birthyear = []
while( count < len(infom)):
    names.append(infom['results'][count]['name'])
    height.append(infom['results'][count]['height'])
    mass.append(infom['results'][count]['mass'])
    eyecolor.append(infom['results'][count]['eye_color'])
    birthyear.append(infom['results'][count]['birth_year'])

    count += 1


@app.route('/')
def index():

    return render_template('index.html', names=names, height=height, mass=mass, eyecolor=eyecolor, birthyear=birthyear)

@app.route('/index2')
def index_2():
    return render_template('index_2.html', names=names, height=height, mass=mass, eyecolor=eyecolor, birthyear=birthyear)


if __name__ == "__main__":
    app.run()
