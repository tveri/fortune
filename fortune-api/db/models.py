import uuid
from enum import Enum

from sqlalchemy import ForeignKey, Column, String, Integer, Float, Boolean, DateTime, TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Role(str, Enum):
    SUPERADMIN_ROLE = 'SUPERADMIN_ROLE'
    ADMIN_ROLE = 'ADMIN_ROLE'
    GROUP_ADMIN_ROLE = 'GROUP_ADMIN_ROLE'
    CURATOR_ROLE = 'CURATOR_ROLE'
    TEACHER_ROLE = 'TEACHER_ROLE'
    STUDENT_ROLE = 'STUDENT_ROLE'
    USER_ROLE = 'USER_ROLE'
    
    

class User(Base):
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=True)
    roles = Column(ARRAY(String), nullable=False)
    is_disabled = Column(Boolean(), default=False)
    
    
class Student(Base):
    __tablename__ = 'students'
    
    user_id = Column(ForeignKey('users.id'), primary_key=True)
    group_id = Column(ForeignKey('groups.id'))
    educational_platform_id = Column(ForeignKey('educational_platforms.id'))
    course = Column(Integer, nullable=False)
    
    
class Curator(Base):
    __tablename__ = 'curators'
    
    user_id = Column(ForeignKey('users.id'), primary_key=True)
    educational_platform_id = Column(ForeignKey('educational_platforms.id'))
    
    
class Teacher(Base):
    __tablename__ = 'teachers'
    
    user_id = Column(ForeignKey('users.id'), primary_key=True)
    educational_platform_id = Column(ForeignKey('educational_platforms.id'))
    # taught_subject_ids = Column(ARRAY(ForeignKey('subjects.id')), nullable=False)  FIX_ME  doesnt work
    taught_subject_ids = Column(ARRAY(UUID), nullable=False) # Fast solution of ^
    
    
class EducationalPlatform(Base):
    __tablename__ = 'educational_platforms'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_en = Column(String, nullable=False)
    name_ru = Column(String, nullable=False)
    short_name_ru = Column(String, nullable=True)
    adress = Column(String, nullable=False)
    lat = Column(Float, nullable=True)
    lng = Column(Float, nullable=True)
    
    
class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_en = Column(String, nullable=False)
    name_ru = Column(String, nullable=False)
    short_name_ru = Column(String, nullable=True)
    curator_id = Column(ForeignKey('curators.user_id'))
    specialization_id = Column(ForeignKey('specializations.id'))
    
    
class Specialization(Base):
    __tablename__ = 'specializations'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_en = Column(String, nullable=False)
    name_ru = Column(String, nullable=False)
    short_name_ru = Column(String, nullable=True)
    time_to_study = Column(TIMESTAMP, nullable=False)
    
    
class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_en = Column(String, nullable=False)
    name_ru = Column(String, nullable=False)
    short_name_ru = Column(String, nullable=True)
    
    
class Chance(Base):
    __tablename__ = 'chances'
    
    user_id = Column(ForeignKey('users.id'), primary_key=True)
    chance_modifier = Column(Float, nullable=False)
    
    
class SpinStatistics(Base):
    __tablename__ = 'spin_statistics'
    
    player_id = Column(ForeignKey('users.id'), primary_key=True)
    host_id = Column(ForeignKey('users.id'), primary_key=True)
    spin_count = Column(Integer, default=0)
    win_count = Column(Integer, default=0)