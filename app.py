from flask import Flask, render_template
from swapidata import Swapidata

app = Flask(__name__)

data = Swapidata('test')

#store all the information that I want to query
infom =  data.get_data()

count = 0
names = []
height = []
mass = []
eyecolor = []
birthyear = []
while( count < len(infom['results'])):
    names.append(infom['results'][count]['name'])
    height.append(infom['results'][count]['height'])
    mass.append(infom['results'][count]['mass'])
    eyecolor.append(infom['results'][count]['eye_color'])
    birthyear.append(infom['results'][count]['birth_year'])

    count += 1


@app.route('/')
def index():
    items =[]
    items.append(names)
    items.append(height)
    items.append(mass)
    items.append(eyecolor)
    items.append(birthyear)
    print items
    #return render_template('index.html', infom = infom)
    return render_template('index.html', items = items)

if __name__ == "__main__":
    app.run(debug=True)
