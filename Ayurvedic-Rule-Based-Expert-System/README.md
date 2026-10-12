markdown
# Ayurvedic Classification as a Rule-Based Expert System

An **Indian Knowledge System (IKS)** project that maps the Ayurvedic
classification of the three Doshas — **Vata**, **Pitta**, and **Kapha** —
to a **Rule-Based Expert System** in Artificial Intelligence.

This project was developed as part of the **IKS in Computational Systems**
course for the Bachelor of Science (Computer Science) programme.

---

## 📌 Project Overview

Ayurveda describes three fundamental Doshas associated with different
physical and behavioural characteristics. This project represents that
classification computationally using:

- A **Knowledge Base** of IF–THEN production rules
- An **Inference Engine** that evaluates rules against user facts
- **Evidence Accumulation** through Dosha scores
- **Conflict Resolution** when two or more Doshas tie

> ⚠️ **Disclaimer:** This is an educational model only. It is **not**
> intended for medical diagnosis or treatment.

---

## 🧠 Conceptual Mapping

| Ayurvedic / IKS Concept | Computer Science Concept | Implementation |
|---|---|---|
| Ayurvedic knowledge | Knowledge Base | Dosha rules in the program |
| Physical/behavioural characteristics | Input Facts | Six user inputs |
| Ayurvedic principles | IF–THEN Production Rules | 18 rules |
| Matching characteristics | Pattern Matching | Rule conditions |
| Application of rules | Inference Engine | `classify_dosha()` |
| Dosha scores | Evidence Accumulation | Score counters |
| Highest score | Decision / Classification | `max()` function |
| Equal highest scores | Conflict Resolution | Mixed classification |
| Explanation of result | Explainable AI | Displays all scores |

---

## 🏗️ System Architecture
User Input
↓
Fact Collection
↓
Knowledge Base
↓
IF–THEN Rule Matching
↓
Inference Engine
↓
Score Calculation
↓
Conflict / Tie Resolution
↓
Final Classification

text

---

## 📥 Input Characteristics

| Characteristic | Vata | Pitta | Kapha |
|---|---|---|---|
| Body Build | lean | medium | large |
| Appetite | irregular | strong | steady |
| Activity Level | high | moderate | low |
| Sleep | light | moderate | deep |
| Temperature Preference | cold | cool | neutral |
| Skin Type | dry | sensitive | oily |

---

## 🚀 How to Run

### Requirements
- Python 3.6 or higher
- No external libraries required

### Steps

```bash
git clone https://github.com/<your-username>/Ayurvedic-Rule-Based-Expert-System.git
cd Ayurvedic-Rule-Based-Expert-System
python src/ayurvedic_expert_system.py
🖥️ Sample Output
text
==============================================
 AYURVEDIC RULE-BASED EXPERT SYSTEM
==============================================
Body build (lean/medium/large): lean
Appetite (irregular/strong/steady): irregular
Activity level (high/moderate/low): high
Sleep (light/moderate/deep): light
Temperature preference (cold/cool/neutral): cold
Skin type (dry/sensitive/oily): dry

--------------- RESULT ---------------
Vata Score  : 6
Pitta Score : 0
Kapha Score : 0
Classification: Vata
--------------------------------------
Educational model only; not a medical
diagnostic or treatment system.
Tie Case Output
text
--------------- RESULT ---------------
Vata Score  : 3
Pitta Score : 3
Kapha Score : 0
Classification: Mixed / Equal Classification
--------------------------------------
🧪 Test Cases
The project was verified using 12 test cases, including pure
classifications, partial matches, and a tie case demonstrating
conflict resolution.

See tests/test_cases.md for the full table.

📊 Complexity
Operation	Complexity
Rule evaluation	O(r) — O(1) for fixed r = 18
Score accumulation	O(r)
Maximum computation	O(d) — O(1) for d = 3
Overall time	O(1) for fixed knowledge base
Overall space	O(1)
⚠️ Limitations
Simplified representation of Ayurveda (only 6 characteristics)

Manually defined rules

Subjective inputs (e.g., "high activity")

Equal weighting — every match counts as 1

No uncertainty handling or probability

No clinical validation

📜 License
This project is licensed under the MIT License — see LICENSE for details.

👤 Author
Student Name: ____________________
PRN: ____________________
Course: B.Sc. Computer Science
Subject: IKS in Computational Systems
Institution: Smt. Devkiba Mohansinhji Chauhan College of Commerce & Science