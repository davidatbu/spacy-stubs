from typing import Any

def add_codes(err_cls: Any): ...

class Warnings:
    W001: str = ...
    W002: str = ...
    W003: str = ...
    W004: str = ...
    W005: str = ...
    W006: str = ...
    W007: str = ...
    W008: str = ...
    W009: str = ...
    W010: str = ...
    W011: str = ...
    W012: str = ...
    W013: str = ...
    W014: str = ...
    W015: str = ...
    W016: str = ...
    W017: str = ...
    W018: str = ...
    W019: str = ...
    W020: str = ...
    W021: str = ...
    W022: str = ...
    W023: str = ...
    W024: str = ...
    W025: str = ...
    W026: str = ...
    W027: str = ...
    W028: str = ...

class Errors:
    E001: str = ...
    E002: str = ...
    E003: str = ...
    E004: str = ...
    E005: str = ...
    E006: str = ...
    E007: str = ...
    E008: str = ...
    E009: str = ...
    E010: str = ...
    E011: str = ...
    E012: str = ...
    E013: str = ...
    E014: str = ...
    E015: str = ...
    E016: str = ...
    E017: str = ...
    E018: str = ...
    E019: str = ...
    E020: str = ...
    E021: str = ...
    E022: str = ...
    E023: str = ...
    E024: str = ...
    E025: str = ...
    E026: str = ...
    E027: str = ...
    E028: str = ...
    E029: str = ...
    E030: str = ...
    E031: str = ...
    E032: str = ...
    E033: str = ...
    E034: str = ...
    E035: str = ...
    E036: str = ...
    E037: str = ...
    E038: str = ...
    E039: str = ...
    E040: str = ...
    E041: str = ...
    E042: str = ...
    E043: str = ...
    E044: str = ...
    E045: str = ...
    E046: str = ...
    E047: str = ...
    E048: str = ...
    E049: str = ...
    E050: str = ...
    E051: str = ...
    E052: str = ...
    E053: str = ...
    E054: str = ...
    E055: str = ...
    E056: str = ...
    E057: str = ...
    E058: str = ...
    E059: str = ...
    E060: str = ...
    E061: str = ...
    E062: str = ...
    E063: str = ...
    E064: str = ...
    E065: str = ...
    E066: str = ...
    E067: str = ...
    E068: str = ...
    E069: str = ...
    E070: str = ...
    E071: str = ...
    E072: str = ...
    E073: str = ...
    E074: str = ...
    E075: str = ...
    E076: str = ...
    E077: str = ...
    E078: str = ...
    E079: str = ...
    E080: str = ...
    E081: str = ...
    E082: str = ...
    E083: str = ...
    E084: str = ...
    E085: str = ...
    E086: str = ...
    E087: str = ...
    E088: str = ...
    E089: str = ...
    E090: str = ...
    E091: str = ...
    E092: str = ...
    E093: str = ...
    E094: str = ...
    E095: str = ...
    E096: str = ...
    E097: str = ...
    E098: str = ...
    E099: str = ...
    E100: str = ...
    E101: str = ...
    E102: str = ...
    E103: str = ...
    E104: str = ...
    E105: str = ...
    E106: str = ...
    E107: str = ...
    E108: str = ...
    E109: str = ...
    E110: str = ...
    E111: str = ...
    E112: str = ...
    E113: str = ...
    E114: str = ...
    E115: str = ...
    E116: str = ...
    E117: str = ...
    E118: str = ...
    E119: str = ...
    E120: str = ...
    E121: str = ...
    E122: str = ...
    E123: str = ...
    E124: str = ...
    E125: str = ...
    E126: str = ...
    E127: str = ...
    E128: str = ...
    E129: str = ...
    E130: str = ...
    E131: str = ...
    E132: str = ...
    E133: str = ...
    E134: str = ...
    E135: str = ...
    E136: str = ...
    E137: str = ...
    E138: str = ...
    E139: str = ...
    E140: str = ...
    E141: str = ...
    E142: str = ...
    E143: str = ...
    E144: str = ...
    E145: str = ...
    E146: str = ...
    E147: str = ...
    E148: str = ...
    E149: str = ...
    E150: str = ...
    E151: str = ...
    E152: str = ...
    E153: str = ...
    E154: str = ...
    E155: str = ...
    E156: str = ...
    E157: str = ...
    E158: str = ...
    E159: str = ...
    E160: str = ...
    E161: str = ...
    E162: str = ...
    E163: str = ...
    E164: str = ...
    E165: str = ...
    E166: str = ...
    E167: str = ...
    E168: str = ...
    E169: str = ...
    E170: str = ...
    E171: str = ...
    E172: str = ...
    E173: str = ...
    E174: str = ...
    E175: str = ...
    E176: str = ...
    E177: str = ...
    E178: str = ...
    E179: str = ...
    E180: str = ...
    E181: str = ...
    E182: str = ...
    E183: str = ...
    E184: str = ...
    E185: str = ...
    E186: str = ...
    E187: str = ...
    E188: str = ...
    E189: str = ...
    E190: str = ...
    E191: str = ...

class TempErrors:
    T003: str = ...
    T004: str = ...
    T007: str = ...
    T008: str = ...

class MatchPatternError(ValueError):
    def __init__(self, key: Any, errors: Any) -> None: ...

class AlignmentError(ValueError): ...
class ModelsWarning(UserWarning): ...

WARNINGS: Any
SPACY_WARNING_FILTER: Any
SPACY_WARNING_TYPES: Any
SPACY_WARNING_IGNORE: Any

def user_warning(message: Any) -> None: ...
def deprecation_warning(message: Any) -> None: ...
def models_warning(message: Any) -> None: ...
