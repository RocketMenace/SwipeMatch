from app.repository.user_repository import UserRepository
from app.services.user_services import UserService


def user_service():
    return UserService(UserRepository)
