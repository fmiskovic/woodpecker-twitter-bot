from difflib import SequenceMatcher

similarity_threshold = 0.7


def are_similar(t1, t2):
    ratio = SequenceMatcher(None, t1, t2).ratio()
    return ratio > similarity_threshold
