import os
import json
import nltk
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

nltk.download('punkt')

# Path to the synthetic data folder
data_folder = "../../synthetic_legal_data"


def analyze_lexical_diversity(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        synthetic_data = json.load(f)

    all_tokens = []
    unique_tokens = set()

    for doc in synthetic_data:
        tokens = nltk.word_tokenize(doc)
        all_tokens.extend(tokens)
        unique_tokens.update(tokens)

    # Calculate lexical diversity
    lexical_diversity = len(unique_tokens) / len(all_tokens) if all_tokens else 0
    print(f"Lexical diversity for {os.path.basename(file_path)}: {lexical_diversity:.4f}")
    return lexical_diversity


def check_document_structure(file_path, expected_sections):
    with open(file_path, "r", encoding="utf-8") as f:
        synthetic_data = json.load(f)

    missing_sections = []
    for i, doc in enumerate(synthetic_data):
        for section in expected_sections:
            if section.lower() not in doc.lower():
                missing_sections.append((i, section))

    if missing_sections:
        print(f"Documents with missing sections in {os.path.basename(file_path)}:")
        for doc_id, section in missing_sections:
            print(f"  - Document {doc_id + 1} is missing section: {section}")
    else:
        print(f"All documents in {os.path.basename(file_path)} have the expected structure.")


def analyze_bias(file_path, terms):
    with open(file_path, "r", encoding="utf-8") as f:
        synthetic_data = json.load(f)

    term_counts = Counter()
    for doc in synthetic_data:
        tokens = nltk.word_tokenize(doc)
        term_counts.update([token.lower() for token in tokens if token.lower() in terms])

    # Plot term frequencies
    df = pd.DataFrame(term_counts.items(), columns=["Term", "Frequency"]).sort_values(by="Frequency", ascending=False)
    print(f"\nTop terms in {os.path.basename(file_path)}:")
    print(df.head(10))
    df.plot(kind="bar", x="Term", y="Frequency", legend=False, title="Term Frequency")
    plt.show()


# Define expected sections for validation
expected_sections = ["Data Collection", "User Rights", "Termination Clause", "Limitation of Liability"]

# Define terms to check for bias
bias_terms = ["california", "gdpr", "hipaa", "john", "jane", "europe", "usa"]

# Run analysis on all files
for file_name in os.listdir(data_folder):
    if file_name.endswith(".json"):
        file_path = os.path.join(data_folder, file_name)

        # Lexical diversity
        analyze_lexical_diversity(file_path)

        # Structural validation
        check_document_structure(file_path, expected_sections)

        # Bias analysis
        analyze_bias(file_path, bias_terms)
