from tools import search_web, extract_text_from_url

links = search_web("AI in banking")
print("Links:", links)

if links:
    text = extract_text_from_url(links[0])
    print("\nExtracted text sample:\n", text[:500])