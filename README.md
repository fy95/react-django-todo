# ToDoList

### 任务要求

使用 Django, Django Rest Framework, Bootstrap, PostgreSQL (optional), React+React Router+ Redux + Redux API (optional), jQuery (optional) 等技术做一个待办事项的网站。

一个参考的例子：[todoist.com](http://todoist.com/)

实现的功能：

* 创建一个待办事项（待办事项可以设置优先级、expire-date）
* 删除一个待办事项
* 标记一个待办事项为已完成
* 编辑一个待办事项的具体内容
* 列出所有的未完成的待办事项
* 支持按照不同的方式排序

### 界面展示
  
1. **TaskList**

 ![](https://github.com/fy95/react-django-todo/blob/master/screenshot.jpg)

2. **TaskDetail**

![](https://github.com/fy95/react-django-todo/blob/master/04list.gif)

### 功能展示

1. **创建待办事项**

事项有 `title,content,expire_date,priority` 这几个属性

![](https://github.com/fy95/react-django-todo/blob/master/01edit.gif)


2. **删除待办事项**

![](https://github.com/fy95/react-django-todo/blob/master/02dele.gif)


3. **标记事项已完成**

![](https://github.com/fy95/react-django-todo/blob/master/03finish.gif)


4. **编辑（修改）一个待办事项的具体内容**

这里修改的表单中如果不填入内容，就默认不改变

![](https://github.com/fy95/react-django-todo/blob/master/01edit.gif)


5. **列出所有的未完成的待办事项**

![](https://github.com/fy95/react-django-todo/blob/master/04list.gif)


6. **支持按照不同的方式排序**

目前设计的有 **按创建时间排序（默认）, 按过期时间排序 , 按优先级排序**

![](https://github.com/fy95/react-django-todo/blob/master/04list.gif)


### 改进方向

1. 列表界面支持翻页
2. 把Sqlite换成PostgreSQL
2. 使用React,Redux构建界面,美化界面
