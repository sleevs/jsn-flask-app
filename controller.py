from flask import Flask , render_template ,jsonify
from werkzeug.wrappers.response import ResponseStream


app = Flask(__name__)

@app.route('/')
def home_page():
     return render_template('index.html')


@app.route('/market')
def market_page():
     return render_template('market.html')


@app.route('/teste')
def teste():
     valor = "VALOR"
     responseTeste = {'TESTE':valor}
     return jsonify(responseTeste)


app.run()