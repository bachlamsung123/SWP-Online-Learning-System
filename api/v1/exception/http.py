from fastapi import HTTPException


class ForbiddenException(HTTPException):
    def __init__(self, detail:str = "You don't have permission to access this resource"):
        super().__init__(status_code=403, detail=detail)


class NotFoundException(HTTPException):
    def __init__(self, detail="Not Found"):
        super().__init__(status_code=404, detail=detail)


class CredentialException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
