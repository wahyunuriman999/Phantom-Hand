"""
Workplace Competency & Learning Agility Profiler Engine
Calculates optimal Likert-scale responses for organizational assessments
(e.g., Kawan Lama Group, Astra, Telkom, BUMN) while balancing authenticity
and high-percentile competency ratings.
"""

from typing import Dict, List, Any, Optional


class CompetencyDimension:
    MENTAL_AGILITY = "Mental Agility"      # Critical thinking, curiosity, complexity navigation
    PEOPLE_AGILITY = "People Agility"      # Collaboration, active listening, coaching, feedback
    CHANGE_AGILITY = "Change Agility"      # Adaptability, comfort with ambiguity, experimentation
    RESULTS_AGILITY = "Results Agility"    # Drive for excellence, execution under shifting goals
    SELF_AWARENESS = "Self Awareness"      # Continuous learning, seeking feedback, knowing limits


class CompetencyProfiler:
    """
    Evaluates behavioral statements against modern corporate competency frameworks
    to generate optimal Likert responses (scale 1 to 5).
    """

    DIMENSION_KEYWORDS = {
        CompetencyDimension.MENTAL_AGILITY: [
            "logis", "informasi baru", "mempelajari", "analitis", "kritis", "menggali", "pemecahan masalah"
        ],
        CompetencyDimension.PEOPLE_AGILITY: [
            "orang lain", "bekerja sama", "tim", "didatangi", "bantuan", "berkenalan", "belajar dari orang"
        ],
        CompetencyDimension.CHANGE_AGILITY: [
            "berubah", "kondisi", "situasi", "suasana", "arah", "tanpa arahan", "cara lain", "gagal"
        ],
        CompetencyDimension.RESULTS_AGILITY: [
            "hasil", "efektif", "efisien", "menyelesaikan", "inisiatif", "menggunakan pengetahuan"
        ],
        CompetencyDimension.SELF_AWARENESS: [
            "feedback", "keterampilan", "pendekatan terbaik", "kemampuan"
        ]
    }

    @classmethod
    def classify_statement(cls, text: str) -> str:
        """Classifies a statement into its primary competency dimension."""
        text_lower = text.lower()
        scores = {}
        for dim, keywords in cls.DIMENSION_KEYWORDS.items():
            count = sum(1 for kw in keywords if kw in text_lower)
            scores[dim] = count
        best_dim = max(scores, key=scores.get)
        return best_dim if scores[best_dim] > 0 else CompetencyDimension.MENTAL_AGILITY

    @classmethod
    def score_statement(cls, text: str) -> int:
        """
        Determines the optimal Likert response:
        - 5 (Selalu dilakukan): For collaboration, positive resilience, initiative, and growth mindset.
        - 4 (Sangat sering dilakukan): For self-claim items (e.g. 'mengingat dengan mudah', 'menikmati perubahan')
          where rating 5 might trigger a lie/faking-good social desirability flag.
        """
        text_lower = text.lower()
        
        # Items that might trigger social desirability detection if marked with absolute 5:
        subtle_moderation_triggers = [
            "mengingat informasi baru dengan mudah",
            "menikmati perubahan suasana",
            "tidak langsung menerima informasi",
            "topik di luar bidang",
            "berkenalan dengan banyak orang untuk mencari tahu cara"
        ]
        
        for trigger in subtle_moderation_triggers:
            if trigger in text_lower:
                return 4

        return 5

    @classmethod
    def build_profile(
        cls, 
        questions: List[Dict[str, Any]], 
        exclude_last: bool = True
    ) -> Dict[int, Dict[str, Any]]:
        """
        Builds a comprehensive scoring map for a list of questions.
        If exclude_last is True, the final question is flagged for Human-in-the-Loop review.
        """
        profile = {}
        total = len(questions)
        for idx, q in enumerate(questions, start=1):
            is_last = (idx == total)
            text = q.get("text", "")
            dim = cls.classify_statement(text)
            score = cls.score_statement(text)
            
            profile[idx] = {
                "question_num": idx,
                "text": text,
                "dimension": dim,
                "recommended_score": score,
                "leave_for_user": is_last and exclude_last
            }
        return profile
