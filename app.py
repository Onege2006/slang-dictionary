from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/last')
def last_page():
    return render_template('last.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/tik')
def tik():
    return render_template('tik.html')

@app.route('/tok')
def tok():
    return render_template('tok.html')

@app.route('/wok')
def wok():
    return render_template('wok.html')

@app.route('/zok')
def zok():
    return render_template('zok.html')

@app.route('/vok')
def vok():
    return render_template('vok.html')

@app.route('/uok')
def uok():
    return render_template('uok.html')

@app.route('/rok')
def rok():
    return render_template('rok.html')

@app.route('/pok')
def pok():
    return render_template('pok.html')

@app.route('/sok')
def sok():
    return render_template('sok.html')

@app.route('/ook')
def ook():
    return render_template('ook.html')

@app.route('/eok')
def eok():
    return render_template('eok.html')

@app.route('/dok')
def dok():
    return render_template('dok.html')

@app.route('/cok')
def cok():
    return render_template('cok.html')

@app.route('/bok')
def bok():
    return render_template('bok.html')
@app.route('/aok')
def aok():
    return render_template('aok.html')

if __name__ == '__main__':
    app.run(debug=True)
