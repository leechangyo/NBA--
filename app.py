from flask import Flask,jsonify,request,render_template
app = Flask(__name__)
from algorithm.nbaPredict import *

@app.route('/')
def home():
  return render_template('index.html')

#post /store data: {name :}
@app.route('/result' , methods=['POST'])
def create_store():
#   request_data = request.get_json()
#   new_store = {
#     'name':request_data['name'],
#     'items':[]
#   }
  # nbaPredict
  # store = nbaPredict.result
#   stores.append(new_store)
  return jsonify(store)
  #pass

# #get /store
@app.route('/result')
def get_stores():
  return jsonify({'stores': stores})


  #pass
if __name__ == "__main__":
    app.run(port=5000)



