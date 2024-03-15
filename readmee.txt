always run in env
(env) PS E:\Manish\MindRisers\project\ToDo> python manage.py startapp base
#write codes
Settings.py ma Installed_apps ma 'base' add garne


model.py terminal
(env) PS E:\Manish\MindRisers\project\ToDo> python manage.py makemigrations

(env) PS E:\Manish\MindRisers\project\ToDo> python manage.py migrate

coding in admin.py

coding in urls.py
(env) PS E:\Manish\MindRisers\project\ToDo> python manage.py createsuperuser    (admin,email,password)    

coding in views.py

import home in url.py and add path('home/',home)

edit templates in Settings.py = 'DIRS': [BASE_DIR/ 'templates'], 


adding bootstrap of table in index.html

code inside def home(request): in views.py by importing ToDo

code inside tbody in index.html