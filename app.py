from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('crypto_giveaways.csv')
    offers = df.to_dict(orient='records')
    return render_template('index.html', offers=offers)

if __name__ == '__main__':
    app.run(debug=True)
