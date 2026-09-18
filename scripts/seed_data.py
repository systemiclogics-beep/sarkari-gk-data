import os
import json

today_data = {
  "date": "2026-09-18",
  "title_en": "Daily Current Affairs & GK Dose - 18 September 2026",
  "title_hi": "दैनिक करेंट अफेयर्स व सामान्य ज्ञान - 18 सितंबर 2026",
  "total_questions": 10,
  "total_one_liners": 10,
  "questions": [
    {
      "id": "gk_2026_09_18_01",
      "category": "international",
      "exam_tags": ["SSC CGL", "Railway NTPC", "UPSC Prelims"],
      "question_en": "In which country was the 25th meeting of Ministers responsible for Foreign Economic and Trade activities of the Shanghai Cooperation Organisation (SCO) held recently?",
      "question_hi": "शंघाई सहयोग संगठन (SCO) के आर्थिक और विदेश व्यापार मंत्रियों की 25वीं बैठक हाल ही में किस देश में संपन्न हुई?",
      "options_en": ["A) Uzbekistan", "B) Tajikistan", "C) Kazakhstan", "D) Kyrgyzstan"],
      "options_hi": ["A) उज्बेकिस्तान", "B) ताजिकिस्तान", "C) कजाकिस्तान", "D) किर्गिस्तान"],
      "correct_answer": "B",
      "explanation_en": "The 25th meeting of SCO Ministers of Foreign Economic and Trade activities concluded in Dushanbe, Tajikistan. The SCO was established in 2001, and its permanent Secretariat is located in Beijing, China.",
      "explanation_hi": "शंघाई सहयोग संगठन (SCO) के आर्थिक और विदेश व्यापार मंत्रियों की 25वीं बैठक ताजिकिस्तान की राजधानी दुशांबे में संपन्न हुई। SCO की स्थापना 2001 में हुई थी और इसका स्थायी सचिवालय बीजिंग (चीन) में स्थित है।"
    },
    {
      "id": "gk_2026_09_18_02",
      "category": "national",
      "exam_tags": ["SSC CGL", "State PCS", "Banking"],
      "question_en": "Under which newly approved government scheme has an outlay of ₹10,900 crore been sanctioned to promote electric mobility and EV charging infrastructure in India?",
      "question_hi": "भारत में इलेक्ट्रिक मोबिलिटी और ईवी चार्जिंग इंफ्रास्ट्रक्चर को बढ़ावा देने के लिए ₹10,900 करोड़ के परिव्यय के साथ किस नई सरकारी योजना को मंजूरी दी गई है?",
      "options_en": ["A) PM E-DRIVE Scheme", "B) PM-GatiShakti EV", "C) Bharat Mobility Mission", "D) FAME-III Ultra"],
      "options_hi": ["A) पीएम ई-ड्राइव योजना", "B) पीएम-गतिशक्ति ईवी", "C) भारत मोबिलिटी मिशन", "D) फेम-III अल्ट्रा"],
      "correct_answer": "A",
      "explanation_en": "The Union Cabinet approved the PM Electric Drive Revolution in Innovative Vehicle Enhancement (PM E-DRIVE) Scheme with an outlay of ₹10,900 crore over two years to accelerate EV adoption and build fast-charging networks.",
      "explanation_hi": "केंद्रीय मंत्रिमंडल ने दो वर्षों में ₹10,900 करोड़ के वित्तीय परिव्यय के साथ पीएम इलेक्ट्रिक ड्राइव रिवॉल्यूशन इन इनोवेटिव व्हीकल एन्हांसमेंट (पीएम ई-ड्राइव) योजना को मंजूरी दी, जिसका उद्देश्य ईवी अपनाने और फास्ट चार्जिंग नेटवर्क को गति देना है।"
    },
    {
      "id": "gk_2026_09_18_03",
      "category": "defence",
      "exam_tags": ["CDS", "NDA", "Railway NTPC", "SSC"],
      "question_en": "The bilateral joint military exercise 'Surya Kiran' is conducted annually between India and which neighbouring country?",
      "question_hi": "द्विपक्षीय संयुक्त सैन्य अभ्यास 'सूर्य किरण' प्रतिवर्ष भारत और किस पड़ोसी देश के बीच आयोजित किया जाता है?",
      "options_en": ["A) Sri Lanka", "B) Bangladesh", "C) Nepal", "D) Bhutan"],
      "options_hi": ["A) श्रीलंका", "B) बांग्लादेश", "C) नेपाल", "D) भूटान"],
      "correct_answer": "C",
      "explanation_en": "Exercise Surya Kiran is an annual battalion-level joint military counter-terrorism exercise conducted between the Indian Army and the Nepalese Army alternatively in India and Nepal.",
      "explanation_hi": "अभ्यास सूर्य किरण भारतीय सेना और नेपाली सेना के बीच बारी-बारी से भारत और नेपाल में आयोजित होने वाला एक वार्षिक बटालियन-स्तरीय संयुक्त सैन्य आतंकवाद-रोधी अभ्यास है।"
    },
    {
      "id": "gk_2026_09_18_04",
      "category": "science",
      "exam_tags": ["SSC CGL", "UPSC Prelims", "Railway Group D"],
      "question_en": "ISRO launched the EOS-08 Earth Observation Satellite using which indigenous launch vehicle from the Satish Dhawan Space Centre, Sriharikota?",
      "question_hi": "इसरो (ISRO) ने सतीश धवन अंतरिक्ष केंद्र, श्रीहरिकोटा से किस स्वदेशी प्रक्षेपण यान का उपयोग करके पृथ्वी अवलोकन उपग्रह EOS-08 लॉन्च किया?",
      "options_en": ["A) PSLV-C58", "B) SSLV-D3", "C) GSLV-F14", "D) LVM3-M4"],
      "options_hi": ["A) PSLV-C58", "B) SSLV-D3", "C) GSLV-F14", "D) LVM3-M4"],
      "correct_answer": "B",
      "explanation_en": "ISRO successfully conducted the third developmental flight of the Small Satellite Launch Vehicle (SSLV-D3), placing the EOS-08 satellite precisely into a circular low Earth orbit.",
      "explanation_hi": "इसरो ने स्मॉल सैटेलाइट लॉन्च व्हीकल (SSLV-D3) की तीसरी विकासात्मक उड़ान को सफलतापूर्वक पूरा कर EOS-08 उपग्रह को पृथ्वी की निचली कक्षा में सटीक रूप से स्थापित किया।"
    },
    {
      "id": "gk_2026_09_18_05",
      "category": "economy",
      "exam_tags": ["IBPS PO", "SBI Clerk", "SSC CGL"],
      "question_en": "What is the minimum statutory Capital Adequacy Ratio (CAR) that Scheduled Commercial Banks in India are mandated to maintain under RBI Basel-III norms?",
      "question_hi": "आरबीआई (RBI) के बेसल-III मानदंडों के तहत भारत में अनुसूचित वाणिज्यिक बैंकों के लिए न्यूनतम सांविधिक पूंजी पर्याप्तता अनुपात (CAR) कितना अनिवार्य है?",
      "options_en": ["A) 8.0%", "B) 9.0%", "C) 11.5%", "D) 12.0%"],
      "options_hi": ["A) 8.0%", "B) 9.0%", "C) 11.5%", "D) 12.0%"],
      "correct_answer": "B",
      "explanation_en": "Under RBI Basel-III regulations, Scheduled Commercial Banks in India must maintain a minimum CAR of 9.0% (excluding Capital Conservation Buffer of 2.5%, totaling 11.5%).",
      "explanation_hi": "आरबीआई के बेसल-III दिशानिर्देशों के अनुसार, भारत में अनुसूचित वाणिज्यिक बैंकों को न्यूनतम 9.0% पूंजी पर्याप्तता अनुपात (2.5% पूंजी संरक्षण बफर सहित कुल 11.5%) बनाए रखना अनिवार्य है।"
    },
    {
      "id": "gk_2026_09_18_06",
      "category": "environment",
      "exam_tags": ["SSC CGL", "State Police", "UPSC"],
      "question_en": "Which state in India hosts the Kaziranga National Park, recently in the news for its expanded eco-sensitive wildlife corridor?",
      "question_hi": "काजीरंगा राष्ट्रीय उद्यान, जो हाल ही में अपने विस्तारित पर्यावरण-संवेदनशील वन्यजीव गलियारे के लिए चर्चा में रहा, किस भारतीय राज्य में स्थित है?",
      "options_en": ["A) West Bengal", "B) Assam", "C) Arunachal Pradesh", "D) Odisha"],
      "options_hi": ["A) पश्चिम बंगाल", "B) असम", "C) अरुणाचल प्रदेश", "D) ओडिशा"],
      "correct_answer": "B",
      "explanation_en": "Kaziranga National Park is in Assam along the Brahmaputra River, famed for hosting two-thirds of the world's great one-horned rhinoceroses. It is a UNESCO World Heritage Site.",
      "explanation_hi": "काजीरंगा राष्ट्रीय उद्यान असम में ब्रह्मपुत्र नदी के किनारे स्थित है, जो दुनिया के दो-तिहाई एक सींग वाले गैंडों के संरक्षण के लिए प्रसिद्ध है। यह एक यूनेस्को विश्व धरोहर स्थल है।"
    },
    {
      "id": "gk_2026_09_18_07",
      "category": "appointments",
      "exam_tags": ["SSC CGL", "Banking", "Railway NTPC"],
      "question_en": "Who appoints the Comptroller and Auditor General (CAG) of India under Article 148 of the Indian Constitution?",
      "question_hi": "भारतीय संविधान के अनुच्छेद 148 के तहत भारत के नियंत्रक एवं महालेखा परीक्षक (CAG) की नियुक्ति कौन करता है?",
      "options_en": ["A) Prime Minister", "B) Chief Justice of India", "C) President of India", "D) Union Finance Minister"],
      "options_hi": ["A) प्रधानमंत्री", "B) भारत के मुख्य न्यायाधीश", "C) भारत के राष्ट्रपति", "D) केंद्रीय वित्त मंत्री"],
      "correct_answer": "C",
      "explanation_en": "Under Article 148 of the Constitution of India, the CAG is appointed by the President of India by warrant under his hand and seal, and can only be removed in like manner and on like grounds as a Supreme Court Judge.",
      "explanation_hi": "भारतीय संविधान के अनुच्छेद 148 के तहत CAG की नियुक्ति भारत के राष्ट्रपति द्वारा अपने हस्ताक्षर और मुहर वाले वारंट द्वारा की जाती है, और उन्हें केवल सर्वोच्च न्यायालय के न्यायाधीश के समान ही हटाया जा सकता है।"
    },
    {
      "id": "gk_2026_09_18_08",
      "category": "sports",
      "exam_tags": ["Railway NTPC", "SSC CHSL", "State Exams"],
      "question_en": "The prestigious Thomas Cup and Uber Cup competitions are associated with which sport?",
      "question_hi": "प्रतिष्ठित थॉमस कप और उबेर कप प्रतियोगिताएं किस खेल से संबंधित हैं?",
      "options_en": ["A) Badminton", "B) Table Tennis", "C) Lawn Tennis", "D) Squash"],
      "options_hi": ["A) बैडमिंटन", "B) टेबल टेनिस", "C) लॉन टेनिस", "D) स्क्वैश"],
      "correct_answer": "A",
      "explanation_en": "Thomas Cup (Men's World Team Championship) and Uber Cup (Women's World Team Championship) are premier international badminton tournaments conducted by the Badminton World Federation (BWF). India won the historic Thomas Cup title in 2022.",
      "explanation_hi": "थॉमस कप (पुरुष विश्व टीम चैम्पियनशिप) और उबेर कप (महिला विश्व टीम चैम्पियनशिप) बीडब्ल्यूएफ (BWF) द्वारा आयोजित प्रमुख अंतरराष्ट्रीय बैडमिंटन टूर्नामेंट हैं। भारत ने वर्ष 2022 में ऐतिहासिक थॉमस कप का खिताब जीता था।"
    },
    {
      "id": "gk_2026_09_18_09",
      "category": "national",
      "exam_tags": ["SSC CGL", "State PCS", "Teaching Exams"],
      "question_en": "Which constitutional amendment introduced the Goods and Services Tax (GST) in India under Article 246A?",
      "question_hi": "किस संविधान संशोधन अधिनियम द्वारा भारतीय संविधान के अनुच्छेद 246A के तहत वस्तु एवं सेवा कर (GST) लागू किया गया?",
      "options_en": ["A) 99th Constitutional Amendment", "B) 100th Constitutional Amendment", "C) 101st Constitutional Amendment", "D) 103rd Constitutional Amendment"],
      "options_hi": ["A) 99वां संविधान संशोधन", "B) 100वां संविधान संशोधन", "C) 101वां संविधान संशोधन", "D) 103वां संविधान संशोधन"],
      "correct_answer": "C",
      "explanation_en": "The 101st Constitutional Amendment Act, 2016 introduced GST in India with effect from 1st July 2017, inserting Article 246A conferring concurrent powers to Parliament and State Legislatures.",
      "explanation_hi": "101वें संविधान संशोधन अधिनियम, 2016 द्वारा 1 जुलाई 2017 से भारत में जीएसटी लागू किया गया, जिसमें संसद और राज्य विधानसभाओं को समवर्ती अधिकार देने वाला अनुच्छेद 246A शामिल किया गया।"
    },
    {
      "id": "gk_2026_09_18_10",
      "category": "science",
      "exam_tags": ["SSC CGL", "Railway Group D", "CDS"],
      "question_en": "Which noble gas is commonly used in high-intensity discharge lamps and airport runway lighting due to its brilliant reddish-orange glow?",
      "question_hi": "कौन सी अक्रिय (नोबल) गैस अपनी चमकदार लाल-नारंगी चमक के कारण हवाई अड्डे के रनवे और डिस्चार्ज लैंप में व्यापक रूप से उपयोग की जाती है?",
      "options_en": ["A) Argon", "B) Neon", "C) Krypton", "D) Xenon"],
      "options_hi": ["A) ऑर्गन", "B) नियॉन", "C) क्रिप्टन", "D) जीनॉन"],
      "correct_answer": "B",
      "explanation_en": "Neon (atomic number 10) emits a distinctive reddish-orange light when electrified in gas-discharge tubes, making it ideal for high-visibility airport runway beacon lighting and signage.",
      "explanation_hi": "नियॉन (परमाणु संख्या 10) गैस-डिस्चार्ज ट्यूबों में विद्युतीकृत होने पर एक विशिष्ट लाल-नारंगी प्रकाश उत्सर्जित करता है, जो इसे हवाई अड्डे के रनवे बीकन और चेतावनी संकेतों के लिए उपयुक्त बनाता है।"
    }
  ],
  "one_liners": [
    {
      "id": "nl_2026_09_18_01",
      "category": "national",
      "note_en": "PM E-DRIVE scheme approved with ₹10,900 crore allocation over two years to supercharge EV manufacturing and public charging infrastructure.",
      "note_hi": "ईवी विनिर्माण और सार्वजनिक चार्जिंग बुनियादी ढांचे को गति देने के लिए दो वर्षों में ₹10,900 करोड़ के आवंटन के साथ पीएम ई-ड्राइव योजना को मंजूरी दी गई।"
    },
    {
      "id": "nl_2026_09_18_02",
      "category": "international",
      "note_en": "SCO Ministers of Foreign Economic and Trade activities 25th summit held in Dushanbe, Tajikistan to boost multilateral trade corridor integration.",
      "note_hi": "बहुपक्षीय व्यापार गलियारा एकीकरण को बढ़ावा देने के लिए ताजिकिस्तान के दुशांबे में SCO विदेश व्यापार मंत्रियों का 25वां शिखर सम्मेलन आयोजित किया गया।"
    },
    {
      "id": "nl_2026_09_18_03",
      "category": "defence",
      "note_en": "Indian Navy commissions newly constructed stealth guided missile frigate into the Western Fleet in Mumbai.",
      "note_hi": "भारतीय नौसेना ने मुंबई में पश्चिमी बेड़े में नव निर्मित स्टील्थ निर्देशित मिसाइल फ्रिगेट को कमीशन किया।"
    },
    {
      "id": "nl_2026_09_18_04",
      "category": "science",
      "note_en": "ISRO successfully validated SSLV third developmental flight placing Earth Observation Satellite EOS-08 into designated orbit.",
      "note_hi": "इसरो ने एसएसएलवी की तीसरी विकासात्मक उड़ान को सफलतापूर्वक पूरा कर अर्थ ऑब्जर्वेशन सैटेलाइट ईओएस-08 को लक्षित कक्षा में स्थापित किया।"
    },
    {
      "id": "nl_2026_09_18_05",
      "category": "economy",
      "note_en": "RBI retains Repo Rate at 6.50% in Monetary Policy Committee (MPC) review, projecting FY27 GDP growth at 7.2%.",
      "note_hi": "आरबीआई ने मौद्रिक नीति समिति (एमपीसी) समीक्षा में रेपो दर को 6.50% पर अपरिवर्तित रखा तथा जीडीपी वृद्धि 7.2% रहने का अनुमान लगाया।"
    },
    {
      "id": "nl_2026_09_18_06",
      "category": "appointments",
      "note_en": "Appointments Committee of the Cabinet (ACC) approves senior administrative appointments across key economic ministries.",
      "note_hi": "मंत्रिमंडल की नियुक्ति समिति (एसीसी) ने प्रमुख आर्थिक मंत्रालयों में वरिष्ठ प्रशासनिक नियुक्तियों को मंजूरी दी।"
    },
    {
      "id": "nl_2026_09_18_07",
      "category": "sports",
      "note_en": "Indian contingent bags record medal tally at the Asian Youth Athletics Championships, clinching multiple gold medals.",
      "note_hi": "एशियाई युवा एथलेटिक्स चैंपियनशिप में भारतीय दल ने कई स्वर्ण पदक जीतकर रिकॉर्ड पदक तालिका दर्ज की।"
    },
    {
      "id": "nl_2026_09_18_08",
      "category": "environment",
      "note_en": "Ministry of Environment notifies expanded buffer boundaries for Project Tiger reserves to protect natural wildlife corridors.",
      "note_hi": "पर्यावरण मंत्रालय ने प्राकृतिक वन्यजीव गलियारों की सुरक्षा के लिए प्रोजेक्ट टाइगर रिजर्व के लिए विस्तारित बफर सीमाओं को अधिसूचित किया।"
    },
    {
      "id": "nl_2026_09_18_09",
      "category": "national",
      "note_en": "Cabinet approves Mission Mausam with ₹2,000 crore outlay to dramatically upgrade India's weather forecasting radar and satellite resolution.",
      "note_hi": "मौसम पूर्वानुमान रडार और उपग्रह सटीकता को बेहतर बनाने के लिए ₹2,000 करोड़ के परिव्यय के साथ कैबिनेट ने 'मिशन मौसम' को मंजूरी दी।"
    },
    {
      "id": "nl_2026_09_18_10",
      "category": "science",
      "note_en": "CSIR develops indigenous low-cost bio-fertilizer technology to reduce agricultural chemical dependency in arid soils.",
      "note_hi": "सीएसआईआर ने शुष्क मिट्टी में कृषि रसायनों पर निर्भरता कम करने के लिए स्वदेशी कम लागत वाली जैव-उर्वरक तकनीक विकसित की।"
    }
  ]
}

os.makedirs('sarkari_gk_backend/data/archive', exist_ok=True)
with open('sarkari_gk_backend/data/today_gk.json', 'w', encoding='utf-8') as f:
    json.dump(today_data, f, ensure_ascii=False, indent=2)

with open('sarkari_gk_backend/data/archive/2026-09-18.json', 'w', encoding='utf-8') as f:
    json.dump(today_data, f, ensure_ascii=False, indent=2)

print('SUCCESS')
