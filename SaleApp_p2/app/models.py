from sqlalchemy import  Column,Integer,String,Float,Boolean,ForeignKey
from  sqlalchemy.orm import  relationship
from app import db,app
from flask_login import  UserMixin
class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False,unique=True)
    products = relationship('Product',backref='category',lazy=True)
    #backref tạo thuộc tính category trên lớp product
    def __str__(self):
        return  self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float,default=0)
    image = Column(String(100),default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
    active = Column(Boolean,default=True)
    category_id= Column(Integer,ForeignKey(Category.id),nullable=False)
    def __str__(self):
        return  self.name
class User(db.Model,UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50),nullable=False,unique=True)
    password = Column(String(50),nullable=False)
    avatar = Column(String(100),default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        import hashlib
        u = User(name='Admin', username='admin',password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()))
        db.session.add(u)
        db.session.commit()
        '''c1 = Category(name="Mobile")
        c2 = Category(name="Tablet")
        c3 = Category(name="Desktop")
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()

        c11 = Product(name="iPhone13",category_id=1)
        c22 = Product(name="Samsung Galaxy S23 Plus",category_id=1)
        c33 = Product(name="GF63 Thin",category_id=2)
        db.session.add(c11)
        db.session.add(c22)
        db.session.add(c33)
        db.session.commit()''''''
    #database-> reverse engineer để xem ERD'''