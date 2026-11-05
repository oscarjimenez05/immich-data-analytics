import re
import httpx

def round_coords(lat: float, lon: float, precision: int = 3):
    """Rounds coordinates to deduplicate API calls (~110m resolution for precision=3)."""
    return round(lat, precision), round(lon, precision)

def fetch_weather_hour(lat: float, lon: float, timestamp_iso: str):
    """Queries Open-Meteo historical archive without an API key."""
    date_str = timestamp_iso[:10]
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}&longitude={lon}&start_date={date_str}&end_date={date_str}"
        f"&hourly=temperature_2m,precipitation,weather_code"
    )
    with httpx.Client(timeout=10.0) as client:
        res = client.get(url)
        return res.json() if res.status_code == 200 else None

def extract_ocr_entities(text: str):
    """Regex scanning to create m:n entities from raw OCR."""
    if not text:
        return []
    entities = []
    # Find totals / currency
    totals = re.findall(r'(?:total|subtotal|balance|amount due)[:\s]*\$?([0-9]+\.[0-9]{2})', text, re.I)
    for t in totals:
        entities.append(("FINANCIAL_TOTAL", t))
    # Find ISBNs
    isbns = re.findall(r'(?:97[89][0-9]{10}|[0-9]{9}[0-9Xx])', text)
    for isbn in isbns:
        entities.append(("BOOK_ISBN", isbn))
    return entities