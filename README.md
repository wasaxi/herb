# herb
中草药

## 请在doc/记录下自己的开发文档！！
## 若负责修改页面，请标明所改页面涉及的业务逻辑！
## 若负责后端逻辑，请标明所写函数的功能以及涉及的数据库！
## 写明 TODO：，记录下一步要干啥
## 请及时交流！

### 数据库文件db.sqlite3不要上传，git无法对比冲突

每次pull到本地后，运行:  
python manage.py makemigrations  
会进行初始化，根据模型生成迁移文件，然后再运行执行命令：  
python manage.py migrate  
根据迁移文件生成表，并将表都写入db.sqlite3文件中  


# 10.7 重建数据库
migrations2里面是以前的迁移文件
models2里面是以前的数据库对象

## 需要重写views.py
## 需要在数据库中插入一些数据做测试
## 前端页面删改
## 前后端连接




