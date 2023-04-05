from flask import Flask, render_template, jsonify
 

app = Flask(__name__)

JOBS = [
  {
    "id":1,
    "title":"data analyst",
    'location' :"banglore",
    'salary' : 'rs 100000'
  },
  {
    "id":2,
    "title":"data analyst",
    'location' :"banglore",
    'salary' : 'rs 500000'
  },
{
    "id":3,
    "title":"data analyst",
    'location' :"banglore",
    'salary' : 'rs 800000'
  },
{
    "id":4,
    "title":"data analyst",
    'location' :"banglore",
    'salary' : 'rs 700000'
  },
{
    "id":5,
    "title":"data analyst",
    'location' :"banglore",
    'salary' : 'rs 900000'
  },{
    "id":6,
    "title":"data analyst",
    'location' :"banglore",
    'salary':"45345"
  }
]



@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")
def jobs_j():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)