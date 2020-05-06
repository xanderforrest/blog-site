from flask import Flask, render_template
from utilities import ContentManager
app = Flask(__name__)

CM = ContentManager()


@app.route('/')
def index():
    return "Hello"


@app.route('/blog')
def blog():
    posts = CM.get_posts()
    return render_template('blog.html', posts=posts)


@app.route('/blog/<blogid>')
def post(blogid):
    post_data = CM.get_post(blogid)
    return str(post_data)


if __name__ == '__main__':
    app.run(debug=True)
