from django.shortcuts import redirect, render
from backend.models import Student


# Create your views here.
def home_page(request):
    return render(request,'home.html')
def students_details(request):
    d=Student.objects.all()
    return render(request,'students_details.html',{"data":d})

def add_page(request):
    return render(request,"add_student.html")

def add_student(request):
    name=request.POST['name']
    gender=request.POST['gender']
    course=request.POST['course']
    city=request.POST['city']
    Student.objects.create(name=name,gender=gender,course=course,city=city)
    return redirect('student')

def update_page(request,id):
    d=Student.objects.get(id=id)
    return render(request,"update.html",{"data":d})

def update_student(request,id):
    Student.objects.filter(id=id).update(name=request.POST['name'],gender=request.POST['gender'],course=request.POST['course'],city=request.POST['city'])
    return redirect('student')
def delete_student(request,id):
    Student.objects.get(id=id).delete()
    return redirect('student')
# def get_excel(request):
#     d=pd.read_excel('student.xlsx')
#     for i,j in d.iterrows():
#         Student.objects.create(name=j['name'],gender=j['gender'],course=j['course'],city=j["city"])
#     return redirect('student')








