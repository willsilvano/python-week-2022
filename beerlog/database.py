import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar
warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inheritc_cache = True

from sqlmodel import Session, create_engine
from beerlog.config import settings
from beerlog import models

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    return Session(engine)