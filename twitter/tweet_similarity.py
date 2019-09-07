from difflib import SequenceMatcher

similarity_threshold = 0.7


def are_similar(t1, t2):
    ratio = SequenceMatcher(None, t1, t2).ratio()
    return ratio > similarity_threshold


def are_similar_text(t1, t2):
    # sub1 = t1[0:t1.find('\n\n')]
    sub1 = t1[0:t1.find('http')]
    return are_similar(sub1, t2)
