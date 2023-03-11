from flask import Flask, request
import sys
project_name = "./Real_Time_Voice_Cloning"
sys.path.append(project_name)

import Real_Time_Voice_Cloning.model as model
import base64
import json
from connect import db,Tales

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lumineuxp:hgnuPHIJS9O7@ep-raspy-hall-234246.ap-southeast-1.aws.neon.tech/syn_voice_app"
db.init_app(app)

    
@app.route('/api-synthesize-tale', methods=['POST'])
def get_synthesize_tale():
    tale_id = request.json['tale_id'] #connect database
    embed64 = bytes(request.json['embed'], 'utf-8')
    
    tales = Tales.query.filter_by(id=tale_id).first()
    story = tales.story
    
    texts = story.split('/')
    
    syn_texts = []
    for text in texts: 
        syn = model.get_syn_voice(embed64,text) #base64
        # print(type(text))
        syn_tostr = syn.decode('utf8').replace("'", '"')
        jsonobj = {
            'text':text,
            'syn_voice': syn_tostr
        } 
        syn_texts.append(jsonobj)
        
    jsonstr = {
            'tale_id': tale_id,
            'syn_voice': syn_texts
        }  
    json_data = json.dumps(jsonstr)
    return json_data


if __name__ == "__main__":

    app.run(debug = True)

