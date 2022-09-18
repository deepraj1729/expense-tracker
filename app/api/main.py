from fastapi import FastAPI
from routes.dashboard import dashboard_router
from routes.profile import profile_router
from routes.transaction import transaction_router
from config.xpense import XpenseConfig
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=XpenseConfig.API.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#ALl the routes
app.include_router(dashboard_router)
app.include_router(profile_router)
app.include_router(transaction_router)