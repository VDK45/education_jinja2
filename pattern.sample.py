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


