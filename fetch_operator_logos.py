"""Download source operator logos for the Partners page."""

from pathlib import Path
from urllib.request import Request, urlopen

ASSETS = Path(__file__).parent / "dist" / "assets" / "operators"
ASSETS.mkdir(parents=True, exist_ok=True)

LOGOS = {
    "viettel.svg": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Viettel_logo_2021.svg",
    "movitel.jpg": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Movitel-Logo.jpg",
    "lumitel.jpg": "https://commons.wikimedia.org/wiki/Special:Redirect/file/LUMITEL_LOGO-01.jpg",
    "telemor.png": "https://upload.wikimedia.org/wikipedia/commons/9/9d/The_Telemor_Logo.png",
    "halotel.png": "https://halotel.co.tz/themes/halotel/images/logo4.png",
    "natcom.png": "https://upload.wikimedia.org/wikipedia/commons/6/62/The_Natcom_Logo.png",
    "nexttel.webp": "https://portal.powertec.com.au/sites/default/files/styles/scale_square/public/2023-11/Nexttel-Cameroon-Logo.png.webp?itok=COPw1MP6",
}

for name, url in LOGOS.items():
    if (ASSETS / name).exists():
        continue
    request = Request(url, headers={"User-Agent": "DIGICOM website asset preparation"})
    try:
        with urlopen(request, timeout=30) as response:
            content = response.read()
            content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            raise ValueError(f"Unexpected content type: {content_type}")
        (ASSETS / name).write_bytes(content)
        print(name, len(content), content_type)
    except Exception as error:
        print(name, "FAILED", error)
