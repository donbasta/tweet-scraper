from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    Username: Optional[str] = None
    User_id: Optional[str] = None
    Limit: Optional[str] = None
    Bearer_token: str = None
