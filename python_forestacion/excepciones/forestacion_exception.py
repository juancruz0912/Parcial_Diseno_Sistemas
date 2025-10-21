class ForestacionException(Exception):
    """Excepción base para todos los errores específicos de la aplicación de forestación.

    Permite encapsular un código de error, un mensaje técnico, un mensaje para el usuario
    y la causa original de la excepción.
    """
    def __init__(self, error_code: str, message: str, user_message: str = None, cause: Exception = None):
        """Inicializa una nueva instancia de ForestacionException.

        Args:
            error_code (str): Código único que identifica el tipo de error.
            message (str): Mensaje técnico detallado de la excepción.
            user_message (str, optional): Mensaje amigable para el usuario. Si no se provee, usa `message`.
            cause (Exception, optional): La excepción original que causó esta excepción.
        """
        super().__init__(message)
        self._error_code = error_code
        self._user_message = user_message if user_message is not None else message
        self._cause = cause

    def get_error_code(self) -> str:
        """Obtiene el código de error de la excepción.

        Returns:
            str: El código de error.
        """
        return self._error_code

    def get_user_message(self) -> str:
        """Obtiene el mensaje amigable para el usuario de la excepción.

        Returns:
            str: El mensaje para el usuario.
        """
        return self._user_message

    def get_full_message(self) -> str:
        """Obtiene el mensaje completo de la excepción, incluyendo el código de error y el mensaje de usuario.

        Returns:
            str: El mensaje completo.
        """
        return f"{self._error_code} - {self._user_message}"

    def __str__(self) -> str:
        """Retorna la representación en cadena de la excepción.

        Returns:
            str: La representación en cadena de la excepción.
        """
        base_str = self.get_full_message()
        if self._cause:
            return f"{base_str} | Causa: {self._cause}"
        return base_str

    @property
    def cause(self) -> Exception:
        """Propiedad para acceder a la excepción original que causó esta excepción.

        Returns:
            Exception: La excepción original.
        """
        return self._cause
