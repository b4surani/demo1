from flask import Flask

all_records = [
{
"name" : "Radiohead",
"albums" : [
{
"title":"The King of Limbs",
"songs":[
...
],
"description":"..."
},
{
"title":"OK Computer",
"songs":[],
"description":"..."
}
]
},
{
"name":"Portishead",
"albums":[
{
"title":"Dummy",
"songs":[],
"description":"..."
},
{
"title":"Third",
"songs":[],
"description":"..."
}
]
}
]

app = Flask(__name__)

@app.route('/')
def hello():
	retunr "<h1>Hello week 5 part 2</h1>"

if __name__ == '__main__':
	app.run(host='0.0.0.0')
