"""
Phantom-Hand: Workplace Personality Inventory Solver (Big Five / 60-Item Inventory)
Automates psychometric scoring for corporate personality tests (Emotional Stability,
Conscientiousness, Extraversion, Agreeableness, Openness) with anti-faking moderation.
"""

from typing import Dict, Any, List


class PersonalityInventorySolver:
    """
    Evaluation engine for 60-item Workplace Personality Assessments (Big Five Framework).
    """

    # Directional scoring rules
    FAVORABLE_ITEMS = [
        9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
        30, 37, 38, 41, 42, 47, 48, 49, 50, 51, 53, 55, 56, 57, 59, 60
    ]

    UNFAVORABLE_ITEMS = [
        1, 2, 3, 4, 5, 6, 7, 8, 16, 28, 31, 32, 33, 34, 39, 40, 43, 44, 45, 46,
        52, 54, 58
    ]

    NEUTRAL_POLITICAL_ITEMS = [29, 35, 36]

    @classmethod
    def get_recommended_choice(cls, question_num: int, text: str = "") -> str:
        """Returns the optimal 5-point Likert response text."""
        if question_num in cls.NEUTRAL_POLITICAL_ITEMS:
            return "Netral"

        if question_num in cls.UNFAVORABLE_ITEMS:
            # Extreme negative traits get 'Sangat Tidak Sesuai'
            if question_num in [1, 2, 3, 4, 5, 6, 7, 8, 32, 39, 40, 43, 44, 46, 52, 54, 58]:
                return "Sangat Tidak Sesuai"
            return "Tidak Sesuai"

        # Favorable traits
        if question_num in [15, 19, 22, 23, 26, 27, 56, 59]:
            return "Sesuai"
        
        return "Sangat Sesuai"

    @classmethod
    def get_all_answers(cls, exclude_last: bool = True) -> Dict[int, str]:
        """Returns answers mapping for all items 1 to 60 (optionally excluding Q60)."""
        mapping = {i: cls.get_recommended_choice(i) for i in range(1, 61)}
        if exclude_last and 60 in mapping:
            del mapping[60]
        return mapping
