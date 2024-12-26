from django.shortcuts import redirect, render
from django.views import View
from userapp.models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.


class register(View):
    def get(self, request):
        return render(request, 'administrator/register.html')

    def post(self, request):
        form = Turfownregform(request.POST)
        print(form)
        if form.is_valid():
            turf_admin = form.save(commit=False)
            username = request.POST['username']
            password = request.POST['password']
            print(username,password)
            turf_user = Userprofile.objects.create_user(
                username=username,
                password=password, 
                user_type='TURF',
            )
            turf_user.is_active = False 
            turf_user.save()

            turf_admin.Loginid = turf_user  
            turf_admin.approval_status = False
            turf_admin.save()

            # Get slots from POST data
            slots = request.POST.getlist("slots")
            for slot_time in slots:
                if slot_time.strip():  # Check for non-empty slot
                    Slot.objects.create(
                        turfid=turf_admin,
                        timeslot=slot_time.strip()
                    )

            return HttpResponse("Successfully registered")
        else:
            return render(request, 'administrator/register.html', {'form': form})




class Addproduct(View):
    def get(self, request):
        user_id = request.session['user_id']
        user_profile = Userprofile.objects.get(id=user_id)
        turfs = Turfadmin.objects.filter(Ownername=user_profile)  
        return render(request, 'turf/addproduct.html', {'turfs': turfs})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.Ownerid = Userprofile.objects.get(id=request.session['user_id'])
            product.turfid = Turfadmin.objects.get(id=request.POST['turfid'])  
            product.save()
            return HttpResponse('''<script>alert("Product added successfully.");window.location="/turfapp/viewproduct/";</script>''')
        return render(request, 'turf/addproduct.html', {'form': form})
    
class Viewproduct(View):
    def get(self, request):
        try:
            turfs =request.session['user_id']
            requests=Product.objects.filter(Ownerid=turfs)
        except Userprofile.DoesNotExist:
            return HttpResponse("Userprofile not found for the current user.", status=404)
        return render(request, 'turf/viewproduct.html', {'turfs': requests})

class Deleteproduct(View):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            product.delete() 
            return HttpResponse('''<script>alert("Product Delected successfully.");window.location="/turfapp/viewproduct/";</script>''')
        except Turfadmin.DoesNotExist:
            return render(request, 'turf/viewproduct.html', {'error': 'Turf not found'})
        
class Editproduct(View):
    def get(self, request, id):
        user_id = request.session['user_id']
        user_profile = Userprofile.objects.get(id=user_id)
        turfs = Turfadmin.objects.filter(Ownername=user_profile)  
        product = Product.objects.get(pk=id)
        form = ProductForm(instance=product)
        return render(request, 'turf/editproduct.html', {'product': form, 'turfs': turfs, 'current_turf': product.turfid})
