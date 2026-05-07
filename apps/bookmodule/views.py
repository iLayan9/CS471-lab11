from django.shortcuts import render


from django.http import HttpResponse
#from httpx import request

#Task1:
#def index(request):
#    return HttpResponse("Hello world")

#Task2:
#def index(request):
#    name = request.GET.get("name") or "world"
#    return HttpResponse("Hello " + name)


#Task3:
#def index2(request, val1=0):
#    return HttpResponse("value1 = " + str(val1))

#task4:
#def task4(request):
#    return render(request, "bookmodule/index.html")



#def index2(request, val1=0):
#    return HttpResponse("value1 = " + str(val1))

#task5
#def index(request):
#    name = request.GET.get("name") or "world"
#    return render(request, "bookmodule/index.html", {"name": name})

#def index2(request, val1=0):
#    return HttpResponse("value1 = " + str(val1))

#task7
#def viewbook(request, bookId):
#    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
#    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

#    targetBook = None
#    if book1['id'] == bookId:
#        targetBook = book1
#    if book2['id'] == bookId:
#        targetBook = book2

#    context = {'book': targetBook}  # book is the variable name accessible by the template
#    return render(request, 'bookmodule/show.html', context)

#task4-lab4
#def index(request):
#    return render(request, "bookmodule/index.html")
#def list_books(request):
#    return render(request, 'bookmodule/list_books.html')
#def viewbook(request, bookId):
#    return render(request, 'bookmodule/one_book.html')
#def aboutus(request):
#    return render(request, 'bookmodule/aboutus.html')



#lab5

def links_view(request):
    return render(request, 'bookmodule/links.html')


def text_formatting_view(request):
    return render(request, 'bookmodule/text_formatting.html')


def listing_view(request):
    return render(request, 'bookmodule/listing.html')


def tables_view(request):
    return render(request, 'bookmodule/tables.html')



#lab6
def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def search_view(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')



#lab7

from .models import Book

def insert_books(request):
    Book.objects.create(title='Continuous Delivery', author='J.Humble and D. Farley', price=120.00, edition=3)
    Book.objects.create(title='Reversing: Secrets of Reverse Engineer', author='E. Eilam', price=97.00, edition=2)
    Book.objects.create(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.00, edition=4)
    return render(request, 'bookmodule/bookList.html', {'books': Book.objects.all()})

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    


#lab8

from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book
from .models import Book, Student, Address

def lab8_task1(request):
    mybooks = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task2(request):
    mybooks = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task3(request):
    mybooks = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task5(request):
    data = Book.objects.aggregate(
        count=Count('id'),
        total=Sum('price'),
        average=Avg('price'),
        maximum=Max('price'),
        minimum=Min('price')
    )
    return render(request, 'bookmodule/task5.html', data)

def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student')).values('city', 'student_count')
    return render(request, 'bookmodule/task7.html', {'cities': cities})


#lab9

from django.db.models import Q, Count, Sum, Avg, Max, Min, F, ExpressionWrapper, FloatField
from .models import Book, Publisher, Author, Address, Student

def lab9_task1(request):
    total = Book.objects.count()
    books = Book.objects.all()
    for book in books:
        book.percentage = round((book.quantity / total) * 100, 2)
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})


def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})


def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})


def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})

def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4))
    ).values('name', 'high_rated_count')
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})

def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        book_count=Count('book', filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1))
    ).values('name', 'book_count')
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})


#lab10
from django.shortcuts import render, redirect
from .forms import BookForm

def lab10_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_listbooks.html', {'books': books})

def lab10_addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        rating = request.POST.get('rating')
        Book.objects.create(
            title=title,
            price=price,
            quantity=quantity,
            rating=rating,
            pubdate='2024-01-01 00:00:00'
        )
        return redirect('/books/lab9_part1/listbooks')
    return render(request, 'bookmodule/lab10_addbook.html')

def lab10_editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.rating = request.POST.get('rating')
        book.save()
        return redirect('/books/lab9_part1/listbooks')
    return render(request, 'bookmodule/lab10_editbook.html', {'book': book})

def lab10_deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books/lab9_part1/listbooks')


def lab10_p2_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_p2_listbooks.html', {'books': books})

def lab10_p2_addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10_p2_addbook.html', {'form': form})

def lab10_p2_editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10_p2_editbook.html', {'form': form})

def lab10_p2_deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books/lab9_part2/listbooks')

#lab11

from .models import Book, Publisher, Author, Address, Student

def lab11_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/lab11_students.html', {'students': students})

def lab11_addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/lab11/students')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/lab11_addstudent.html', {'form': form})

def lab11_editstudent(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/books/lab11/students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/lab11_editstudent.html', {'form': form})

def lab11_deletestudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/books/lab11/students')

from .models import Book, Publisher, Author, Address, Student, Address2, Student2, Product
from .forms import BookForm, StudentForm, Student2Form

def lab11_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/lab11_students2.html', {'students': students})

def lab11_addstudent2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/lab11/students2')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/lab11_addstudent2.html', {'form': form})

def lab11_editstudent2(request, id):
    student = Student2.objects.get(id=id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/books/lab11/students2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/lab11_editstudent2.html', {'form': form})

def lab11_deletestudent2(request, id):
    student = Student2.objects.get(id=id)
    student.delete()
    return redirect('/books/lab11/students2')


from .forms import BookForm, StudentForm, Student2Form, ProductForm

def lab11_products(request):
    products = Product.objects.all()
    return render(request, 'bookmodule/lab11_products.html', {'products': products})

def lab11_addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/books/lab11/products')
    else:
        form = ProductForm()
    return render(request, 'bookmodule/lab11_addproduct.html', {'form': form})

def lab11_editproduct(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/books/lab11/products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'bookmodule/lab11_editproduct.html', {'form': form, 'product': product})

def lab11_deleteproduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/books/lab11/products')