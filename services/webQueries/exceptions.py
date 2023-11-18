class BaseError(Exception):
    def __init__(self, message: object, extra_inf: object = None) -> None:
        super().__init__(message)
        self.message = message
        self.extra_inf = extra_inf

    def __str__(self) -> str:
        if self.extra_inf:
            return f'Error: {self.message}\nDetails: {self.extra_inf}'
        return f'Error: {self.message}'


class ApiException(BaseError):
    def __init__(self, message: object, extra_inf: object = None) -> None:
        super().__init__(message, extra_inf)


class InvalidEndpoint(BaseError):
    def __init__(self, message: object, extra_inf: object = None) -> None:
        super().__init__(message, extra_inf)
