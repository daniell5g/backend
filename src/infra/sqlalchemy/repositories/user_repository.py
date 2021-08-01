from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas.schema import UserSchema
from src.infra.sqlalchemy.models.user_model import UserModel

class UserRepository():
    def __init__(self, db: Session):
        self.db = db

    def index(self):
        stmt = select(UserModel)
        users = self.db.execute(stmt).scalars().all()
        return users

    def create(self, user: UserSchema):
        db_user = UserModel(
            name=user.name,
            document=user.document,
            pis=user.pis,
            email=user.email,
            password=user.password,
            zipcode=user.zipcode,
            address=user.address,
            number=user.number,
            complement=user.complement,
            city=user.city,
            state=user.state,
            country=user.country,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, id: int, user: UserSchema):
        stmt = update(UserModel).where(UserModel.id == id).values(
            name=user.name,
            document=user.document,
            pis=user.pis,
            email=user.email,
            password=user.password,
            zipcode=user.zipcode,
            address=user.address,
            number=user.number,
            complement=user.complement,
            city=user.city,
            state=user.state,
            country=user.country,
        )
        self.db.execute(stmt)
        self.db.commit()
        return {'message': 'Usuário atualizado com sucesso.'}

    def show(self, user_id: int):
        stmt = select(UserModel).where(UserModel.id == user_id)
        user = self.db.execute(stmt).scalars().first()
        return user

    def destroy(self, user_id: int):
        stmt = delete(UserModel).where(UserModel.id == user_id)
        self.db.execute(stmt)
        self.db.commit()
        return {'message': 'Usuário deletado com sucesso.'}
