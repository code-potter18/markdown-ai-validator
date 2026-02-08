import re
import requests

def validate_markdown(text):
    issues = []

    # Check broken links
    urls = re.findall(r'https?://[^\s\)\]]+', text)
    for url in urls:
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code >= 400:
                issues.append({
                    "issue": f"Broken link: {url}",
                    "fix": "Update or correct the URL"
                })
        except requests.RequestException:
            issues.append({
                "issue": f"Broken link: {url}",
                "fix": "Update or correct the URL"
            })

    # Missing top-level heading
    if not text.lstrip().startswith("# "):
        issues.append({
            "issue": "Missing top-level heading",
            "fix": "Add a heading at the start of the file"
        })

    # Empty headings
    headings = re.findall(r'^(#+)\s*(.*)', text, re.MULTILINE)
    for level, content in headings:
        if not content.strip():
            issues.append({
                "issue": f"Heading '{level}' has no content",
                "fix": "Add text after the heading"
            })

    return issues
