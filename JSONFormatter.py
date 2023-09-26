import json

class JSONFormatter:

    def convert(data):
        if type(data)==list:
            json_str = json.dumps([data_.to_dict() for data_ in data], indent=2)
        else:
            json_str=json.dumps(data.to_dict(),indent=2)
        return json_str
        
    