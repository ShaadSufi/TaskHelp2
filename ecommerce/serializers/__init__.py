from abc import ABC, abstractmethod
import json


class ExtDict(dict):
    def to_json(self):
        return json.dumps(self)


class ExtList(list):
    def to_json(self):
        return json.dumps(self)


class BaseSerializer(ABC):
    @abstractmethod
    def to_dict(self):
        pass

    @staticmethod
    def to_json(obj):
        return json.dumps(obj)

    @classmethod
    def from_db(cls, obj):
        return cls(obj)

    @classmethod
    def obj_list_to_dict_list(cls, obj_list: list) -> ExtList:
        dict_list = ExtList([cls(obj).to_dict() for obj in obj_list])
        return dict_list
