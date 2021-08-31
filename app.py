from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


def model(x):
    query = [[x['day']] + [0 for i in range(24)]]
    query[0][x['hour'] + 1] = 1
    return round(lin_reg.predict(query)[0], 2)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        day = int(request.form.get('date')[-2:])
        hour = int(request.form.get('time')[0:2])
        message = model({'day': day, 'hour': hour})
        return render_template("index.html", message=message)
    return render_template("index.html")


if __name__ == '__main__':
    with open("C:/Users/user/anaconda notebooks/data/models/lin_reg.pkl", 'rb') as file:
        lin_reg = pickle.load(file)
    app.run(debug=True)
