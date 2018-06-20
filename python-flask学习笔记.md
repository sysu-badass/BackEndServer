## python与flask的学习笔记

[toc]

### Flask

+ 首先若是在virtualenv中建立project，首先需要建立虚拟环境先，使用 virtualenv 命令在project文件夹中创建 Python 虚拟环境。这个命令只有一个必需的参数,即虚拟环境的名字。创建虚拟环境后,当前文件夹中会出现一个子文件夹,名字就是上述命令中指定的参数,与虚拟环境相关的文件都保存在这个子文件夹中。按照惯例,一般虚拟环境会被命名为venv,如**virtualenv venv**就可以创建虚拟环境了。 **(p26)**
+ Linux环境下可以通过**source venv/bin/activate**启动虚拟环境，并通过**deactivate**关闭虚拟环境。
+ 要运行Flask程序，需要以下命令，在Linux环境下，我们需要告诉系统Flask app是哪一个文件。先**export FLASK_APP = main.py**，再**flask run**。这里的main.py文件指的是我们的程序实例，里面有视图函数以及路由等信息。


### python
* 有关python的类的介绍 https://docs.python.org/3/tutorial/classes.html 主要有关其中的namespace and scope
* python 中immutable basic types 有numbers, strings, tuples，它们都是不可变的。
* 在python类中，\__str\__() and \__repr\__()的差别参考网址 https://stackoverflow.com/questions/1436703/difference-between-str-and-repr
