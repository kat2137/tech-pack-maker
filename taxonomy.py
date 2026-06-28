ELEMENTS = {
    "pocket": {
        "multiple": True,
        "detect": True,                                  
        "attributes": {
            "type":        {"fill": "vision",    "terms": ["welt", "patch", "slide-in", "chest", "patch with flap", "box pleat", "jetted", "welt with button", "cargo", "jetted with flap"]},
            "topstitched": {"fill": "vision",    "terms": ["yes", "no"]},   
            "flap":        {"fill": "vision",    "terms": ["yes", "no"]},
            "fused":       {"fill": "inference", "terms": ["yes", "no"]},    # invisible → app/setup
        },
    },
    "hood": {
        "multiple": False,
        "detect": True,                                  
        "attributes": {
            "drawstring": {"fill": "vision",    "terms": ["yes", "no"]},
            "lined":      {"fill": "inference", "terms": ["yes", "no"]},     # app/setup
        },
    },
    "lining":       {"multiple": False, "detect": True, "attributes": {}},   
    "shoulder_pads":{"multiple": False, "detect": True, "attributes": {}},
    "button": {
        "multiple": True,
        "detect": True,
        "attributes": {
            "type":         {"fill": "vision",    "terms": ["sewn-on", "stud", "snap"]}
        },
    },
    "placket":{
        "multiple": False,
        "detect": True,
        "attributes": {
            "type":          {"fill": "vision",    "terms": ["american", "covered", "concealed", "french", "popover"]},
            "topstitched":   {"fill": "vision",    "terms": ["yes", "no"]},
            "location":      {"fill": "vision",    "terms": ["front"]},
            "size":          {"fill": "vision",    "terms": ["full-lenght", "quarter", "half-lenght"]}
        }
    },
    "sleeve placket":{
        "multiple": True,
        "detect": True,
        "attributes": {
            "type":         {""}
        }
    },
    "cuffs":{
        "multiple": True,
        "detect": True,
        "attributes": {
            "types":                    {"fill": "vision",     "terms": ["angled", "rounded", "shotgun", "straight", "zipped", "ribbed", "piped", "frilled", "with ruffle", "strapped", "elasticated", "shirred", "turn-up", "tab", "barrel"]},
            "topstitched":              {"fill": "vision",     "terms": ["yes", "no"]},
            "button-closure":           {"fill": "vision",     "terms": ["yes", "no"]}
        }
    },
    "neckline":{
        "multiple": False,
        "detect": True,
        "attributes": {
            "types":                    {"fill": "vision",       "terms": ["scooped", "halter", "high", "split", "collar", "ribbed", "jabot", "v-neckline","crew", "funnel", "sweetheart", "assymetric", "cowl", "bandeau", "square", "boat neck", "keyhole", "off-shoulder", "turtleneck"]},
            "neckline facing":          {"fill": "inference",    "terms": ["yes", "no"]},
            "facing finish":            {"fill": "inference",    "terms": ["bagged out into lining", "overlocked", "pin hem", "folded hem", "binding"]},
            "neckline finish":          {"fill": "inference",    "terms": ["facing topstitched", "ribbing with coverstitch", "coverstitch", "binding", "placket", "raw", "frilled"]}
        }
    },
    "collar":{
        "multiple": False,
        "detect": True,
        "attributes": {
            "types":                    {"fill": "vision",      "terms": ["mandarin", "straight", "ribbed", "sailor", "notched", "bib", "jabot", "ruffle trim", "shawl", "funnel"]}
        }
    }
}
