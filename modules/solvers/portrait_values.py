"""
Phantom-Hand: Schwartz Portrait Values Questionnaire (PVQ-57) Profiler
Calculates optimal responses for 57 universal human values dimensions
aligned with corporate culture (Kawan Lama Group: Integrity, Humility, Respect, Teamwork).
"""

from typing import Dict, Any, List


class PortraitValuesProfiler:
    """
    Evaluates 57 items of the Portrait Values Questionnaire (PVQ-57).
    Scale: 0 = Sama sekali tidak mirip s/d 5 = Sangat mirip dengan saya.
    """

    VALUE_SCORES: Dict[int, int] = {
        1: 5,   # Self-Direction: Thought
        2: 5,   # Security: Societal
        3: 4,   # Hedonism (balanced)
        4: 4,   # Conformity: Interpersonal
        5: 5,   # Universalism: Concern
        6: 0,   # Power: Dominance (authoritarian - negative)
        7: 5,   # Humility (positive)
        8: 5,   # Universalism: Nature
        9: 1,   # Face: Pride/Fragile ego
        10: 4,  # Stimulation: Variety
        11: 5,  # Benevolence: Caring
        12: 0,  # Power: Wealth/Greed (negative)
        13: 5,  # Security: Personal Health
        14: 5,  # Universalism: Tolerance
        15: 5,  # Conformity: Rules
        16: 5,  # Self-Direction: Action Autonomy
        17: 5,  # Achievement: Ambition
        18: 4,  # Tradition: Cultural respect
        19: 5,  # Benevolence: Dependability
        20: 1,  # Power: Wealth accumulation
        21: 5,  # Universalism: Nature action
        22: 5,  # Conformity: Non-disturbance
        23: 5,  # Self-Direction: Independent opinion
        24: 4,  # Face: Professional image
        25: 5,  # Benevolence: Caring
        26: 5,  # Security: Personal
        27: 5,  # Benevolence: Trustworthy friend
        28: 3,  # Stimulation: Risk taking (moderate)
        29: 0,  # Power: Imposing will (negative)
        30: 5,  # Self-Direction: Personal planning
        31: 5,  # Integrity: Rule following unwatched
        32: 5,  # Achievement: Success
        33: 5,  # Tradition & Spiritual/Family respect
        34: 5,  # Universalism: Listening to diversity
        35: 5,  # Security: Societal strength
        36: 4,  # Hedonism: Enjoying life
        37: 5,  # Universalism: Equality of opportunity
        38: 5,  # Humility: Modesty (Core Kawan Lama Value)
        39: 5,  # Self-Direction: Independent learning
        40: 5,  # Tradition: Cultural respect
        41: 0,  # Power: Micromanagement/Tyranny (negative)
        42: 5,  # Conformity: Law abiding
        43: 5,  # Stimulation: Novel experiences
        44: 0,  # Power: Flexing wealth/Expensive items (negative)
        45: 5,  # Universalism: Protecting environment
        46: 2,  # Hedonism: Constant pleasure seeking (low discipline)
        47: 5,  # Benevolence: Caring for loved ones
        48: 4,  # Achievement: Recognition of success
        49: 4,  # Face: Dignity
        50: 5,  # Security: Societal safety
        51: 4,  # Conformity: Interpersonal harmony
        52: 5,  # Universalism: Fairness to strangers
        53: 5,  # Security: Hazard avoidance
        54: 4,  # Humility: Contentment
        55: 5,  # Benevolence: Fully dependable
        56: 5,  # Self-Direction: Free choice
        57: 5   # Universalism: Tolerance of dissenting views (left for user)
    }

    OPTION_TEXTS = [
        "Sama sekali tidak mirip dengan saya",  # 0
        "Tidak mirip dengan saya",              # 1
        "Sedikit mirip dengan saya",            # 2
        "Agak mirip dengan saya",               # 3
        "Mirip dengan saya",                    # 4
        "Sangat mirip dengan saya"              # 5
    ]

    @classmethod
    def get_score_index(cls, question_num: int) -> int:
        return cls.VALUE_SCORES.get(question_num, 5)

    @classmethod
    def get_option_text(cls, question_num: int) -> str:
        idx = cls.get_score_index(question_num)
        return cls.OPTION_TEXTS[idx]

    @classmethod
    def get_all_answers(cls, exclude_last: bool = True) -> Dict[int, int]:
        mapping = dict(cls.VALUE_SCORES)
        if exclude_last and 57 in mapping:
            del mapping[57]
        return mapping
