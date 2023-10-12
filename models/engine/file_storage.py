import json
class FileStorage:
    __file_path = "file.json"
    __object = {}

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        key = "{}.{}.format(obj.__class__.__name__, obj.id)"
        FileStorage.__objects[key] = obj
    def save(self):
        serial_obj = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w')  as f:
            json.dump(serial_obj, f)
    def reload(self):
        
