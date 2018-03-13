import pytest
from project import create_app, db
from project.models import User


@pytest.fixture(scope='session')
def app(request):
    flask_app = create_app('flask_test.cfg')
    # flask_app.testing = True

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    return flask_app.test_client()


@pytest.fixture(scope='session')
def database(app, request):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    print('Creating new users...')
    user1 = User(email='patkennedy79@gmail.com', plaintext_password='FlaskIsAwesome')
    user2 = User(email='kennedyfamilyrecipes@gmail.com', plaintext_password='PaSsWoRd')
    user3 = User(email='blaa@blaa.com', plaintext_password='MyFavPassword')
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # Commit the changes for the users
    db.session.commit()

    def teardown():
        db.drop_all()

    request.addfinalizer(teardown)
    return db
