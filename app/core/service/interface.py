from dataclasses import dataclass, field
from typing import List, Any, Union, Dict


class IBase:

    def to_dict(self):
        return self._asdict()

    def _asdict(self):
        return self.__dict__


@dataclass
class IRequestProtocol(IBase):
    """Frontend Request protocol
    """
    action: str
    arguments: dict
    secret: field(default="secret")


@dataclass
class IBackendProtocol(IBase):
    """Backend Request protocol
    """
    data: List[Any]
    status_code: int
    message: str


@dataclass
class MessageProtocol(IBase):
    status_code: int
    payload: Union[List, Dict, None]
    action: str
    message: str