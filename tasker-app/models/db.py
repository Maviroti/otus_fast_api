from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    url=config.settings.db.url,
    echo=config.settings.db.echo,
    pool_size=config.settings.db.pool_size,
    max_overflow=config.settings.db.max_overflow,
)


session_factory = sessionmaker(bind=engine)
