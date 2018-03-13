def test_home_page(app):
    """
    GIVEN a Flask application
    WHEN the / page is requested
    THEN check the response
    """
    response = app.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask User Management Example!" in response.data
    assert b"Need an account?" in response.data
    assert b"Existing user?" in response.data


def test_login_page(app):
    """
    GIVEN a Flask application
    WHEN the /login page is requested
    THEN check the response
    """
    response = app.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_logging_in(app, database):
    """
    GIVEN a Flask application
    WHEN the /login page is posted to
    THEN check the response
    """
    response = app.post('/login',
                        data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome'),
                        follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for logging in, patkennedy79@gmail.com!" in response.data
    assert b"Welcome patkennedy79@gmail.com!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" in response.data
    assert b"Login" not in response.data
    assert b"Register" not in response.data
