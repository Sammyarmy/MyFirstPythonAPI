import main
from main import User

def test_user_initialiser():
    user = User(username="test_username", password = "test_password", email= "test@email.com", phone_number=123)
    assert user.username == "test_username"
    assert user.password == "test_password"
    assert user.email == "test@email.com"
    assert user.phone_number == 123

def test_post_user():
    user = User(username="test_username", password = "test_password", email= "test@email.com", phone_number=123)
    result = main.create_user(user)
    print("test post")
    assert result == {
                        'message': 'New User created',
                        'user_info': 
                            {'email': 'test@email.com',
                            'password': 'test_password',
                            'phone_number': 123,
                            'username': 'test_username'},
                    }