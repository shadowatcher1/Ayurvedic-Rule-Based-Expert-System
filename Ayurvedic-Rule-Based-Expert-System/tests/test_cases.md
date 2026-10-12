# Test Cases — Ayurvedic Rule-Based Expert System

Total test cases: **12**

---

## Test Case Table

| TC | Body Build | Appetite | Activity | Sleep | Temperature | Skin | Expected Output | Status |
|----|-----------|----------|----------|-------|-------------|------|-----------------|--------|
| TC01 | lean | irregular | high | light | cold | dry | Vata | Pass |
| TC02 | medium | strong | moderate | moderate | cool | sensitive | Pitta | Pass |
| TC03 | large | steady | low | deep | neutral | oily | Kapha | Pass |
| TC04 | lean | irregular | high | moderate | cold | sensitive | Vata | Pass |
| TC05 | medium | strong | moderate | light | cool | sensitive | Pitta | Pass |
| TC06 | large | steady | low | deep | neutral | dry | Kapha | Pass |
| TC07 | lean | strong | high | light | cold | dry | Vata | Pass |
| TC08 | medium | irregular | moderate | moderate | cool | sensitive | Pitta | Pass |
| TC09 | large | steady | low | moderate | neutral | oily | Kapha | Pass |
| TC10 | lean | irregular | moderate | light | cold | dry | Vata | Pass |
| TC11 | lean | strong | high | moderate | cold | sensitive | Mixed / Equal | Pass |
| TC12 | medium | strong | moderate | moderate | cool | oily | Pitta | Pass |

---

## Detailed Test Results

### TC01
Input: lean, irregular, high, light, cold, dry  
Scores: Vata = 6, Pitta = 0, Kapha = 0  
Result: **Vata** ✅

### TC02
Input: medium, strong, moderate, moderate, cool, sensitive  
Scores: Vata = 0, Pitta = 6, Kapha = 0  
Result: **Pitta** ✅

### TC03
Input: large, steady, low, deep, neutral, oily  
Scores: Vata = 0, Pitta = 0, Kapha = 6  
Result: **Kapha** ✅

### TC04
Input: lean, irregular, high, moderate, cold, sensitive  
Scores: Vata = 4, Pitta = 2, Kapha = 0  
Result: **Vata** ✅

### TC05
Input: medium, strong, moderate, light, cool, sensitive  
Scores: Vata = 1, Pitta = 5, Kapha = 0  
Result: **Pitta** ✅

### TC06
Input: large, steady, low, deep, neutral, dry  
Scores: Vata = 1, Pitta = 0, Kapha = 5  
Result: **Kapha** ✅

### TC07
Input: lean, strong, high, light, cold, dry  
Scores: Vata = 5, Pitta = 1, Kapha = 0  
Result: **Vata** ✅

### TC08
Input: medium, irregular, moderate, moderate, cool, sensitive  
Scores: Vata = 1, Pitta = 5, Kapha = 0  
Result: **Pitta** ✅

### TC09
Input: large, steady, low, moderate, neutral, oily  
Scores: Vata = 0, Pitta = 1, Kapha = 5  
Result: **Kapha** ✅

### TC10
Input: lean, irregular, moderate, light, cold, dry  
Scores: Vata = 5, Pitta = 1, Kapha = 0  
Result: **Vata** ✅

### TC11 — Tie Case ⭐
Input: lean, strong, high, moderate, cold, sensitive  
Scores: Vata = 3, Pitta = 3, Kapha = 0  
Result: **Mixed / Equal Classification** ✅

### TC12 — Partial Match
Input: medium, strong, moderate, moderate, cool, oily  
Scores: Vata = 0, Pitta = 5, Kapha = 1  
Result: **Pitta** ✅

---

## Invariant

For every valid input:
Score(Vata) + Score(Pitta) + Score(Kapha) = 6

text

Verified on all 12 test cases.