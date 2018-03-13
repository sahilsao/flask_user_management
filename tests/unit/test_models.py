from project.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    new_user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.hashed_password != 'FlaskIsAwesome'
    assert not new_user.authenticated
    assert new_user.role == 'user'


def test_setting_password():
    """
    GIVEN an existing user
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    new_user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
    new_user.set_password('MyNewPassword')
    assert new_user.hashed_password != 'MyNewPassword'
    assert new_user.is_correct_password('MyNewPassword')
    assert not new_user.is_correct_password('MyNewPassword2')
    assert not new_user.is_correct_password('FlaskIsAwesome')
