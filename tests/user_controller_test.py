from app.main import User, create_user, root

def test_root_returns_correct_response():
    result = root()
    assert result == {"message: Welcome to my API"}

def test_create_user_returns_correctly_formatted_response():
    user = User(username="test_username", password = "test_password", email= "test@email.com", phone_number=123)
    result = create_user(user)
    assert result == {
                        'message': 'New User created',
                        'user_info': 
                            {'email': 'test@email.com',
                            'password': 'test_password',
                            'phone_number': 123,
                            'username': 'test_username'},
                    }