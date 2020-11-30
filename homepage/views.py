from django.shortcuts import render, get_object_or_404
from .models import Profile, Skill
from datetime import date

# Create your views here.
# sWebTitle = "Uday Kiran Reddy"
# username = sWebTitle


def home(request):
    print("----testing----")
    profile = get_object_or_404(Profile)
    skills = Skill.objects.all()
    skills_1 = get_odds(skills, False)
    skills_2 = get_odds(skills, True)
    #testing = type(profile.dateofbirth)
    #print(testing)
    #print(calculateAge(profile.dateofbirth))
    return render(request, 'homepage/home.html', {'title': profile.webtitle, 'username': profile.name,'age':calculateAge(profile.dateofbirth), 'profile': profile, 'skills_1': skills_1, 'skills_2': skills_2})

def calculateAge(birthDate):
    birthDate = birthDate.date()
    #print(birthDate)
    today = date.today()
    age = today.year - birthDate.year - \
        ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age


def get_odds(local_list, even=True):
    odd_i = []
    even_i = []
    for i in range(0, len(local_list)):
      if (i % 2 == 0):
        even_i.append(local_list[i])
      else:
        odd_i.append(local_list[i])
    if even:
       return even_i
    else:
       return odd_i
