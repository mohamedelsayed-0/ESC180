import math

def norm(vec):
    sum_sq = 0.0
    for k in vec:
        sum_sq += vec[k] * vec[k]
    return math.sqrt(sum_sq)


def cosine_similarity(vec1, vec2):
    if len(vec1) <= len(vec2):
        small, big = vec1, vec2
    else:
        small, big = vec2, vec1

    dot = 0.0
    for k in small:
        if k in big:
            dot += small[k] * big[k]

    n1 = norm(vec1)
    n2 = norm(vec2)
    if n1 == 0.0 or n2 == 0.0:
        return -1.0  # cannot be computed

    return dot / (n1 * n2)


def build_semantic_descriptors(sentences):
    descriptors = {}

    for sentence in sentences:
        unique = set(sentence)

        for w in unique:
            if w not in descriptors:
                descriptors[w] = {}

            for co in unique:
                if co == w:
                    continue
                descriptors[w][co] = descriptors[w].get(co, 0) + 1

    return descriptors


def build_semantic_descriptors_from_files(filenames):
    parts = []
    for fname in filenames:
        with open(fname, "r", encoding="latin1") as f:
            parts.append(f.read())
    text = "\n".join(parts).lower()

    for sep in ["?", "!", "."]:
        text = text.replace(sep, ".")

    raw_sentences = text.split(".")
    sentences = []

    # punctuation removal (replace with spaces)
    # do "--" before "-" so it actually has an effect
    punct = ["--", ",", "-", ":", ";"]

    for s in raw_sentences:
        for p in punct:
            s = s.replace(p, " ")
        words = s.split()
        if words:
            sentences.append(words)

    return build_semantic_descriptors(sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    best_choice = choices[0]
    best_sim = -1.0

    if word not in semantic_descriptors:
        return best_choice

    for c in choices:
        if c not in semantic_descriptors:
            sim = -1.0
        else:
            sim = similarity_fn(semantic_descriptors[word], semantic_descriptors[c])

        if sim > best_sim:
            best_sim = sim
            best_choice = c

    return best_choice


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct = 0
    total = 0

    with open(filename, "r", encoding="latin1") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 3:
                continue

            word = parts[0]
            answer = parts[1]
            choices = parts[2:]

            guess = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
            if guess == answer:
                correct += 1
            total += 1

    return 0.0 if total == 0 else (correct / total) * 100.0


if __name__ == "__main__":
    sentences = [
        ["i", "am", "a", "sick", "man"],
        ["i", "am", "a", "spiteful", "man"],
        ["i", "am", "an", "unattractive", "man"],
        ["i", "believe", "my", "liver", "is", "diseased"],
        ["however", "i", "know", "nothing", "at", "all", "about",
         "my", "disease", "and", "do", "not", "know", "for", "certain",
         "what", "ails", "me"]
    ]

    sem = build_semantic_descriptors(sentences)
    print("cos(man, liver) =", cosine_similarity(sem["man"], sem["liver"]))
