from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection


if __name__ == '__main__':
    api = OandaApi()

    # data = api.get_instruments()
    # [print(x['name']) for x in data]

    # instrumentCollection.loadInstruments("./data")
    # instrumentCollection.printInstruments()


    instrumentCollection.createFile(api.get_account_instruments(), "./data")
    instrumentCollection.printInstruments()