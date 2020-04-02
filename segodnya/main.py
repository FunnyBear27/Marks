from data import db_session, users
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.run()


@app.route('/')
def index():
    session = db_session.create_session()
    jobs = session.query(users.Jobs).all()

    return render_template('extend.html', jobs=jobs)


if __name__ == '__main__':
    main()
