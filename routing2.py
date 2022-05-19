from xml.sax import parseString
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def hello():
    return render_template('play.html')

@app.route('/many/<int:num>')
def many(num):
    return render_template('play2.html', play=num)

@app.route('/play/<int:num>/<color>')
def play_color(num, color):
    return render_template('play3.html', play=num, color=color)


if __name__== "__main__":
   app.run(debug=True)