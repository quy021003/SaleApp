from sqlalchemy import  Column,Integer,String,Float,Boolean,ForeignKey
from  sqlalchemy.orm import  relationship
from app import db,app

class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False,unique=True)
    products = relationship('Product',backref='category',lazy=True)
    #backref tạo thuộc tính category trên lớp product


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float,default=0)
    image = Column(String(100),default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg")
    active = Column(Boolean,default=True)
    category_id= Column(Integer,ForeignKey(Category.id),nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        '''c1 = Category(name="Mobile")
        c2 = Category(name="Tablet")
        c3 = Category(name="Desktop")
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()'''

        '''c1 = Product(name="iPhone13",category_id=1)
        c2 = Product(name="Samsung Galaxy S23 Plus",category_id=1)
        c3 = Product(name="GF63 Thin",category_id=2)
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()'''
        p = Product.query.get(2)
        p.price = 22
        db.session.add(p)
        db.session.commit()
    #database-> reverse engineer để xem ERD