from pymongo import MongoClient
con=MongoClient('mongodb+srv://goutham:goutham1@cluster0-hzp6j.mongodb.net/test?retryWrites=true&w=majority')
db=con['bikesecurity']
db['safe'].update_one({"name":"gouthambabu1@gmail.com"},{"$set":{"secure":0}})
