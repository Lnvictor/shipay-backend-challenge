from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey, Integer,
                        String, UniqueConstraint)

from .base import base


class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role_id = Column("role_id", Integer, ForeignKey("roles.id"))
    created_at = Column(Date)
    updated_at = Column(Date)

    def __repr__(self):
        return self.email


class Claim(base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    active = Column(Boolean)

    def __repr__(self):
        return self.description


class Role(base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    description = Column(String)

    def __repr__(self):
        return self.description


class UserClaims(base):
    __tablename__ = "user_claims"

    user_id = Column("user_id", Integer, ForeignKey("users.id"), primary_key=True)
    claim_id = Column("claim_id", Integer, ForeignKey("claims.id"), primary_key=True)

    user_claims_un = UniqueConstraint("user_id", "claim_id", name="user_claims_un")
