from models.models import Base
from repository.SessionSingleton import SessionSingleton

Base.metadata.drop_all(SessionSingleton.singleton().engine)
Base.metadata.create_all(SessionSingleton.singleton().engine)

