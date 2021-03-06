from difflib import SequenceMatcher

similarity_threshold = 0.7


def are_similar(t1, t2):
    sub1 = t1[0:t1.find('http')].rstrip()
    sub2 = t2[0:t2.find('http')].rstrip()
    ratio = SequenceMatcher(None, sub1, sub2).ratio()
    return ratio > similarity_threshold


def are_similar_text(t1, t2):
    sub = t1[0:t1.find('#')].rstrip()
    return are_similar(sub, t2)


def are_similar_source(s1, s2):
    sub = s1[s1.find('http'):len(s1)].rstrip()
    return sub == s2
