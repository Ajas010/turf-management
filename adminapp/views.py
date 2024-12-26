from django.shortcuts import redirect, render
from django.views import View
from turf.models import *

# Create your views here.


class AdminTurfApprovalView(View):
    def get(self, request):
        turf_registration = Turfadmin.objects.all()
        return render(request,'administrator/approve.html',{'users':turf_registration})
    
class UpdateYurfStatusView(View):
    def post(self,request,pk):
        turf = Turfadmin.objects.get(id=pk)
        action = request.POST.get('action')
        if action == 'approve':
            turf.status = 'approved'
            turf.loginid.is_active = True
            turf.logined.save()
        elif action == 'reject':
             turf.status = 'rejected'
             turf.logind .is_active = False
             turf.logind.save()  

             turf.save()
             return redirect('admin_turf_approval')
class adminviewuser(View):
    def get(self,request):
        return render(request,'administrator/adminviewuser.html')
    
class adminviewturf(View):
    def get(self,request):
        return render(request,'administrator/adminviewturf.html')
    
class adminviewbooking(View):
    def get(self,request):
        return render(request,'administrator/adminviewbooking.html')
    
class adminviewproduct(View):
    def get(self,request):
        return render(request,'administrator/adminviewproduct.html')
    
class adminviewrenting(View):
    def get(self,request):
        return render(request,'administrator/adminviewrenting.html')
        