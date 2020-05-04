from flask import Flask, render_template
from utilities import ContentManager
app = Flask(__name__)

CM = ContentManager()


@app.route('/')
def index():
    posts = CM.get_posts()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
