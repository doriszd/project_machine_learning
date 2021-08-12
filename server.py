# Adapted from lecture  - https://github.com/ianmcloughlin/random-app/blob/master/rando.py
# https://towardsdatascience.com/deploying-keras-models-using-tensorflow-serving-and-flask-508ba00f1037
# https://github.com/Freeha-S/Machine-Learning-Project2020/blob/main/web-service.py

# windows machine:
# set FLASK_APP=server.py
# python -m flask run
# when server is running access on web browser at - http://127.0.0.1:5000/

# import flask for web app.
from flask import Flask


# tensorflow documentation on saving and loading keras model - https://www.tensorflow.org/guide/keras/save_and_serialize
from tensorflow import keras
model = keras.models.load_model("model.h5")

# Create a new web app.
app = Flask(__name__, static_url_path='', static_folder='static')

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index_new.html')


# from stack overflow - https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
# added a second app route to handle floating point numbers using same function to call model.predict 
@app.route('/predict/<int:x>', methods=['GET'])
@app.route('/predict/<float:x>', methods=['GET'])
def predict(x):
  prediction = model.predict([x])
  #return {"predicted power output": str(prediction[0][0])}
  return str(prediction[0][0])

