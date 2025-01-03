from sentence_transformers import SentenceTransformer, util
import json
import numpy as np
import os
import torch

# Load a pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Path to the generated data
data_folder = "../synthetic_legal_data"

# Real-world examples for validation (add examples for comparison)
real_examples = [
    "This Privacy Policy explains how we collect, use, and disclose personal information in compliance with GDPR and HIPAA.",
    "Terms of Service outline the obligations of users and limitations of liability under applicable laws.",
    "An employment contract specifies the rights and responsibilities of both the employer and the employee."
]

def validate_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        synthetic_data = json.load(f)

    # Embed real examples
    real_embeddings = model.encode(real_examples, convert_to_tensor=True)

    similarities = []
    for doc in synthetic_data:
        synthetic_embedding = model.encode(doc, convert_to_tensor=True)
        # Compute cosine similarity
        similarity_scores = util.pytorch_cos_sim(synthetic_embedding, real_embeddings)
        max_similarity = torch.max(similarity_scores).item()
        similarities.append(max_similarity)

    # Average similarity across all documents
    avg_similarity = np.mean(similarities)
    print(f"Average semantic similarity for {os.path.basename(file_path)}: {avg_similarity:.4f}")

# Validate all generated files
for file_name in os.listdir(data_folder):
    if file_name.endswith(".json"):
        validate_data(os.path.join(data_folder, file_name))
