import json
import models


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}.format(obj.__class__.__name__, obj.id)"
        FileStorage.__objects[key] = obj

    def save(self):
        serial_obj = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serial_obj, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                serial_obj = json.load(f)
            for key, value in serial_obj.items():
                class_name = value["__class__"]
                cls = getattr(models, class_name)
                self.__objects[key] = cls(**value)
        except:
            pass
