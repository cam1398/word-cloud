from flask import Flask, request,render_template
from flask_restful import Resource, Api
import base64
import wordcloud_code as wcp
app = Flask(__name__)
api = Api(app)
 
class GST_Query_Service(Resource):
   
    def post(self, query): 
      #d=request.data       
      istring= request.headers['myData']
      # UserQuery = base64.b64decode(d)
      BotResponse=AiBot.get_bot_response(istring)        
      return str(BotResponse)   

api.add_resource(GST_Query_Service, '/AiGSTBot/<string:query>')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5089, debug=True, threaded=True)