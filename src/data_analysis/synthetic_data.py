import os
from openai import OpenAI
import json

# Set up OpenAI client
client = OpenAI(
    api_key=""
)

# Define templates for legal document generation
templates = [
    {
        "type": "Privacy Policy",
        "prompt": (
            "You are a legal expert. Generate a privacy policy for a SaaS company "
            "operating in the US and the EU. Ensure compliance with GDPR and HIPAA. "
            "Include sections on data collection, usage, user rights, and dispute resolution. Use sample data - like names of company, products, dates, and addresses. Do not ever have place holders!"
        ),
    },
    {
        "type": "Terms of Service",
        "prompt": (
            "You are a legal expert. Generate Terms of Service for a mobile app that "
            "operates globally. Include clauses for user responsibilities, limitations of liability, "
            "and jurisdictional compliance. Use sample data like names, dates, and addresses.  Use sample data - like names of company, products, dates, and addresses. Do not ever have place holders!"
        ),
    },
    {
        "type": "Employment Contract",
        "prompt": (
            "Generate an employment contract for a software engineer in California. "
            "Include clauses for at-will employment, non-disclosure, and intellectual property rights.  Use sample data - like names of company, products, dates, and addresses. Do not ever have place holders!."
        ),
    },
]

# Output folder for generated data
output_folder = "../synthetic_legal_data"
os.makedirs(output_folder, exist_ok=True)


def generate_documents(template, num_samples=40):
    print(f"Generating {template['type']} documents...")
    documents = []

    for i in range(num_samples):
        try:
            # Use chat.completions endpoint
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": template["prompt"],
                    }
                ],
                model="gpt-3.5-turbo",
                max_tokens=1500,  # Adjust token limit based on your requirements
                temperature=0.7,  # Adjust creativity level
                top_p=0.9,
                n=1,
            )
            print(f"Response {i + 1}: {response}")
            content = response.choices[0].message.content.strip()
            # Append the content to the documents list
            documents.append(content)
        except Exception as e:
            print(f"Error generating document {i + 1}: {e}")

    # Save the documents to a JSON file
    output_file = os.path.join(output_folder, f"{template['type'].replace(' ', '_').lower()}_samples.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=4)
    print(f"Saved {template['type']} documents to {output_file}")


# Generate documents for all templates
for template in templates:
    generate_documents(template, num_samples=40)

print("Synthetic legal document generation completed.")
