from db.base import engine
from db.models import Base

Base.metadata.create_all(bind=engine)
print("DB updated")
