from flask import Flask
from flask import request
from flask import jsonify
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'
    
users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'bjk123', 
         'name': 'Susie',
         'job': 'Doctor',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST'])
def get_users():
 #  print(">> request: " , request)
 #  print(">> request.args: " , request.args)
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      elif search_username  :
         return find_users_by_name(search_username)  
      elif search_job  :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
    #    print(">> request JSON", request.get_json())
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
  
      
# def get_users():
#    search_username = request.args.get('name') #accessing the value of parameter 'name'
#    if search_username :
#       subdict = {'users_list' : []}
#       for user in users['users_list']:
#          if user['name'] == search_username:
#             subdict['users_list'].append(user)
#       return subdict
#    return users
   
@app.route('/users/<id>', methods=['GET', 'DELETE'])

def get_user(id):
   if id :
      for user in users['users_list']:
         if user['id'] == id:
            if request.method == 'GET':
               return user
            elif request.method == 'DELETE':
               users['users_list'].remove(user)
               resp = jsonify({}), 204
               return resp
      resp = jsonify({"error": "User not found"}), 404
      return resp
   return users
   
def find_users_by_name(name):
   subdict = {'users_list' : []}
   for user in users['users_list']:
      if user['name'] == name:
         subdict['users_list'].append(user)
   return subdict   

