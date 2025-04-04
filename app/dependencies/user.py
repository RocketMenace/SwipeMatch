from app.services.user_services import UserService
from app.repository.user_repository import UserRepository

def user_service():
    return UserService(UserRepository)