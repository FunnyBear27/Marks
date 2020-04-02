from data import db_session, users
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("/mars_explorer.sqlite")
    app.run()


@app.route('/')
def index():
    session = db_session.create_session()
    job = session.query(users.Jobs)

    dict = {}
    dict['title of activity'] = job.job
    dict['name'] = job.team_leader
    dict['duration'] = job.work_size
    dict['list of collaborators'] = job.collaborators
    dict['is finished'] = job.is_finished

    return render_template('extend.html', **dict)


if __name__ == '__main__':
    main()
