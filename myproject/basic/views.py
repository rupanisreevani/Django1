from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from .models import StudentNew
from .models import post 
from.models import Users
from django.contrib.auth.hashers import make_password,check_password
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


# Create your views here.
def sample(request):
    return HttpResponse('hello world')


def sample1(request):
    return HttpResponse('welcome to django')

def sampleInfo(request):
    #data={"name":'sai',"age":22}
    data={"result":[1,3,6]}
    return JsonResponse(data)

def dynamicResponse(request):
    name=request.GET.get("name","sreevani")
    city=request.GET.get("city","hyd")

    #return HttpResponse(f"hello{name}")
    return HttpResponse(f"hello{name} from {city}")
# to test database connection
def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})
@csrf_exempt
def addstudent(request):
    print(request.method)
    if request.method == "POST":
        data = json.loads(request.body)
        student = StudentNew.objects.create(
            name=data.get('name'),
            age=data.get('age'),
            email=data.get('email')  
        )
        return JsonResponse({"status": "success", "id": student.id}, status=200)
    elif request.method=="GET":
        # results=list(StudentNew.objects.all().values())
        # print(results)
        # return JsonResponse({"status":"ok","data":results},status=200)
        # get a specific record by id
        # data = json.loads(request.body) 
    
        # ref_id = data.get("id")
        # results = list(StudentNew.objects.filter(id=ref_id).values())
        # return JsonResponse({"status": "ok", "data": results}, status=200)

        # filter by age>=20
    
        # data = json.loads(request.body)
        # ref_age = data.get("age")  
        # results = list(StudentNew.objects.filter(age__gte=ref_age).values())
        # return JsonResponse({"status": "ok", "data": results}, status=200)
        #filter by age<=20
        # data = json.loads(request.body)
        # ref_age = data.get("age")  
        # results = list(StudentNew.objects.filter(age__lte=ref_age).values())
        # return JsonResponse({"status": "ok", "data": results}, status=200)
        #order by name
        # results=list(StudentNew.objects.order_by('name').values())
        # return JsonResponse({"status":"ok","data":results},status=200)
    
        #get unique ages:
        # results=list(StudentNew.objects.values('age').distinct())
        # return JsonResponse({'status':'ok','data':results},status=200)
    
        # count total students:
        # results=StudentNew.objects.count()
        # return JsonResponse({'status':'ok',"data":results},status=200)




    

        results=list(StudentNew.objects.values())
        print(results)
        return JsonResponse({"status":"success","id":results},status=200)
    

    elif request.method=="PUT":
        
        data = json.loads(request.body)

        ref_id=data.get("id")#get id
        new_name=data.get("name")#fetting eamil wie request
        existin_stu=StudentNew.objects.get(id=ref_id)
        #print(existin_stu)
        
        existin_stu.name=new_name
        existin_stu.save()
        updated_data=StudentNew.objects.filter(id=ref_id).values().first()
        
        return JsonResponse({"status":"data updated successfully","updated_data":updated_data},status=200)
    
    elif request.method=="DELETE":
        data = json.loads(request.body)
        ref_id=data.get("id")#get id
        get_deleted_data=StudentNew.objects.filter(id=ref_id).values().first()
        to_be_delete=StudentNew.objects.filter(id=ref_id).delete()
        #to_be_delete.delete()
        return JsonResponse({"status":"success","messge":"student details successfully","deleted_data":get_deleted_data},status=200)
    
    return JsonResponse({"error": "Use POST method"}, status=400)
    




def addPost(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_post = post.objects.create(   # use a different variable name
                post_name=data.get('post_name'),
                post_type=data.get('post_type'),
                post_date=data.get('post_date'),
                post_description=data.get('post_description')
            )
            return JsonResponse({"status": "success", "id": new_post.id}, status=201)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"error": "Use POST method"}, status=405)


#get,post,put,delete



#get all records


@csrf_exempt
def get_all_students(request):
    students=StudentNew.objects.all()
    data=list(students.values())
    return JsonResponse(data,safe=False)


#get a specific record by id

def get_student_by_id(request, id):
    try:
        student = StudentNew.objects.get(id=id)  
        return JsonResponse({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "city": student.city
        })
    except StudentNew.DoesNotExist:  
        return JsonResponse({"error": "student not found"}, status=404)
    

# filter by age>=20

def filter_age_gte(request):
    students = StudentNew.objects.filter(age__gte=20)
    result = list(students.values())
    return JsonResponse(result, safe=False)


#filter by age>=20
def filter_age_gte(request):
    Students=StudentNew.objects.filter(age__gte=20)
    data=list(Students.values())
    return JsonResponse(data,safe=False)


# order ny name

def order_by_name(request):
    Students=StudentNew.objects.order_by('name')
    data=list(Students.values())
    return JsonResponse(data,safe=False)

#gte unique ages
def get_unique_ages(request):
    ages=StudentNew.objects.values_list('age',flat=True).distinct()
    return JsonResponse({"unique_ages":list(ages)})


#count total students
def count_students(request):
    total=StudentNew.objects.count()
    return JsonResponse({"total_students":total})



def job1(request):
    return JsonResponse({"message":"u have successfully applied for job1"},status=200)


def job2(request):
    return JsonResponse({"message":"u hava successfully applid for job1"},status=200)    



@csrf_exempt
def signUp(request):
    if request.method=='POST':
        data = json.loads(request.body)
        print(data)
        user=Users.objects.create(
            username=data.get('username'),
            email=data.get('email'),
            password=make_password(data.get('password'))
            )
    return JsonResponse({"status":"success"},status=200)


@csrf_exempt
def login(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        username=data.get('username')
        password=data.get('password')
        try:
            user=Users.objects.get(username=username)
            issuesd_time = datetime.now(ZoneInfo("Asia/Kolkata"))
            expired_time = issuesd_time + timedelta(minutes=25)
            if check_password(password,user.password):
                # token="a json web token"
                # creating jwt
                payload={"username":username,"email":user.email,"id":user.id,"exp":expired_time}
                token=jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")
                return JsonResponse({"ststus":'successfully loggedin','token':token,"issued_at":issuesd_time,"expired at":expired_time,"expired_in":int((expired_time - issuesd_time).total_seconds() / 60),
    },status=200)
            else:
                return JsonResponse({"status":'failure','message':'invalid password'},ststus=400)
        except Users .DoesNotExist:
            return JsonResponse({"status":'failure','message':'user not found'},ststus=400)


@csrf_exempt
def check(request):
    hashed="!80dRi6kiPX5oOOQ1dCn7ZxxhpyTaJf1Iftx1ceSh"
    ipdata = request.POST          # Gets POST form data
    print(ipdata)
    x=check_password(ipdata.get("ip"),hashed)
    print(x)

    # hashed = make_password(ipdata.get("ip"))   # Hashes input value
    # print(hashed)

    return JsonResponse({"status": "success", "data":x }, status=200)

@csrf_exempt
def hashed(request):
    if request.method == "GET":
        users = Users.objects.all() 
        for user in users:
            if not user.password.startswith('pbkdf2_sha256'):
                user.password = make_password(user.password)
                user.save()
        return JsonResponse({"status":"success","message":"All passwords updated"}, status=200)

@csrf_exempt
def getAllusers(request):
    if request.method == "GET":
        users_list = list(Users.objects.values())
        print(request.token_data,"token_data in view")
        print(request.token_data.get("username"),"username from token")
        print(Users,"Users list")
        for user in users_list:
            print(user["username"],"username from user list")
            if user["username"]==request.token_data.get("username"):
                return JsonResponse({"status": "success","loggedin_user":request.token_data,"data": users_list}, status=200)
        else:
                return JsonResponse({"error":"unauthorized access"},status=401)


    

 