from flask import Flask, render_template, request, url_for, redirect
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
    return render_template('post.html', post=post_data)


@app.route('/blog/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'GET':
        return render_template('blogbuilder.html')
    elif request.method == 'POST':
        id = CM.add_post(request.form.to_dict())
        if id:
            return redirect(url_for("post", blogid=id))


if __name__ == '__main__':
    app.run(debug=True)
