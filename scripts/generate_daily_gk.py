#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SarkariGK Daily Content Generator
Fetches official releases from Press Information Bureau (PIB - pib.gov.in)
and synthesizes 10 high-yield exam MCQs + 10 One-Liners using Google Gemini Flash.
100% Zero-Scraping of Competitors, 100% Free Government Public Domain Data.
"""

import os
import sys
import json
import time
import datetime
import urllib.request
from bs4 import BeautifulSoup

def fetch_pib_releases(limit=15):
    """
    Fetches the latest official Government of India press releases from PIB.
    """
    url = "https://pib.gov.in/allRel.aspx?lflag=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    releases = []
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as response:
            html = response.read()
            soup = BeautifulSoup(html, "html.parser")
            items = soup.select("div.content-area ul li a")
            for item in items[:limit]:
                text = item.get_text(strip=True)
                href = item.get("href", "")
                if text:
                    releases.append(text)
    except Exception as e:
        print(f"[WARN] Error fetching PIB live releases: {e}", file=sys.stderr)
        
    # If network drops or PIB layout changes, provide fallback official headline topics
    if not releases:
        releases = [
            "Cabinet approves PM E-DRIVE Scheme with financial outlay of ₹10,900 crore",
            "SCO Ministers for Foreign Economic and Trade activities 25th meeting concludes in Dushanbe, Tajikistan",
            "Indian Navy commissions stealth guided missile frigate into Western Fleet",
            "ISRO validates Small Satellite Launch Vehicle third flight with EOS-08",
            "RBI MPC retains policy Repo Rate at 6.5% with focus on inflation containment",
            "Ministry of Youth Affairs felicitates medalists at Asian Youth Athletics Championships",
            "Ministry of Environment expands eco-sensitive wildlife corridor around national parks",
            "Cabinet approves Mission Mausam with ₹2,000 crore outlay for meteorological upgrade",
            "Appointments Committee of the Cabinet clears key administrative postings",
            "CSIR validates indigenous bio-fertilizer technology for dryland farming"
        ]
        
    return releases

def call_gemini_api(api_key, prompt):
    """
    Calls Google Gemini Flash API with strict JSON schema instructions.
    Uses exponential backoff retry mechanism (3 attempts).
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2,
            "responseMimeType": "application/json"
        }
    }
    
    data_bytes = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    
    for attempt in range(1, 4):
        try:
            print(f"[INFO] Calling Gemini API (Attempt {attempt}/3)...")
            req = urllib.request.Request(url, data=data_bytes, headers=headers)
            with urllib.request.urlopen(req, timeout=90) as res:
                res_body = res.read().decode("utf-8")
                res_json = json.loads(res_body)
                content_text = res_json["candidates"][0]["content"]["parts"][0]["text"]
                return json.loads(content_text)
        except Exception as err:
            print(f"[ERROR] Attempt {attempt} failed: {err}", file=sys.stderr)
            if attempt < 3:
                time.sleep(10 * attempt)
            else:
                raise

def validate_schema(data):
    """
    Ensures the generated JSON strictly obeys SarkariGK contract.
    """
    assert "questions" in data and len(data["questions"]) >= 5, "Questions missing or insufficient"
    assert "one_liners" in data and len(data["one_liners"]) >= 5, "One-liners missing or insufficient"
    
    for q in data["questions"]:
        assert "id" in q, "Question missing id"
        assert "question_en" in q and "question_hi" in q, "Question missing bilingual text"
        assert "options_en" in q and len(q["options_en"]) == 4, "options_en must have 4 items"
        assert "options_hi" in q and len(q["options_hi"]) == 4, "options_hi must have 4 items"
        assert q.get("correct_answer") in ["A", "B", "C", "D"], "Invalid correct_answer"
        assert "explanation_en" in q and "explanation_hi" in q, "Explanation missing bilingual text"
        
    print("[INFO] Schema validation passed successfully!")

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
        print("[INFO] For local testing without an API key, use seed_data.py.")
        sys.exit(1)
        
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    print(f"[INFO] Generating SarkariGK feed for date: {today_str}")
    
    releases = fetch_pib_releases()
    releases_text = "\n".join([f"- {r}" for r in releases])
    
    prompt = f"""
    You are an expert exam question-setter for Indian Government Competitive Exams (SSC CGL, Railway NTPC, Banking, UPSC Prelims, State Police).
    
    Based on the following official Government of India (PIB) releases:
    {releases_text}
    
    Today's Date: {today_str}
    
    Generate a JSON object with this exact structure:
    {{
      "date": "{today_str}",
      "title_en": "Daily Current Affairs & GK Dose - {today_str}",
      "title_hi": "दैनिक करेंट अफेयर्स व सामान्य ज्ञान - {today_str}",
      "total_questions": 10,
      "total_one_liners": 10,
      "questions": [
        {{
          "id": "gk_{today_str.replace('-', '_')}_01",
          "category": "national|international|defence|economy|science|appointments|sports|environment",
          "exam_tags": ["SSC CGL", "Railway NTPC", "UPSC Prelims"],
          "question_en": "Clear English exam question...",
          "question_hi": "परीक्षा-उपयोगी शुद्ध हिंदी प्रश्न...",
          "options_en": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
          "options_hi": ["A) विकल्प 1", "B) विकल्प 2", "C) विकल्प 3", "D) विकल्प 4"],
          "correct_answer": "A",
          "explanation_en": "Original 2-3 line explanation linking static GK (constitutional article, year, ministry, or headquarters).",
          "explanation_hi": "2-3 पंक्तियों में विस्तृत व्याख्या (संबंधित मंत्रालय, मुख्यालय, संवैधानिक अनुच्छेद आदि)।"
        }}
      ],
      "one_liners": [
        {{
          "id": "nl_{today_str.replace('-', '_')}_01",
          "category": "national|international|defence|economy|science|appointments|sports|environment",
          "note_en": "Crisp 1-line factual bullet point in English",
          "note_hi": "परीक्षा-उपयोगी 1-लाइन तथ्य हिंदी में"
        }}
      ]
    }}
    
    REQUIREMENTS:
    1. Exactly 10 questions and 10 one-liners.
    2. Authentic exam Hindi (standard vocabulary used in SSC/UPSC, avoid broken machine translation).
    3. Diverse categories (Defence, National, Appointments, Economy, Science, Sports, Summits).
    4. Output ONLY valid raw JSON.
    """
    
    try:
        result = call_gemini_api(api_key, prompt)
        validate_schema(result)
    except Exception as e:
        print(f'[WARN] Gemini generation failed ({e}), falling back to seed generator...', file=sys.stderr)
        import subprocess
        subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seed_data.py')])
        return
    
    # Save today_gk.json relative to repository root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    data_dir = os.path.join(repo_root, "data")
    os.makedirs(data_dir, exist_ok=True)

    today_path = os.path.join(data_dir, "today_gk.json")
    with open(today_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[SUCCESS] Updated {today_path}")
    
    # Archive dated copy
    archive_dir = os.path.join(data_dir, "archive")
    os.makedirs(archive_dir, exist_ok=True)
    archive_path = os.path.join(archive_dir, f"{today_str}.json")
    with open(archive_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[SUCCESS] Archived to {archive_path}")

if __name__ == "__main__":
    main()
