from typing import Dict, Union

JSONPrimitive = Union[int, str, float, bool, None]
PythonDeserializedJSON = Dict[str, JSONPrimitive]
