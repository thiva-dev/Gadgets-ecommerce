from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,ProductForm
from .models import User,Product

# Create your views here.

def base (req):
    return render(req,'app/base.html')


def home(request):
    return render(request, 'app/home.html')

def about (req):
    return render(req, 'app/about.html')


def contact(req):
    return render(req, 'app/contact.html')

def signin(request):
    msg=""
    
    if request.method == "POST":
        form=RegisterForm(request.POST)
        email= request.POST.get("email")

        if User.objects.filter(email=email).exists():
            msg="Email already Exists"
        
        else:
           if form.is_valid():
            form.save()
            return redirect("login")
    else:
       form = RegisterForm()
    return render(request, 'app/signin.html', {'form':form, "msg":msg})



def login(request):
    mgs = ""


    if request.method == "POST":

        form = LoginForm(request.POST)

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username, password=password)

            request.session['username'] = user.username

            response = redirect("home")

            response.set_cookie('username', user.username)

            return response
        
        except User.DoesNotExist:
            mgs="invalid username or password"
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form':form, "mgs":mgs})

#product upload using POST

def uploadProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
        
    else:
        form = ProductForm()
    return render(request, 'app/Adminproduct.html', {'form':form})

# product get
def product(request):
    gadgets = Product.objects.all()

    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(title__icontains = query)

    else:
        products = Product.objects.all()

    return render (request, 'app/product.html', {"gadgets":gadgets, 'products':products})

#search :

def search_data(request):
    query = request.GET.get('q', "").strip()

    if query:
        products = Product.objects.filter(title__icontains = query)
    
    else:
        products = Product.objects.all()

    return render(request, 'app/search.html', {"products":products})


def addtocart(req, prod_id):
    cart = req.session.get("cart",{})
    prod_id=str(prod_id)
    if prod_id in cart:
        cart[prod_id]+=1
    else:
        cart[prod_id]=1
        req.session['cart']=cart
        return redirect("cart_view")
    
def deletocart(req, prod_id):
    cart = req.session.get("cart",{})
    prod_id=str(prod_id)
    if prod_id in cart:
        del cart[prod_id]

    req.session['cart'] = cart
    return redirect('cart_view')

def Cart(req):
    cart = req.session.get('cart', {})
    products = []
    total = 0

    for prod_id, quantity in cart.items():
        product = Product.objects.get(id=prod_id)
        product.quantity = quantity
        total += product.price*quantity
        products.append(product)
        req.session['cart'] = cart
    return render(req, 'app/cart.html', {'products':products, 'total':total})


