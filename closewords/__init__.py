from rapidfuzz import fuzz
from unidecode import unidecode

def closeWords(q, candidates):
    word = unidecode(q)
    results = []
    for candidate in candidates:
        after_candidate = unidecode(candidate)
        score = fuzz.ratio(word, after_candidate)/100
        results.append({"word":candidate,"score":score})
    results.sort(key=lambda candidates: candidates["score"], reverse=True)
    return results
