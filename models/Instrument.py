

class Instrument:

    def __init__(self, name, inst_type, display_name, pip_location, trade_units_precision, margin_rate) -> None:
        self.name = name
        self.inst_type = inst_type
        self.display_name = display_name
        self.pip_location = pow(10, pip_location)
        self.trade_units_precision = trade_units_precision
        self.margin_rate = float(margin_rate)

    def __repr__(self) -> str:
        return str(vars(self))

    @classmethod
    def fromApiObject(cls, obj):
        # obj is JSON object
        return Instrument(
            obj['name'],
            obj['type'],
            obj['displayName'],
            obj['pipLocation'],
            obj['tradeUnitsPrecision'],
            obj['marginRate']
        )