from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username="ian", email="ian@vscn.com", password="senha")

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == "ian@vscn.com"))

    assert result.username == "ian"
