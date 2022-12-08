import main
from main import User

def test_create_user_returns_correctly_formatted_response():
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