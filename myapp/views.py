from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home_page.html')

def about(request):
    scores =[{"names":"Jaden Vaughn","english":57,"maths":37,"chemistry":48,"biology":56},{"names":"Sigourney Brewer","english":31,"maths":21,"chemistry":82,"biology":83},{"names":"Kirestin Goff","english":45,"maths":31,"chemistry":58,"biology":75},{"names":"Britanni Ray","english":43,"maths":66,"chemistry":41,"biology":67},{"names":"Penelope Clarke","english":40,"maths":38,"chemistry":72,"biology":64},{"names":"Imelda Mejia","english":65,"maths":36,"chemistry":83,"biology":66},{"names":"Aidan Erickson","english":70,"maths":70,"chemistry":46,"biology":84},{"names":"Sebastian West","english":57,"maths":29,"chemistry":77,"biology":57},{"names":"Keelie Craig","english":55,"maths":62,"chemistry":69,"biology":79},{"names":"Kerry Brown","english":56,"maths":32,"chemistry":55,"biology":81}]
    data = {
        "scores":scores,

    }
    return render(request, 'about_page.html' ,data)

def product(request):
    age = 65
    weight = 70
    subjects = ["Math", "Science", "English"]
    isDisabled = True
    name = "Jane Johnson"

    data = {
       "age":age,
        "weight":weight,
        "subjects":subjects,
        "isDisabled":isDisabled,
        "name":name
    }
    return render(request, 'product_page.html' , data)

# .gitignore,requirements.txt,manage.py,db.sqlite3,template/,myapp/,myproject/
# pip freeze > requirements.txt
#git init
