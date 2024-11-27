import requests
import constants.defs as defs

class OandaApi:

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {defs.API_KEY}",
            "Content_Type": "application/json"
        })

    def make_request(self, url, verb='get', code=200, params=None, data=None, headers=None):
        full_url = f"{defs.OANDA_URL}/{url}"
        try:
            res = None
            if verb == 'get':
                res = self.session.get(full_url, params=params, data=data, headers=headers)
            
            if res == None:
                return False, {'error': 'verb not found'}
            
            if res.status_code == code:
                return True, res.json()
            else:
                return False. res.json()
            
        except Exception as error:
            return False, {'Exception': error}

    def get_account_endpt(self, endpt, data_key):
        url = f"accounts/{defs.ACCOUNT_ID}/{endpt}"
        ok, data = self.make_request(url)
        if ok and data_key in data:
            return data[data_key]
        else:
            print("ERROR get_account_endpt()", data)
            return None

    def get_account_summary(self):
        return self.get_account_endpt("summary", "account")

    def get_account_instruments(self):
        return self.get_account_endpt("instruments", "instruments")