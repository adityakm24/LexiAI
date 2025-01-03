def map_to_jurisdiction(text):
    """Map a legal document to relevant jurisdictions."""
    # Define jurisdiction-specific keywords
    JURISDICTION_KEYWORDS = {
        "GDPR": ["personal data", "data processing", "EU", "GDPR", "Article 28"],
        "CCPA": ["consumer privacy", "California", "CCPA", "opt-out", "sale of personal data"],
        "HIPAA": ["protected health information", "PHI", "healthcare", "HIPAA", "privacy rule"],
    }

    # Find matching jurisdictions based on keywords
    matched_jurisdictions = []
    for jurisdiction, keywords in JURISDICTION_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in text.lower():
                matched_jurisdictions.append(jurisdiction)
                break  # Stop checking further keywords for this jurisdiction

    if not matched_jurisdictions:
        return ["Unknown"]  # No jurisdiction matched

    return matched_jurisdictions
