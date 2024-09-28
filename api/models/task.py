from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base

class Task(Base):
    __tablename__="tasks"
    id=Column(Integer, primary_key=True)
    title=Column(String(1024))
    done= relationship("Done", back_populates="task", cascade="delete")
    # task.done を呼び出すと、そのタスクに関連する Done インスタンスが取得できます。
    # 逆に、Done インスタンスがあるときに done.task を呼び出すと、
    # その Done に関連する Task インスタンスが取得できます

class Done(Base):
    __tablename__= "dones"#donesテーブルに対応
    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)#tasksテーブルのIDが入る
    task= relationship("Task", back_populates="done")