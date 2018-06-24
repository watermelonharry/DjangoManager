It'll be a deploy platform(or an DevOp platform) using:
1. Django as web server (controller) to manage the tasks
2. Ansible(or fabric) as local/remote executer (agent)
3. ZeroRPC(or Celery / rest api) to distribute tasks
4. Bootstrap and Vue to reduce the costs in front-end developing
-----------------------------

#required package:
1. django 1.11.X
2. django-rest-framework-2.X.X
3. other modules

#INSTALL GUIDE:
1. git clone xxxx
2. cd to project dir, using "pip install -r requirements.txt" to install required package
3. using "python manage.py syncdb" to create your own database.
4. run test server or deploy the server in apache/nginx. Dokcer env is recommended

-----------------------------
#dev roadmap:
1. command management: keep sh command in database
2. agent register: agent will register to server
3. advanced user management.
4. agent remote control: push commands from server and execute them remotely.
5. agent status monitoring and graphic demonstration: monitor the agent status.
....and so on

-----------------------------
#structure:  
--commader: sh command manager. Offers single command / command set storage.  
--basepkg: public modules  
--feedback: feedback module, prototype.  
--DjangoManager: base folder, contains the django config files, and "welcome page".  
--static: static files, such as *.js *.ico *.css  
--terminalReg: manage the terminal's registration.  
--userManage: manage the users' profiles, providing user signup/verification services.  
-manage.py: django's powerful tool.  
-requirement.txt: required packages.  


-----------------------------
#todo:
1. command management: keep sh command in database
2. agent register: agent will register to server
3. advanced user management.
4. agent remote control: push commands from server and execute them remotely.
5. agent status monitoring and graphic demonstration: monitor the agent status.
....and so on

-----------------------------
#snapshots：
##main page(inherit from former project):
![main page](https://github.com/watermelonharry/django-ipmanage/blob/master/introduction/main_page.png)