from flask import Flask, render_template
import random

def see(comment):
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        hello = comment
        return hello
    
    if __name__=="__main__":
        app.run()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_click')
def button_click():
    # ボタンがクリックされたときの処理を記述
    omikuji = random.randint(1,7)
    print(omikuji)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


