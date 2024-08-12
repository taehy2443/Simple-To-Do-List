from sqlalchemy.orm import Session
from src.database.models import Users

# 아래 설계한 컨트롤러를 만들어 넣기
def create_user(db: Session, user: Users, commit : bool = True):
    db.add(user)
    if commit:
        db.commit()
    return user

def get_user_by_id(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()