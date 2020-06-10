#coding=utf-8
 
from pymongo import MongoClient
 
conn = MongoClient('127.0.0.1', 27017)
 
# 连接 test 数据库bai，没有则自动创建
db = conn.test  
 
# 使用du results 集合，没有则自动创建
results = db.results
 
# 打开扫描信息文件, 并将数据存入到数据库
with open(r'C:\Users\dell\Desktop\result.txt', 'r') as f:
     for line in f.readlines():
    # 分割信息
     	items = line.strip('\r').strip('\n').split(',')    
    # 添加到数据库
     	students.insert({ 'stu_id': items[0], 'name': items[1], 'grade': int(items[2]) })
 
# 数据库查询信息并打印出来
for s in results.find():
    print(s)
