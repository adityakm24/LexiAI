import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.stats import wasserstein_distance

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Paths to synthetic and real-world data
synthetic_data_path = "../synthetic_legal_data"
real_examples = [
    "This Privacy Policy explains how we collect, use, and disclose personal information in compliance with GDPR and HIPAA.",
    "Terms of Service outline the obligations of users and limitations of liability under applicable laws.",
    "An employment contract specifies the rights and responsibilities of both the employer and the employee."
]


# Function to generate embeddings
def generate_embeddings(data):
    return model.encode(data, convert_to_tensor=False)


# Function to calculate Wasserstein distance
def calculate_wasserstein_distance(synthetic_embeddings, real_embeddings):
    distances = []
    for synthetic_doc in synthetic_embeddings:
        # Compute Wasserstein distance between each synthetic doc and the real dataset
        for real_doc in real_embeddings:
            dist = wasserstein_distance(synthetic_doc, real_doc)
            distances.append(dist)
    avg_distance = np.mean(distances)
    return avg_distance


# Load and process synthetic data
synthetic_data_files = [f for f in os.listdir(synthetic_data_path) if f.endswith(".json")]

for synthetic_file in synthetic_data_files:
    with open(os.path.join(synthetic_data_path, synthetic_file), "r", encoding="utf-8") as f:
        synthetic_data = json.load(f)

    # Generate embeddings
    synthetic_embeddings = generate_embeddings(synthetic_data)
    real_embeddings = generate_embeddings(real_examples)

    # Calculate Wasserstein distance
    avg_wasserstein_distance = calculate_wasserstein_distance(synthetic_embeddings, real_embeddings)
    print(f"Wasserstein distance for {synthetic_file}: {avg_wasserstein_distance:.4f}")
