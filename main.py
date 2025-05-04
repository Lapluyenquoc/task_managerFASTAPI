from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from fastapi.security import OAuth2PasswordBearer

# Khởi tạo ứng dụng FastAPI
app = FastAPI(
    title="Система управления задачами",
    description="REST API для создания, чтения, обновления и удаления задач.",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "email": "your.email@example.com",
    },
    swagger_ui_init_oauth={
        "clientId": "your-client-id",
        "scopes": "read write"
    }
)

# Cấu hình cơ sở dữ liệu SQLite
DATABASE_URL = "sqlite:///./task_manager.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)

# Tạo phiên làm việc (session)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Kết nối route
from routes import router
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в систему управления задачами!"}





