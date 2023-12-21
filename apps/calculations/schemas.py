from pydantic import BaseModel, EmailStr, constr, ValidationError, validator


class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    created_at: str
    is_active: bool

class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str

    @validator('username')
    def validate_username(cls, value):
        if not value.isalpha():
            raise ValueError('Имя пользователя должно состоять только из букв')
        return value

    @validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError('Пароль должен содержать не менее 8 символов')
        if not any(char.isdigit() for char in value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        return value

    @validator('email')
    def validate_email(cls, value):
        # Pydantic уже проверяет валидность email, но можно добавить кастомные условия
        if not value.endswith('example.com'):
            raise ValueError('Допустимы только email с доменом example.com')
        return value

    @validator('full_name')
    def validate_full_name(cls, value):
        if not value.strip():
            raise ValueError('Полное имя не должно быть пустой строкой')
        return value

# Схема для ответа с токеном
class Token(BaseModel):
    access_token: str

# Схема для входа пользователя (аутентификации)
class UserLogin(BaseModel):
    username: str
    password: str