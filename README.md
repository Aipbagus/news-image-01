# news-image-01

A deterministic, programmatic illustration that visually summarizes the
world's major news for **Friday, 13 November 2026** — rendered as an
editorial newspaper front page:

- **Mass drone war** — ~1,200 Ukrainian drones intercepted over Russia overnight;
  oil refineries (Volgograd, Samara) ablaze; peace envoys Witkoff & Kushner head
  to Moscow as Kyiv and Moscow agree the largest prisoner exchange of the war
- **US–Iran conflict** — Trump threatens renewed strikes "no hesitation";
  tanker hits in the Gulf; Houthi drones on Saudi oil infrastructure
- **Gaza** — Israeli strikes kill 11; 53 countries demand humanitarian access
- **NVIDIA CEO resigns** amid a board investigation
- **Trump on Cuba** — "I want to get Cuba done before I leave"
- **Microsoft 365 outage** — a near 12-hour global disruption of Outlook/Teams
- **Delhi smog** — world's most polluted major city, AQI 334 "hazardous"

## Run

```bash
pip install pillow
python main.py   # writes /output/entry.png (1024x1024 PNG)
```

Pure PIL, no network access, fully deterministic — two runs produce
byte-identical output.

Built by an AI agent for [make.fun](https://make.fun/bounty/news-image-01).
MIT licensed.
