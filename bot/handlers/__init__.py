from .start import start_router
from .commands import commands_router
from .convert import convert_router

routers = (start_router, commands_router, convert_router)
