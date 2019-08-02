from flask import Flask
import requests
from bs4 import BeautifulSoup
from flask import jsonify, request, abort


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/check-voen', methods=['POST'])
def check_voen():
    if not request.json or not 'voen' in request.json:
        abort(400)
    url = 'https://www.e-taxes.gov.az/ebyn/edvPayerChecker.jsp'
    voen = request.json['voen']
    if voen:
        data = {'name': voen, 'submit': 'submit'}
        result = requests.post(url, data=data)
        plain_text = result.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        span = soup.find('span', attrs={'style': ' font-weight:bold'})
        if span:
            st = span.text
            st = st.split('"', 1)[1].split('"')[0]
            res = {'status': 1, 'name': st}
            return jsonify(res)
        else:
            span = soup.find('span', attrs={'style': 'background-color:#FF0000;color:#FFFFFF; font-weight:bold '})
            res = {'status': 0, 'message': span.text.strip()}
            return jsonify(res)
    else:
        return jsonify({'message': 'Voen duzgun deyil'})



if __name__ == '__main__':
    app.run()
