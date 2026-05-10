from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "codealpha"

# Product Data
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000,
        "image": "https://via.placeholder.com/250"
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 25000,
        "image": "https://via.placeholder.com/250"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 3000,
        "image": "https://via.placeholder.com/250"
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "price": 5000,
        "image": "https://via.placeholder.com/250"
    }
]

# Home Page
@app.route('/')
def home():
    return render_template('index.html', products=products)

# Product Details
@app.route('/product/<int:id>')
def product(id):
    selected_product = None

    for product in products:
        if product["id"] == id:
            selected_product = product

    return render_template('product.html', product=selected_product)

# Add To Cart
@app.route('/add_to_cart/<int:id>')
def add_to_cart(id):

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)
    session.modified = True

    return redirect('/cart')

# Cart Page
@app.route('/cart')
def cart():

    cart_products = []
    total = 0

    if "cart" in session:

        for item_id in session["cart"]:

            for product in products:

                if product["id"] == item_id:
                    cart_products.append(product)
                    total += product["price"]

    return render_template(
        'cart.html',
        cart=cart_products,
        total=total
    )

# Order Page
@app.route('/order')
def order():

    session.pop("cart", None)

    return render_template('order.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Register Page
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)