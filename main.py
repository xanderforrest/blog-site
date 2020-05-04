from flask import Flask, render_template
app = Flask(__name__)

posts = [{"heading": "First blog post", "short": "Introduction", "date": "1st May 2020", "intro": "THIS IS FIRST BLOG POST", "image": "/static/im.png"},
         {"heading": "Second blog post", "short": "Game", "date": "2nd May 2020", "intro": "second BLOG POST", "image": "/static/woh.png"}]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
