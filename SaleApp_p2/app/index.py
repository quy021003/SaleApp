from flask import Flask, render_template,request
#import công cụ Flask và render template

import dao
#import file dao csl
app = Flask(__name__)
#Tạo mới đối tượng Flask tham số là name

@app.route("/")
#chỉ dẫn đường dẫn chạy file khi truy cập trang chủ
def index():
    kw = request.args.get('kw')
    cates = dao.get_categories()
    prods = dao.get_products(kw)
    return render_template('index.html',categories = cates,products = prods)
    #Vào thư mục templates tìm file index.html




if __name__ == '__main__':
    app.run(debug=True)