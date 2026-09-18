# 🚀 SarkariGK Backend & Serverless CDN Pipeline

This repository serves as the **100% Free Serverless Cloud CDN Backend** for the **SarkariGK (दैनिक करेंट अफेयर्स व जीके क्विज)** Flutter mobile app.

---

## 🏗️ Architecture

1. **Daily PIB Ingest & AI Compilation:**
   * Runs nightly at **2:00 AM IST** via GitHub Actions (`.github/workflows/daily_gk_cron.yml`).
   * Ingests official public domain releases from **Press Information Bureau (pib.gov.in)**.
   * Compiles 10 bilingual exam MCQs (SSC, Railway, Banking, UPSC) + 10 One-Liners using **Google Gemini 2.0 Flash (Free Tier)**.
2. **CDN Delivery (Zero Hosting Bills):**
   * Static JSON files are cached and delivered globally via **Fastly / jsDelivr / GitHub Pages CDN**.
   * Instant responses (< 50ms) across India with zero cloud server expenses.

---

## 📁 Repository Structure

```
├── .github/workflows/
│   └── daily_gk_cron.yml         # Nightly 2:00 AM IST automation runner
├── data/
│   ├── config.json               # Remote config (AdMob switch, Telegram link, update flags)
│   ├── categories.json           # GK categories metadata
│   ├── today_gk.json             # Today's active 10 MCQs + 10 One-Liners
│   └── archive/                  # Historical date-wise archive
│       └── 2026-09-18.json
└── scripts/
    ├── generate_daily_gk.py      # Automated generator script
    └── seed_data.py              # Offline seed generator
```

---

## ⚡ CDN Access Endpoints

Once you push this repo to your GitHub account (e.g. `systemiclogics-beep/sarkari-gk-data`), the files are immediately accessible globally via Fastly-backed CDN:

* **Today's GK Feed:**  
  `https://cdn.jsdelivr.net/gh/systemiclogics-beep/sarkari-gk-data@main/data/today_gk.json`
* **Remote App & Ad Config:**  
  `https://cdn.jsdelivr.net/gh/systemiclogics-beep/sarkari-gk-data@main/data/config.json`
* **Historical Archive:**  
  `https://cdn.jsdelivr.net/gh/systemiclogics-beep/sarkari-gk-data@main/data/archive/{YYYY-MM-DD}.json`

---

## 🔑 Setup GitHub Secrets

1. Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Click **New repository secret**.
3. Name: `GEMINI_API_KEY`
4. Value: Paste your Google AI Studio API key.
5. That's it! The nightly cron will now automatically update daily current affairs every night.
