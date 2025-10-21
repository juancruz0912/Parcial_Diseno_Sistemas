class ForestacionException(Exception):
    def __init__(self, error_code: str, message: str, user_message: str = None, cause: Exception = None):
        super().__init__(message)
        self._error_code = error_code
        self._user_message = user_message if user_message is not None else message
        self._cause = cause

    def get_error_code(self) -> str:
        return self._error_code

    def get_user_message(self) -> str:
        return self._user_message

    def get_full_message(self) -> str:
        return f"{self._error_code} - {self._user_message}"

    def __str__(self) -> str:
        base_str = self.get_full_message()
        if self._cause:
            return f"{base_str} | Causa: {self._cause}"
        return base_str

    @property
    def cause(self) -> Exception:
        return self._cause
