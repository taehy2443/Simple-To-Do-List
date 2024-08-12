from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


# class 명은 마음대로 바꿔도 됨
class Users(Base):
    __tablename__ = "users" # 여기에 테이블 이름
    # 이건 건들지 말기
    id = Column(Integer, primary_key=True, index=True)

    # 아래 원하는 컬럼 추가
    # user_id = Column(Integer, primary_key=True)
    # summoner_id = Column(String, nullable=False, unique=True, index=True)
    # puuid = Column(String, nullable=True, index=True)



# 여러개도 가능
class MatchIds(Base):
    __tablename__ = "match_ids" # 중복 안됨
    match_id = Column(Integer, primary_key=True, index=True)
    riot_match_id = Column(String, nullable=False, unique=True, index=True)
    crawled = Column(Boolean, nullable=False, default=False)
    crawled_count = Column(Integer, nullable=False, default=0)
    region = Column(String, nullable=False)
    
    # 이러면 created_at과 updated_at이 자동으로 생성됨
    created_at = Column(DateTime, server_default=current_timestamp())
    updated_at = Column(DateTime, server_default=current_timestamp(), onupdate=current_timestamp())


# 데이터베이스 생성
Base.metadata.create_all()