from .start import start_router
from .commands import commands_router
from .convert import convert_router
from .timeframe import time_frame_router
from .menu import menu_router

routers = (start_router, commands_router, convert_router, time_frame_router, menu_router)
