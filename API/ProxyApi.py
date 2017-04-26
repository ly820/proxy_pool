from flask import Flask,jsonify,request
from Manager.Proxymanger import Proxymanger

app = Flask(__name__)

api_list = {
    'get':'get an usable proxy',
    'refresh':'refresh proxy pool',
    'getall':'get all usable proxy',
    'delete?proxy=127.0.0.1:8080':'delete an unable proxy'
}

@app.route('/')
def index():
    return jsonify(api_list)

@app.route('/get/')
def get():
    proxy = Proxymanger().get()
    return proxy

@app.route('/refresh/')
def refresh():
    Proxymanger().refresh()
    return 'successful refresh proxy pool'

@app.route('/getall/')
def getall():
    proxies = Proxymanger().getAll()
    return jsonify(list(proxies))

@app.route('/delete/',methods=['GET'])
def delete():
    proxy = request.args.get('proxy')
    Proxymanger().delete(proxy)
    return 'success delete {}'.format(proxy)

def run():
    app.run(host='0.0.0.0',port=5000)

if __name__ == '__main__':
    run()