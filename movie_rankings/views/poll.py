import flask
import json
import movie_rankings.data as data
import movie_rankings.auth as auth


app_poll = flask.Blueprint('app_poll', __name__)


@app_poll.route('/polls/')
def view_all_polls():
    polls = data.get_polls(auth.current_user_id())
    for poll in polls:
        poll['choices'] = list(poll['choices'].values())
        poll['choices'].sort(key=lambda x: x['vote_count'], reverse=True)
    return flask.render_template('polls.html', c={
        'user': auth.get_user_context(auth.current_user_id()),
        'polls': polls
    })
