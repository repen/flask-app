"""
Copyright 2022 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""
from dataclasses import dataclass, field
from typing import List, Any, Union, Dict


class IBase:

    def to_dict(self):
        return self._asdict()

    def _asdict(self):
        return self.__dict__



@dataclass
class MessageProtocol(IBase):
    status_code: int
    payload: Union[List, Dict, None]
    action: str
    message: str