from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)


from models.BaseModel import EntityMeta


class User(EntityMeta):
    __tablename__ = "user"

    id = Column(Integer, nullable=False)
    name = Column(String(45), nullable=False)
    department = Column(String(45), nullable=False)
    auth = Column(Integer, nullable=False)

    PrimaryKeyConstraint(id)

    def normalize(self):
        return{
            'user_id': self.id.__str__(),
            'user_name': self.name.__str__(),
            'user_department': self.department.__str__(),
            'user_auth': self.auth.__str__(),
        }