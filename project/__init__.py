#
import os,sys
from flask import Flask,jsonify

# 初始化app
app = Flask(__name__)


# 环境配置
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)

@app.route('/ping', methods = ['GET'])
def ping_pong():
	return jsonify({
		'status':'success',
		'message':'pong!'
	})

print(app.config,file=sys.stderr)
