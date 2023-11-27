from compsoc.profile import Profile
from typing import Callable

# my rule

def get_borda_xform(xform: float = 2) -> Callable[[int], float]:
    """
    Returns a callable function for the Borda alpha method with the specified decay alpha.

    :param alpha: The decay factor for Borda alpha, defaults to 0.5.
    :type alpha: float, optional
    :return: A callable function for the Borda alpha method.
    :rtype: Callable[[int], float]
    """

    def borda_xform(profile: Profile, candidate: int) -> float:
        """
        Calculates the Borda alpha (decay 2) score for a candidate
        :param profile: The voting profile.
        :type profile: VotingProfile
        :param candidate: The base candidate for scoring.
        :type candidate: int
        :return: The Borda alpha score for the candidate.
        :rtype: float
        """
        # Max score to be applied with borda count
        top_score = len(profile.candidates) - 1

        # Get pairwise scores
        scores = 0
        for pair in profile.pairs:
            # Adds score only if the candidate appears in the ballots. 
            # Supports the case when the ballots are distorted.
            if candidate in pair[1]:
                scores += pair[0] * (((top_score - pair[1].index(candidate))  / top_score) ** xform)
        return scores
    
    return borda_xform
