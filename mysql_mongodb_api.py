import flask
from flask import Flask,request,jsonify,render_template
import mysql.connector as conn

import pymongo







app=Flask(__name__)



@app.route('/',methods=['POST'])
def Get_Data_From_Database():
    if request.method=='POST':
        
        db_service=request.json['db_service']
        if db_service.lower()=='mysql':
            user_sql=request.json['user_sql']
            password_sql=request.json['pass_sql']
            db_name=request.json['database']
            query_sql=request.json['query_sql']
            mydb = conn.connect(host = 'localhost',user = user_sql ,passwd = password_sql )
            cursor = mydb.cursor()
            cursor.execute(query_sql)
            data=cursor.fetchall()
            return jsonify(str(data)) 
        
        if db_service.lower()=='mongodb':
            client_mongo=request.json['client_mongo']
            db_name=request.json['database']
            coll_name=request.json['coll_name']
            client = pymongo.MongoClient(client_mongo)
            db=client[db_name]
            coll=db[coll_name]
            data=dict()
            counter=1
            for i in coll.find():
                data[counter]=i
                counter+=1
            print(data)
            return jsonify(str(data))



if __name__=="__main__":
    app.run()