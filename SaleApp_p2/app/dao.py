def get_categories():
    return [{
        "id":1,
        "name":"Mobile"
    },{
        "id":2,
        "name":"Tablet"
    }]

def get_products(kw):
    products = [{
        "id":1,
        "name":"iPhone13",
        "price":20000000,
        "image":"https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id":1
    }, {
        "id": 2,
        "name": "Galaxy S23 Plus",
        "price": 19000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    },{
        "id": 2,
        "name": "Galaxy S23 Plus",
        "price": 19000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    },{
        "id": 2,
        "name": "Galaxy S23 Plus",
        "price": 19000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    },{
        "id": 2,
        "name": "Galaxy S23 Plus",
        "price": 19000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    },{
        "id": 2,
        "name": "Galaxy S23 Plus",
        "price": 19000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    },{
        "id": 2,
        "name": "Galaxy S23 Plus",
        "price": 19000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    } ]
    if kw: #vừa khác null vừa khác rỗng
        products = [p for p in products if p['name'].find(kw)>=0]

    return products