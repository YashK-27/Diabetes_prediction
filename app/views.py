from app import app
from app import render_template,url_for,request,jsonify


@app.route('/')
def test_page():
    return render_template('index.html')

@app.route('/start_test/')
def start_test():
    return render_template('start_test.html')

@app.route('/api',methods = ['POST', 'GET'])
def tt():
    data = request.get_json()
    print(data['data'][0])
    
    
    # Do something with the data...
    response = {'status': 'success'}
    return jsonify(response)