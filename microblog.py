from app import create_app, db, cli
from app.models import User, Post, Notification, Message, Task

from app.email import send_email
from threading import Thread

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification, 'Task': Task}


def ping_elasticsearch(app):
    with app.app_context():
        if not app.elasticsearch.ping():
            app.elasticsearch = None

            send_email('[Microblog] Elasticsearch server cannot be reached',
                       sender=app.config['MAIL_DEFAULT_SENDER'],
                       recipients=[app.config['MAIL_DEFAULT_SENDER']],
                       text_body='Elasticsearch server cannot be reached.',
                       html_body='Elasticsearch server cannot be reached.')


# startup code, runs once
with app.app_context():
    if app.elasticsearch:
        Thread(target=ping_elasticsearch, args=[app]).start()
