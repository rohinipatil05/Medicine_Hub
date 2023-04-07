from django.contrib import admin
from .models import Category,Product,Supplier,PaymentMaster,Contact
# Register your models here.

admin.site.site_header='Admin-Medicine Hub'
admin.site.site_title='Home'
admin.site.index_title='Dashboard'

class Category_Admin(admin.ModelAdmin):
    list_display = ('id','category_name')

class Product_Admin(admin.ModelAdmin):
    list_display = ('id','prod_name','category_id','supplier_id','prod_photo',
                        'prod_price','prod_quantity','prod_description',
                        'prod_treatment','prod_compostion','prod_type','prod_exp')

class Supplier_Admin(admin.ModelAdmin):
    list_display = ('id','sname','address','mobile','email')
   
class PaymentMasterAdmin(admin.ModelAdmin):
    list_display = ("cardno","cvv","expiry","balance")

class Contact_Admin(admin.ModelAdmin):
    list_display = ('uname','email','subject','messege')

admin.site.register(Category, Category_Admin)
admin.site.register(Product, Product_Admin)
admin.site.register(PaymentMaster,PaymentMasterAdmin)
admin.site.register(Supplier, Supplier_Admin)
admin.site.register(Contact, Contact_Admin)