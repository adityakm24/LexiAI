from src.jurisdiction_mapping import map_to_jurisdiction

def test_jurisdiction_mapping():
    """Test the jurisdiction mapping function."""
    test_text = """
    This document outlines the requirements for processing personal data in the EU
    in accordance with GDPR Article 28.
    """
    jurisdictions = map_to_jurisdiction(test_text)
    assert "GDPR" in jurisdictions, "GDPR should be identified."

    test_text_2 = """
    The company must allow California residents to opt-out of the sale of their personal data,
    as required by the CCPA.
    """
    jurisdictions = map_to_jurisdiction(test_text_2)
    assert "CCPA" in jurisdictions, "CCPA should be identified."

    print("All tests passed!")

if __name__ == "__main__":
    test_jurisdiction_mapping()
