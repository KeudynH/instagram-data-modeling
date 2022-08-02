import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    adress = Column(String(250), nullable=False)
    birth_day = Column(String(250), nullable=False)
    account_creation_date = Column(String(250), nullable=False)

class UserWall(Base):
    __tablename__ = 'UserWall'
    id = Column(Integer, primary_key=True)

class PublicWall(Base):
    __tablename__ = 'PublicWall'
    id = Column(Integer, primary_key=True)

class ReelsWall(Base):
    __tablename__ = 'ReelsWall'
    id = Column(Integer, primary_key=True)

class photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    User_comment = Column(String(250))
    likes = Column(Integer, nullable=False)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)
    UserWall_id = Column(Integer, ForeignKey('UserWall.id'))
    UserWall = relationship(UserWall)
    PublicWall_id = Column(Integer, ForeignKey('PublicWall.id'))
    User = relationship(PublicWall)

class video(Base):
    __tablename__ = 'video'
    id = Column(Integer, primary_key=True)
    User_comment = Column(String(250))
    likes = Column(Integer, nullable=False)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)
    UserWall_id = Column(Integer, ForeignKey('UserWall.id'))
    UserWall = relationship(UserWall)
    PublicWall_id = Column(Integer, ForeignKey('PublicWall.id'))
    User = relationship(PublicWall)

class reel(Base):
    __tablename__ = 'reel'
    id = Column(Integer, primary_key=True)
    User_comment = Column(String(100))
    likes = Column(Integer, nullable=False)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)
    UserWall_id = Column(Integer, ForeignKey('UserWall.id'))
    User = relationship(UserWall)
    PublicWall_id = Column(Integer, ForeignKey('PublicWall.id'))
    PublicWall = relationship(PublicWall)
    ReelsWall_id = Column(Integer, ForeignKey('ReelsWall.id'))
    ReelsWall = relationship(ReelsWall)

class follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)

class commentsP(Base):
    __tablename__ = 'commentsP'
    id = Column(Integer, primary_key=True)
    comment = Column(String(250), nullable=False)
    follower_id = Column(Integer, ForeignKey('follower.id'))
    User = relationship(follower)
    photo_id = Column(Integer, ForeignKey('photo.id'))
    photo = relationship(photo)

class commentsV(Base):
    __tablename__ = 'commentsV'
    id = Column(Integer, primary_key=True)
    comment = Column(String(250), nullable=False)
    follower_id = Column(Integer, ForeignKey('follower.id'))
    User = relationship(follower)
    video_id = Column(Integer, ForeignKey('video.id'))
    video = relationship(video)

class commentsR(Base):
    __tablename__ = 'commentsR'
    id = Column(Integer, primary_key=True)
    comment = Column(String(250), nullable=False)
    follower_id = Column(Integer, ForeignKey('follower.id'))
    User = relationship(follower)
    reel_id = Column(Integer, ForeignKey('reel.id'))
    reel = relationship(reel)

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e