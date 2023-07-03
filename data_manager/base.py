from abc import ABC, abstractmethod
from typing import Any, Generator


class BaseModel(ABC):
    _id: int

    def __repr__(self):
        return f"<{self.__class__.__name__} #{self._id}>"

    def __eq__(self, __value: object) -> bool:
        return (type(self) is type(__value) and
                self._id == __value._id)

    @classmethod
    def from_dict(cls, data):
        obj = cls.__new__(cls)
        for k, v in data.items():
            setattr(obj, k, v)
        return obj

    def to_dict(self):
        result = vars(self).copy()
        for k in result.keys():
            if not k.lower():
                del result[k]
        return result


class BaseManager(ABC):

    def __init__(self, config: dict) -> None:
        self._config = config or {}

    @property
    def config(self):
        return self._config

    @abstractmethod
    def create(self, m: BaseModel) -> Any:
        """
        Generates a new _id for the instance 'm' and store it.
        Then returns a handle of that (path or _id)
        """
        pass

    @abstractmethod
    def read(self, id: int, model_cls: type) -> BaseModel:
        """
        Returns a model by its class and id
          and None if not found
        """
        pass

    @abstractmethod
    def update(self, m: BaseModel) -> None:
        """
        Update model with id == m.id with new object 'm' new data
        """
        pass

    @abstractmethod
    def delete(self, id: int, model_cls: type) -> None:
        """
        Removes a specific model
        """
        pass

    @abstractmethod
    def read_all(self, model_cls: type) -> Generator:
        """
        Returns a generator of all stored models with type == model_cls
        (Optional: Returns all stored models (non-type-sensitive) if models_cls == None)
        """
        pass

    @abstractmethod
    def truncate(self, model_cls: type) -> None:
        """
        Remove all stored models with type == model_cls
        (Optional: Remove all stored models (non-type-sensitive) if models_cls == None)
        """
        pass
