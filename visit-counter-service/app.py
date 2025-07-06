from flask import Flask, jsonify
import redis
import requests  


app = Flask(__name__)


redis_client = redis.StrictRedis(host='34.197.132.90', port=6379, db=0, decode_responses=True)

@app.route('/')
def home():
    
    visit_count = redis_client.incr('visit_count')
    return jsonify({'message': 'Bienvenido a la página de inicio', 'visit_count': visit_count})


@app.route('/count-external-visits')
def count_external_visits():
    
    external_page_url = 'http://44.206.184.200/'
    
    try:
        
        response = requests.get(external_page_url)
        
        if response.status_code == 200:
            
            external_visit_count = redis_client.incr('external_page_visit_count')
            return jsonify({'message': 'Visita a la página externa registrada', 'visit_count': external_visit_count})
        else:
            return jsonify({'message': 'Error al acceder a la página externa'}), 500
    except Exception as e:
        return jsonify({'message': f'Error al hacer la solicitud: {str(e)}'}), 500

@app.route('/reset')
def reset_visits():
    redis_client.set('visit_count', 0)
    redis_client.set('external_page_visit_count', 0)
    return jsonify({'message': 'Contadores de visitas reiniciados', 'visit_count': 0, 'external_page_visit_count': 0})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
