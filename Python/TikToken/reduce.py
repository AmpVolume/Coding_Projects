import tiktoken
import string

encoding = tiktoken.get_encoding("cl100k_base")


def analyze_text(text):
    tokens = encoding.encode(text)
    num_tokens = len(tokens)

    suggestions = []

    if len(text) > 500:
        suggestions.append("Shorten long paragraphs.")

    if "  " in text:
        suggestions.append("Remove extra spaces.")

    if "\n\n\n" in text:
        suggestions.append("Reduce excessive line breaks.")

    if len(text.split()) > 80:
        suggestions.append("Summarize or compress wording.")

    if not suggestions:
        suggestions.append("Text is already efficient.")

    return num_tokens, suggestions


def compress_text(text):
    text = text.lower().strip()

    # -----------------------------
    # phrase-level removals
    phrase_fillers = [
        "you know", "i mean", "to be honest",
        "by the way", "i noticed",
        "what do you think", "what's your opinion",
        "to be honest with you", "at the end of the day",
        "for what it's worth", "that said", "having said that",
        "as i said", "in general"
    ]

    for phrase in phrase_fillers:
        text = text.replace(phrase, "")

    # -----------------------------
    # word-level fillers
    word_fillers = {
        "very", "really", "just", "basically",
        "actually", "maybe", "like",
        "um", "uh", "ah", "hmm", "oh", "please",
        "so", "well", "okay", "ok", "alright", "alrighty",
        "truly", "honestly", "literally",
        "pretty", "fairly", "quite", "a", "bit", "little", "slightly"
    }

    words = text.split()
    words = [w for w in words if w not in word_fillers]

    text = " ".join(words)

    # -----------------------------
    # replacements (FIXED MISSING PART)
    replacements = {
        "rate this": "rate efficiency",
        "rate it": "evaluate efficiency",
        "what i typed": "input text",
        "it was not good enough": "it was inefficient",
        "this program is": "program efficiency",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    # -----------------------------
    # normalize spacing
    text = " ".join(text.split())

    # -----------------------------
    # remove punctuation + repeated words
    cleaned = []
    for w in text.split():
        w = w.translate(str.maketrans("", "", string.punctuation))

        if w and (not cleaned or cleaned[-1] != w):
            cleaned.append(w)

    text = " ".join(cleaned)

    # -----------------------------
    # optional intent rewrite
    if "rate efficiency" in text:
        text = "Evaluate prompt efficiency and suggest improvements"

    return text