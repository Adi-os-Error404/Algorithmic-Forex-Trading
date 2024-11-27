import json
from models.instrument import Instrument


class InstrumentCollection:
    FILENAME = "instruments.json"
    API_KEYS = ['name', 'type', 'displayName', 'pipLocation', 'displayPrecision', 'tradeUnitsPrecision', 'marginRate']

    def __init__(self) -> None:
        self.instruments_dict = {}

    def loadInstruments(self, path):
        self.instruments_dict = {}
        fileName = f"{path}/{self.FILENAME}"
        with open(fileName, 'r') as f:
            data = json.loads(f.read())
            for k, v in data.items():
                self.instruments_dict[k] = Instrument.fromApiObject(v)

    def createFile(self, data, path):
        if data is None:
            print("Instrument file creation failed")
            return
        
        self.instruments_dict = {}
        for i in data:
            key = i['name']
            self.instruments_dict[key] = { k: i[k] for k in self.API_KEYS }

        fileName = f"{path}/{self.FILENAME}"
        with open(fileName, "w") as f:
            f.write(json.dumps(self.instruments_dict, indent=3))

    def printInstruments(self):
        [print(k,v) for k,v in self.instruments_dict.items()]
        print("Total instruments:", len(self.instruments_dict.keys()))


# By defualt, in python, Singleton pattern is implemented
instrumentCollection = InstrumentCollection()