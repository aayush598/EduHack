from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/feature')
def feature():
    return render_template('feature.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/single-blog')
def singleBlog():
    return render_template('single-blog.html')

if __name__ == '__main__':
    app.run(debug=True)