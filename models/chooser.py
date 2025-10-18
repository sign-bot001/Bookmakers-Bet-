from dataclasses import dataclass
from typing import Dict, Any, List, Optional

@dataclass
class BetOption:
    market: str
    selection: str
    odds: float
    p: float
    ev: float
    confidence: int
    meta: Dict[str, Any]

def ev_from_p_odds(p: float, odds: float) -> float:
    return p*odds - (1 - p)

def confidence_from(p: float, ev: float, data_quality: float=1.0):
    base = (p*100*0.6) + (max(ev,0)*100*0.4)
    return int(max(0, min(100, round(base*data_quality))))

def pick_best(options: List[BetOption]) -> Optional[BetOption]:
    options = [o for o in options if o.ev is not None]
    if not options: return None
    options.sort(key=lambda x: (x.ev, x.confidence), reverse=True)
    return options[0]
