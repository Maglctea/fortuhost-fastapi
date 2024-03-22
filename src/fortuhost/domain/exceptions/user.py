from fortuhost.domain.exceptions.base import AppException


class UserException(AppException):
    pass


class UserNotFoundException(UserException):
    pass


class AccessDeniedException(AppException):
    pass
