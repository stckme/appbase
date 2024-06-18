from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY

from appbase.sa import (
    metadata,
    engine,
    Column_created,
    Column_id,
    Column_active,
    Column_pk_name,
)


users = Table(
    "users",
    metadata,
    Column_id(),
    Column("email", String, nullable=False, unique=True, index=True),
    Column("password", String),
    Column_created(),
    Column_active(),
    Column("groups", ARRAY(String), default=[]),
)

groups = Table(
    "groups",
    metadata,
    Column_created(),
    Column_active(),
    Column_pk_name(),
    Column("description", String),
)

group_users = Table(
    "group_users",
    metadata,
    Column_id(),
    Column("user_id", None, ForeignKey("users.id")),
    Column("group_name", String, nullable=False),
    Column_created(),
)

metadata.create_all(engine)
