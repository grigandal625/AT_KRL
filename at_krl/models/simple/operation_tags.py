TAGS_SIGNS = {
    "eq": {
        "values": ["=", "==", "eq"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "gt": {
        "values": [">", "gt"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "ge": {
        "values": [">=", "ge"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "lt": {
        "values": ["<", "lt"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "le": {
        "values": ["<=", "le"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "ne": {
        "values": ["<>", "!=", "ne"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "and": {
        "values": ["&", "&&", "and"],
        "is_binary": True,
        "meta": "log",
    },
    "or": {
        "values": ["|", "||", "or"],
        "is_binary": True,
        "meta": "log",
    },
    "not": {
        "values": ["~", "!", "not"],
        "is_binary": False,
        "meta": "log",
    },
    "xor": {
        "values": ["xor"],
        "is_binary": True,
        "meta": "log",
    },
    "neg": {
        "values": ["-", "neg"],
        "is_binary": False,
        "meta": "super_math",
    },
    "add": {
        "values": ["+", "add"],
        "is_binary": True,
        "meta": "math",
    },
    "sub": {
        "values": ["-", "sub"],
        "is_binary": True,
        "meta": "math",
    },
    "mul": {
        "values": ["*", "mul"],
        "is_binary": True,
        "meta": "math",
    },
    "div": {
        "values": ["/", "div"],
        "is_binary": True,
        "meta": "math",
    },
    "mod": {
        "values": ["%", "mod"],
        "is_binary": True,
        "meta": "super_math",
    },
    "pow": {
        "values": ["^", "**", "pow"],
        "is_binary": True,
        "meta": "super_math",
    },
}
