from typing import Annotated
from fastapi import Depends, Request

from app.registation_authentication_dependencies.schemas import Token
from app.services.session_services import SessionsService
from app.services.user_services import UsersService
from app.utils.uow import IUnitOfWork, UnitOfWork
from app.core import security

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]


async def get_users_service(uow: UOWDep) -> UsersService:
    return UsersService(uow)


async def get_sessions_service(uow: UOWDep) -> SessionsService:
    return SessionsService(uow)


users_service_dependency = Annotated[UsersService, Depends(get_users_service)]
sessions_service_dependency = Annotated[SessionsService, Depends(get_sessions_service)]
fingerprint_dependency = Annotated[str, Depends(security.get_fingerprint)]
tokens_dependency = Annotated[Token, Depends(security.get_tokens)]
