from django.shortcuts import render,redirect
from Admin.models import Category,Product,UserInfo,Supplier,PaymentMaster,Contact
from User.models import MyCart,OrderMaster
from django.contrib import messages
# Create your views here.

def index(request):
    cats = Category.objects.all()
    medicines = Product.objects.all()
    return render(request,'index.html',{"cats":cats,"medicines":medicines})
    

def store(request):
    medicines = Product.objects.all().order_by("prod_price")
    cats = Category.objects.all()    
   
    return render(request,'store.html',{"cats":cats,"medicines":medicines})
    
def login(request):
    cats = Category.objects.all() 
    if(request.method == "GET"):
        return render(request,"login.html",{"cats":cats})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        try:
            user = UserInfo.objects.get(uname=uname,password=password)
        except:
            return redirect(login)
        else:
            #Create the session
            request.session["uname"]=uname
            return redirect(index)

def register(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        return render(request,"register.html",{"cats":cats})
    else:
        uname = request.POST["uname"]
        phone =request.POST["phone"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = UserInfo(uname,phone,email,password)
        user.save()
        return redirect(register)
    

def ViewDetails(request,id):
    cats = Category.objects.all()
    medicine = Product.objects.get(id=id)
    #supplier = Supplier.objects.all()
    return render(request,"ViewDetails.html",{"medicine":medicine,"cats":cats})

def about(request):
    return render(request,"about.html",{})


def ShowMedicines(request,id):    
    #get method returns single object
    id = Category.objects.get(id=id) 
    #filter method returns multiple objects   
    medicines = Product.objects.filter(category_id = id)
    cats = Category.objects.all()    
    return render(request,"ShowMedicines.html",{"medicines":medicines,"cats":cats})

def allmedicines(request):
    cats = Category.objects.all()    
    return render(request,"allmedicines.html",{"cats":cats})

def contact(request):
    cats = Category.objects.all()    
    return render(request,"contact.html",{"cats":cats})
    
def nav(request):
    cats = Category.objects.all()
    medicines = Product.objects.all()
    return render(request,'carousel.html',{"cats":cats,"medicines":medicines})
   

def addToCart(request):
    if(request.method == "POST"):
        if("uname" in request.session):
            #Add to cart
            #User and Product
            medicineid = request.POST["medicineid"]
            user = request.session["uname"]
            qty = request.POST["qty"]
            medicine = Product.objects.get(id=medicineid)
            user = UserInfo.objects.get(uname = user)
            #check for duplicate entry
            try:
                cart = MyCart.objects.get(medicine=medicine,user=user)
            except:
                cart = MyCart()
                cart.user = user
                cart.medicine = medicine
                cart.qty = qty
                cart.save()
                return redirect(ShowAllCartItems)
            else:
                messages.success (request,"Already in cart") 
            return redirect(ShowAllCartItems)
        else:
            return redirect(login)

def ShowAllCartItems(request):
    cats = Category.objects.all()
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname = uname)
    if(request.method == "GET"):
        cartitems = MyCart.objects.filter(user=user)
        total = 0
        for item in cartitems:
            total+= item.qty*item.medicine.prod_price
        request.session["total"] = total
        return render(request,"ShowAllCartItems.html",{"items":cartitems,"cats":cats})
    else:
        id = request.POST["medicineid"]
        medicine = Product.objects.get(id=id)
        item = MyCart.objects.get(user=user,medicine=medicine)            
        qty = request.POST["qty"]
        item.qty = qty
        item.save() #Update
        return redirect(ShowAllCartItems)



def removeItem(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname = uname)
    id = request.POST["medicineid"]
    medicine = Product.objects.get(id=id)
    item = MyCart.objects.get(user=user,medicine=medicine)   
    item.delete()
    return redirect(ShowAllCartItems)


def signout(request):
    request.session.clear()
    return redirect(index)

def MakePayment(request):
    if(request.method == "GET"):
        return render(request,"MakePayment.html",{})
    else:
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = PaymentMaster.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
        except:
            return redirect(MakePayment)
        else:
            #Its a match
            owner = PaymentMaster.objects.get(cardno='101',cvv='111',expiry='12/25')
            owner.balance += request.session["total"]
            buyer.balance -=request.session["total"]
            owner.save()
            buyer.save()
            #Delete all items from cart
            uname = request.session["uname"]
            user = UserInfo.objects.get(uname = uname)
            
            order = OrderMaster()
            order.user = user
            order.amount = request.session["total"]
            #order.dateOfOrder = datetime.now
            #Fetch all cart items for that user
            details = ""
            items = MyCart.objects.filter(user=user)
            for item in items:
                details += (item.medicine.prod_name)+","
                item.delete()            
            order.details = details
            order.save()
            return redirect(thankyou)

def thankyou(request):
    cats = Category.objects.all()    
    return render(request,"thankyou.html",{"cats":cats})

def cthankyou(request):
    cats = Category.objects.all()    
    return render(request,"cthankyou.html",{"cats":cats})

def carousel(request):
    cats = Category.objects.all()    
    return render(request,"carousel.html",{"cats":cats})

def ShippingDetails(request):
    cats = Category.objects.all()    
    return render(request,"ShippingDetails.html",{"cats":cats})
    

    #cats = Category.objects.all()    
    #return render(request,"ShippingDetails.html",{"cats":cats})
    
def contact(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        return render(request,"contact.html",{"cats":cats})
    else:
        uname = request.POST["uname"]
        email =request.POST["email"]
        subject = request.POST["subject"]
        messege = request.POST["message"]
        user = Contact(uname,email,subject,messege)
        user.save()
        return redirect(cthankyou)

