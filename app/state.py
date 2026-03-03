from typing import TypedDict, Optional, Dict

class CivilState(TypedDict):
    query: str
    intent: Optional[str]
    bbs_input: Optional[Dict]
    bbs_data: Optional[Dict]
    weather_data: Optional[Dict]
    material_data: Optional[Dict]
    iscode_text: Optional[str]
