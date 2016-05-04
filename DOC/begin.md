# 目录说明

## django

安装了django之后，使用 *django-admin.py startproject projectname* 创建工程

### 原始工程目录

    ├── manage.py
    └── projectname
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

1. manage.py 是管理项目的脚本，有很多管理指令
2. projectname 下则是工程主目录（现在什么都没有，只有配置文件）
3. settings.py 配置文件（配置各种目录，各种环境，例如数据库等等）
4. urls.py 解析输入的url，并配置对应这个url的处理转发
5. wsgi.py 不用管

### 什么是django中的app？

**app就是相当于模块，比如说我要做一个主页模块或者博客模块，一般对应一个数据库表**

使用manage.py创建模块

*python manage.py startapp module*

    ├── manage.py
    ├── module
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── projectname
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

看到有新建一个module出来，重要的文件

1. models.py 定义对象的名称属性，基本类型，定义完成之后参考<django的指令－－生成指令>，可以生成对应的数据库，这就是django的orm映射，所有数据库的改动都由models决定，并不用去动数据库。
2. views.py 我的理解类似于controller，获取models的对象，然后进行展现（获取html）

### 目前的目录工程

括号中为添加的目录，非django创建的目录, <> 意思是我加的目录

    ├── manage.py
    ├── static <用于放各种静态文件>
    │   ├── css
    │   │   ├── bootstrap-theme.css
    │   │   ├── bootstrap-theme.css.map
    │   │   ├── bootstrap-theme.min.css
    │   │   ├── bootstrap.css
    │   │   ├── bootstrap.css.map
    │   │   ├── bootstrap.min.css
    │   │   └── customCss <放自定义的css，其他css文件目录下的都是bootstrap的东西>
    │   │       └── index.css
    │   ├── database（放数据库）
    │   │   └── teamWeb.sql
    │   ├── fonts（bootstrap的字体目录）
    │   ├── image <放图片的>
    │   ├── js
    │   │   ├── bootstrap.js
    │   │   ├── bootstrap.min.js
    │   │   ├── customJs
    │   │   │   └── index.js
    │   │   ├── jQuery.js (这个要另外下载放进去的)
    │   │   └── npm.js
    │   └── templates<html模版我放到这里来了>
    │       └── index.html
    ├── teamSite
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    ├── teaminfo (想做详细界面的app)
    └── teammate (index对应的app)


**注：任何生成的pyc文件都是python的执行文件，随便删除都可以，也不用在意，因为我已经设置了.gitignore 所以提交的时候也不用管，默认不会提交**
    

# django工作流

    
    1.用户请求URL(http://127.0.0.1:8000/index)
    
    2.由urls.py解析(正则表达式)
        urlpatterns = [
            url(r'^admin/', include(admin.site.urls)),
            url(r'^index/$', 'teammate.views.index'),
        ]
    分发到teammate这个app的views的index方法
    
    3. teammate里面的index响应 然后拿TeamMate的所有Obj,展示到index.html里面。
        def index(request):
            members = TeamMate.objects.all()
            return render_to_response('index.html',{'members':members})
        3.1 TeamMate：看import就知道，是models里面的 TeamMate类
        3.2 index.html 我在settings里面配置了TEMPLATES，会去static/templates目录下找同名文件。
        
    4.index.html
         使用 link和script 引入我们写好的css和js（当然还有bootstrap的js和css，这里也可以设置成读远程的cdn）
         <!-- 外部Css -->
          <link rel="stylesheet" href="/static/css/bootstrap.css"/>
          <link rel="stylesheet" href="/static/css/customCss/index.css" type="text/css" />

          <!-- 外部JS -->
          <script src="/static/js/jQuery.js"></script>  
          <script src="/static/js/bootstrap.min.js"></script>
          <script src="/static/js/customJs/index.js"></script>

# django的指令

    －－创建指令
    1.django-admin.py startproject projectname  创建工程
    2.python manage.py startapp module          创建app
    
    －－生成指令
    1.python manage.py validate 第一步验证(1.96好像没有了)

    2.python manage.py makemigrations (在已有的models中更新了东西用这个)

    3.python manage.py migrate（新建的models用这个）
    
    －－跑工程
    1.python manage.py runserver
    
    
# BootStrap是什么

bootstrap就是一个前端框架，就是把html和js还有css封装好成了模块给你直接用。

### 哪些是bootstrap？

index.html为例子：

      <div class = "row">
        <div class="col-md-12">
          <div class="jumbotron">
            <div class="row">
              <div class="col-md-8" id="maininfo">
                <h1>(〃＞皿＜)工作室</h1>
                <p>强悍的实力、无比的创意，Join us right now！</p>
                <p><a class="btn btn-primary btn-lg" role="button">点击更多了解</a></p>
              </div>

              <div class="col-md-4" id="logo">
                <img src="/static/image/stone.jpg" 
                class="img-thumbnail">
              </div>
            </div>

          </div>
        </div>
      </div>
    
1. 行的class是row 列是 col－xx-nn(xx代表尺寸，nn代表列数)，一般被分成12列，设计的时候让一行里面所有的nn加起来等于12就可以了。
2. xx不细说，这里就用md，代表一般电脑上看到的效果，以后适配移动端的时候再加别的。
3. img-thumbnail 这种就是圆形的图片。

可以看出bootstrap就是封装了一些控件，想要什么控件的时候就百度找一下，记得我们是用bootstrap3.3.5的版本。

# JS怎么写？

js就是写事件和特效，index.js为例：

    $("#four_flash .but_right img").click(function(){
        _index5++;
        var len=$(".flashBg ul.mobile li").length;
        // 每行摆3个,大于len了就要重新循环,所以要加上
        if(_index5+3>len){
            $("#four_flash .flashBg ul.mobile").stop().append($("ul.mobile").html());
        }
        //270为一个li的宽度
        $("#four_flash .flashBg ul.mobile").stop().animate({left:-_index5*270},1000);
    });
    
1. 这里的js一般都用jquery，jquery是什么？就是封装了js的一个框架，类比于android和afinal。
2. \#four_flash .but_right img （id 为# class 为. ） 通过这种形式来准备找到html中的每一个标签。

        <div id="four_flash"> （id为four_flash）
          <div class="flashBg"> （class为but_right）
            <ul class="mobile">
              <li>
                <img src="/static/image/{{member.image}}" /> （img标签）
3. click里面就是具体的事件了，和java语法比较像

# CSS 怎么写？

index.css为例：

    #four_flash .flashBg ul.mobile li{
        border:10px solid #2E324B;
        float:left;
        width:260px;
        height:280px;
        margin-left:5px;
        margin-right: 5px;
        padding-top:40px;
        color:#6C6E85;
    }
    
1. 和js一样的方法去找到那个标签（或者是一类标签）
2. ／#four_flash .flashBg ul.mobile li : id为four_flash，class为flashBg 的\<ul\>标签中的 id为mobile的\<li\>标签。
3. 属性不说

# 怎么开发与调试？

## 工程运行与查看
1. <django的指令－－跑工程>
2. 直接在浏览器看 http://127.0.0.1:8000/index/

## IDE与调试
1. 我是用sublime 3写的
2. 用chrome的开发者模式，进行细调（快捷键是ALT+花+I）
    
    
        