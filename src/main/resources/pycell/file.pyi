from pycell.client import VizierDBClient as VizierDBClient
from typing import Any, Dict, Optional

class FileClient:
    client: Any = ...
    name: Any = ...
    io: Any = ...
    filename: Any = ...
    identifier: Any = ...
    file_path: Any = ...
    meta_url: Any = ...
    url: Any = ...
    open_mode: Any = ...
    def __init__(self, client: VizierDBClient, name: str, mime_type: str=..., filename: Optional[str]=..., metadata: Optional[Dict[str, str]]=..., open_mode: str=...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: Any, value: Any, traceback: Any): ...
