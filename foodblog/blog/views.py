from django.shortcuts import render, redirect
from .models import Category, Food
# Create your views here.
def home(request):
    category = request.GET.get('category')
    if category == None:
        foods = Food.objects.all()
    else:
        foods = Food.objects.filter(category__name__contains=category)

    categories = Category.objects.all()
    # foods = Food.objects.all()
    data = {
        'categories':categories,
        'foods':foods,
    }
    return render(request, 'blog/home.html', data)

def viewFood(request,pk):
    food = Food.objects.get(id=pk)

    return render(request, 'blog/food.html', {'food':food})

def addFood(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        food = Food.objects.create(
            category=category,
            description=data['description'],
            image=image,
            short_description=data['short_description'],
            title=data['title'],
            ingredients=data['ingredients'],
        )
        return redirect('home')
    context = {
        'categories':categories,
    }
    return render(request, 'blog/add.html',context)


