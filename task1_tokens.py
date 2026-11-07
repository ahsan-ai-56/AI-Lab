import Retriever

FAQ = [
    {"id": "faq:password", "question": "How do I reset my password?",
     "answer": "Use the recovery link on the login page.",
     "source": "it_help.txt"},
    {"id": "faq:submit", "question": "Where do I submit my assignment?",
     "answer": "Use the assignment upload page in the learning portal.",
     "source": "assessment.txt"},
    {"id": "faq:late", "question": "Can illness justify a late submission?",
     "answer": "Request an extension with medical evidence before the deadline.",
     "source": "handbook.txt"}
]


def build_bot(backend="tfidf"):
    records = [dict(r, text=r["question"] + " " + r["answer"]) for r in FAQ]
    return Retriever(records, backend)


def reply(engine, query):
    if not query.strip():
        return "Please enter a question."

    # Only exact canonical FAQ text is answered automatically here.
    for r in FAQ:
        if query.strip().casefold() == r["question"].casefold():
            return r["answer"] + " [source: " + r["source"] + "]"

    hits = engine.search(query)

    if not hits:
        return "No matching FAQ. Please contact the help desk."

    lines = ["Possible matches; choose or rephrase your question:"]

    for r, score in hits:
        lines.append(r["question"] + f" (similarity {score:.3f})")

    return "\n".join(lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", choices=["tfidf", "embedding"],
                        default="tfidf")
    args = parser.parse_args()

    engine = build_bot(args.backend)
    print("FAQ assistant. Type exit to stop.")

    while True:
        try:
            query = input("You: ")
        except (EOFError, KeyboardInterrupt):
            break

        if query.strip().lower() == "exit":
            break

        print("Bot:", reply(engine, query))


import re

samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 version 2.1",
]

for text in samples:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print(repr(text), "whitespace:", ws, len(ws))
    print("word-like:", words, len(words))

assert re.findall(r"\b\w+\b", "") == []

from sentence_transformers import SentenceTransformer

model = SentenceTransformer( "sentence-transformers/all-MiniLM-L6-v2",device="cpu")

for text in samples[:2]:
    print(text, model.tokenizer.tokenize(text))
