from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)


class KitapAdi(Resource):
    def get(self):
        data = pd.read_csv('yabanciklasikler.csv')
        data = data.to_dict('records')
        return {'data': data}, 200

    def post(self):
        KitapAdi = request.args['KitapAdi']
        KitapYazari = request.args['KitapYazari']
        SayfaSayisi = request.args['SayfaSayisi']

        data = pd.read_csv('yabanciklasikler.csv')

        new_data = pd.DataFrame({
            'Kitapadi': [KitapAdi],
            'KitapYazari': [KitapYazari],
            'SayfaSayisi': [SayfaSayisi]
        })

        data = data.append(new_data, ignore_index=True)
        data.to_csv('yabanciklasikler.csv', index=False)
        return {'data': new_data.to_dict('records')}, 200



class KitapYazari(Resource):
    def get(self, KitapYazari):
        data = pd.read_csv('yabanciklasikler.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['KitapYazari'] == KitapYazari:
                return {'data': entry}, 200
        return {'message': 'No entry found with this name !'}, 404



api.add_resource(KitapAdi, '/kitapadi')
api.add_resource(KitapYazari, '/<string:KitapYazari>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    app.run()