from jinja2 import Template  # устарела escape jinja2
from markupsafe import escape

name = 'vodka'
age = 23

tm = Template('My name {{ n.upper() }} age {{ a*2 }} old')
msg = tm.render(n=name, a=age)
print(type(msg))  # <class 'str'>

print(msg)

print('-------- Dict ------------')

person = {'name': 'vodka', 'age': 45}
tm = Template('My name {{ p.name.upper() }} age {{ p.age*33 }} old')
msg = tm.render(p=person)
print(type(msg))  # <class 'str'>

print(msg)

print("-------- class -----------")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


per = Person('vodka', 22)

tm = Template('My name {{ p.name.upper() }} age {{ p.age*300 }} old')
msg = tm.render(p=per)
print(type(msg))  # <class 'str'>

print(msg)

tm = Template('My name {{ p.getName().upper() }} age {{ p.getAge()*4000 }} old')
msg = tm.render(p=per)
print(type(msg))  # <class 'str'>

print(msg)

print('-------- Экранирование {{ name }} --------')

data = '''Модуль Jinja вместо определения
{{ name }} Подставляет соответствующее значение
'''

tm = Template(data)
msg = tm.render(name='VDK45')

print(msg)

data = '''{% raw %}Модуль Jinja вместо определения
{{ name }} Подставляет соответствующее значение{% endraw %}
'''

tm = Template(data)
msg = tm.render(name='VDK45')

print(msg)

print('--------- Экранирование tag html------------')

link = '''
Not shield Html link:
<a href="#">Ссылка</a>
'''

tm = Template(link)
msg = tm.render()

print(msg)

link = '''
Shield Html link:
<a href="#">Ссылка</a>
'''

tm = Template('{{ lk | e }} ')
msg = tm.render(lk=link)

print(msg)

print('--------- escape --------')

link_2 = '''
Use escape for shield Html link:
<a href="#">Ссылка</a>
'''

tm = escape(link_2)
print(tm)

print('--------- Выражение for --------')

cities = [{'id': 1, 'city': 'Mosscow'},
          {'id': 2, 'city': 'Kiev'},
          {'id': 3, 'city': 'London'},
          {'id': 4, 'city': 'Dubai'},
          {'id': 5, 'city': 'Hanoi'}]

# -% Убирает перенос строки
link = '''<select name="cities">
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)

print('--------- Выражение if > 6 elif  else  --------')

cities = [{'id': 1, 'city': 'Mosscow'},
          {'id': 4, 'city': 'Kiev'},
          {'id': 7, 'city': 'London'},
          {'id': 10, 'city': 'Dubai'},
          {'id': 55, 'city': 'Hanoi'}]

# -% Убирает перенос строки
link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == 'Mosscow' -%}
    </option>{{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)

print('---------- sum ----------')

cars = [
    {'Model': 'Audi', 'price': 23000},
    {'Model': 'BMW', 'price': 17300},
    {'Model': 'Ford', 'price': 44300},
    {'Model': 'Honda', 'price': 21300}
]

tpl = "Сумарная цена всех авто: {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

digs = [1, 2, 3, 4, 5]
tpl = 'Сума всех чисел: {{ dig | sum }}'
tm = Template(tpl)
msg = tm.render(dig=digs)

print(msg)

print('---------- max ----------')

cars = [
    {'Model': 'Audi', 'price': 23000},
    {'Model': 'BMW', 'price': 17300},
    {'Model': 'Ford', 'price': 44300},
    {'Model': 'Honda', 'price': 21300}
]

tpl = "Максимальная цена всех авто: {{ cs | max(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

# Только модель
tpl = "Максимальная цена всех авто: {{ (cs | max(attribute='price')).Model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

# Только price
tpl = "Максимальная цена всех авто: {{ (cs | max(attribute='price')).price }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

print('---------- random ----------')

tpl = "Максимальная цена всех авто: {{ cs | random }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

print('---------- replace  ----------')

tpl = "Replace o на O: {{ cs | replace('o', 'O') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)
print(cars)

print('---------- filter  ----------')

persons = [
    {'name': 'Bob', 'old': 18, 'weight': 78.5},
    {'name': 'Tom', 'old': 28, 'weight': 82.3},
    {'name': 'Maria', 'old': 33, 'weight': 94.0}
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''

tm = Template(tpl)
msg = tm.render(users=persons)

print(msg)

print('---------- macro  ----------')

html = '''
{%- macro input(name, value='',  type='text', size=20) -%}
    < input type='{{ type }}' name='{{ name }}' value='{{ value | e }}' size='{{ size }}'>
{%- endmacro -%}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''

tm = Template(html)
msg = tm.render()

print(msg)

print('---------- call  ----------')

persons = [
    {'name': 'Bob', 'old': 18, 'weight': 78.5},
    {'name': 'Tom', 'old': 28, 'weight': 82.3},
    {'name': 'Maria', 'old': 33, 'weight': 94.0}
]

html = '''
{% macro list_users(list_of_users) %}
<ul>
{% for u in  list_of_users -%}
    <li>{{u.name}}
{%- endfor %}
<ul>
{%- endmacro -%}

{{ list_users(users) }}
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)

print(' ------- ')

html = '''
{%- macro list_users(list_of_users) -%}
<ul>
{% for u in  list_of_users -%}
    <li>{{u.name}}  {{caller(u)}}
{%- endfor %}
<ul>
{%- endmacro %}

{%- call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{%- endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)

print(' ------- Environment -------- ')  # Окружение

from jinja2 import Environment, FileSystemLoader


persons = [
    {'name': 'Александр', 'old': 18, 'weight': 78.5},
    {'name': 'Марина', 'old': 28, 'weight': 82.3},
    {'name': 'Андрей', 'old': 33, 'weight': 94.0}
]

file_loader = FileSystemLoader('templates')  # загрузчик
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons)

print(msg)

# PackageLoader - Загрузка шаблонов из пакета
# DictLoader - Загрузка шаблонов из словаря
# FunctionLoader - Загрузка на основе функции
# PrefixLoader - Загрузчик, использующий словаря для построения подкаталогов
# ChoiceLoader - Загрузчик, содержащий список других загрузчиков (если один не сработает, выбирает следующий)
# ModuleLoader - Загрузчик для скомпилированных шаблоных

print(' ------- FunctionLoader --------- ')
from jinja2 import Environment, FunctionLoader

def loadTpl(path):
    if path == 'index':
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные: {{u}}'''


file_loader = FunctionLoader(loadTpl)  # загрузчик
env = Environment(loader=file_loader)

tm = env.get_template('index')  # if index8 result = Данные: {'name': 'Александр', 'old': 18, 'weight': 78.5}
msg = tm.render(u=persons[0])

print(msg)

print('-------- include --------')

file_loader = FileSystemLoader('templates')  # загрузчик (FileSystemLoader) берет из под каталог templates
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(domain='hhtps://vdk45.ddns.net', title='Jinja2 include')

print(msg)

print('-------- import --------')

file_loader = FileSystemLoader('templates')  # загрузчик (FileSystemLoader) берет из под каталог templates
env = Environment(loader=file_loader)

tm = env.get_template('page_dialog.html')
msg = tm.render(domain='hhtps://vdk45.ddns.net', title='Jinja2 include')

print(msg)

print('------- Наследование --------')
print('----- from jinja2 import Environment, FileSystemLoader -----')

file_loader = FileSystemLoader('templates')  # загрузчик
env = Environment(loader=file_loader)

tm = env.get_template('about.html')

output = tm.render()
print(output)

print('------- Наследование {{ super() }} из базового шаблона layout/default.html--------')

file_loader = FileSystemLoader('templates')  # загрузчик
env = Environment(loader=file_loader)

tm = env.get_template('about_2.html')

output = tm.render()
print(output)

print('------- Наследование table_content --------')

subs = ['Математика ', 'Физика', 'Информатика ',  'Русский ']

file_loader = FileSystemLoader('templates')  # загрузчик
env = Environment(loader=file_loader)

tm = env.get_template('about_3.html')

output = tm.render(list_table=subs)
print(output)

print('------- Наследование block_item --------')

subs = ['Математика ', 'Физика', 'Информатика ',  'Русский ']

file_loader = FileSystemLoader('templates')  # загрузчик
env = Environment(loader=file_loader)

tm = env.get_template('about_4.html')

output = tm.render(list_table=subs)
print(output)















