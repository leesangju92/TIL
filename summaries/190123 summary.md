# 190123 summary

## Ⅰ. SQL

```sql
CREATE TABLE awards (
	id INTEGER PRIMARY KEY,
	recipient TEXT NOT NULL,
	award_name TEXT DEFAULT 'Grammy'
);
```

```sql
SELECT * FROM movies WHERE year BETWEEN 1970 AND 1979;
```

```sql
SELECT *
FROM movies
WHERE year < 1985 AND genre="horror";
```

```sql
SELECT *
FROM movies
WHERE genre = "comedy"
   OR genre = 'romance';
```

```sql
SELECT name,
CASE
WHEN genre="romance" THEN "Chill"
WHEN genre="comedy" THEN "Chill"
ELSE "Intense"
END AS "Mood"
FROM movies;
```

```sql
SELECT DISTINCT year
FROM movies;
```

```sql
SELECT imdb_rating AS 'IMDb'
FROM movies;
```

```sql
SELECT category, price, AVG(downloads)
FROM fake_apps
GROUP BY 1,2;
```

```sql
SELECT price, ROUND(AVG(downloads)), COUNT(*)
FROM fake_apps
GROUP BY price
HAVING COUNT(*) > 10;
```

```sql
SELECT ROUND(AVG(price),2)
FROM fake_apps;
```

```sql
SELECT orders.order_id,
   customers.customer_name
FROM orders
JOIN customers
  ON orders.customer_id = customers.customer_id; 
```

```sql
SELECT *
FROM newspaper
LEFT JOIN online
ON newspaper.id = online.id
WHERE online.id IS NULL;
```

```sql
SELECT month, COUNT(*)
FROM newspaper
CROSS JOIN months
WHERE start_month <= month and end_month >= month
GROUP BY month;
```

```sql
SELECT * FROM newspaper UNION SELECT * FROM online;
```

```sql
WITH previous_query AS (
SELECT customer_id,
   COUNT(subscription_id) AS 'subscriptions'
FROM orders
GROUP BY customer_id
)
SELECT customers.customer_name, previous_query.subscriptions
FROM previous_query
JOIN customers
ON previous_query.customer_id = customers.customer_id;

```

## Ⅱ. ERD

> Database를 어떻게 구성할지 고민하는 것이며 1:1, 1:n, n:n 관계가 있다.
>
> http://aquerytool.com/에서 그리기 가능하다.



## Ⅲ. Django

### 1. Web Framework

> Dynamic web (static web과 반대되는 개념)
>
> Framework : 기본적인 구조나 필요한 코드를 제공하는 서비스 (Ex: React JS, Python django, Java spring, PHP Laravel, ASP.NET, Angular JS, Ruby on Rails)
> 다른 언어는 MVC (Model View Controller) 파이썬은 MTV (Model Template View), Database는 따로 존재한다. View가 필수이자 핵심이다. 

`사용자 → View(뭘 할지 판단) → Model → Database → Model → view → template → 사용자`

### 2. Django 설치

#### Terminal

> `$ pip install djangjo`
>
> `$ django-admin help ` 		
>
> `$ django-admin startproject first_django`
>
> `$ python manage.py runserver`
>
> `$ python manage.py runserver $IP:$PORT`
>
> `$ django-admin startapp home`

#### views.py

>```python
>from django.shortcuts import render, HttpResponse
>import random
>
>def index(request):
>    return render(request, "index.html")
>
>def lotto(request):
>    lucky_numbers = random.sample(range(1, 46), 6)
>    print("----------",lucky_numbers,"---------")  #터미널에서 인쇄된다.
>    return HttpResponse(lucky_numbers)
>
>def hello(request, name):
>    return HttpResponse("hello" + name)
>
>```

#### urls.py

> ```python
> from home import views
> 
> urlpatterns = [
>     path('admin/', admin.site.urls),
>     path("", views.index),
>     path("lotto/", views.lotto),
>     path( "hello/<name>/    ", views.hello),
> ]
> ```

#### settings.py

> ```python
> TEMPLATES_DIR = os.path.join(BASE_DIR, "templates") #추가해야한다
> 
> ALLOWED_HOSTS = [
>  "django-leesangju92.c9users.io",
> ]
> 
> #ALLOWED_HOSTS = ["*"]	
> 
> 
> INSTALLED_APPS = [
>  'django.contrib.admin',
>  'django.contrib.auth',
>  'django.contrib.contenttypes',
>  'django.contrib.sessions',
>  'django.contrib.messages',
>  'django.contrib.staticfiles',
>  'home', #이것을 추가한다.
> ]
> 
> TEMPLATES = [
>  {
>      'BACKEND': 'django.template.backends.django.DjangoTemplates',
>      'DIRS': [TEMPLATES_DIR], #이것을 추가한다.
>      'APP_DIRS': True,
>      'OPTIONS': {
>          'context_processors': [
>              'django.template.context_processors.debug',
>              'django.template.context_processors.request',
>              'django.contrib.auth.context_processors.auth',
>              'django.contrib.messages.context_processors.messages',
>          ],
>      },
>  },
> ]
> 
> LANGUAGE_CODE = 'ko-kr'
> 
> TIME_ZONE = 'Asia/Seoul'
> 
> USE_I18N = True
> 
> USE_L10N = True
> 
> USE_TZ = True
> 
> ```

#### 주의사항

> `$ export 환경변수="value"`
>
> `$ $환경변수`:환경변수 안의 `value`값을 return
>
> django 리스트 안에 변수 쓸 때 `,`꼭 써놓기 
>
> 항상 주소 뒤에 / 붙이기 

## Ⅳ. 기타

### 1. C9 단축기

| 단축키  | 설명                    |
| ------- | ----------------------- |
| `alt+w` | 탭 닫기                 |
| `alt+s` | 탭 이동(메인과 터미널 ) |

