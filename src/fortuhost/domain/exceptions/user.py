from fortuhost.domain.exceptions.base import AppException


class UserException(AppException):
    pass


class UserNotFoundError(UserException):
    pass


class AccessDeniedError(AppException):
    pass
