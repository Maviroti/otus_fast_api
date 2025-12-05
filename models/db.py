from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    url=config.db_url,
    echo=config.db_echo,
    pool_size=config.sqla_pool_size,
    max_overflow=config.sqla_max_overflow,
)


session_factory = sessionmaker(bind=engine)
