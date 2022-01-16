import secrets
import string
from datetime import datetime

import bcrypt

from .models import Claim, Role, User, UserClaims


def get_user_info(session, id):
    return (
        session.query(User, Claim.description, Role.description)
        .filter_by(id=id)
        .join(Role, User.role_id == Role.id)
        .join(UserClaims, User.id == UserClaims.user_id)
        .join(Claim, UserClaims.claim_id == Claim.id)
        .all()
    )


def create_user(session, data):
    if not "password" in data.keys():
        data["password"] = "".join(
            secrets.choice(string.ascii_letters) for i in range(8)
        )

    data["created_at"] = datetime.now()
    data["updated_at"] = datetime.now()
    data["password"] = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
    user = User(**data)
    session.add(user)
    session.commit()
    return user
