from flask import Flask

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items = items)

@app.route('/add_new_item', methods = ['POST'])
def add_new_item():
    add_item(request.form.get('title'))
    return redirect(url_for('index'))
