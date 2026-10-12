# Conceptual Mapping: Ayurveda → Rule-Based Expert System

## Overview

This document maps the Indian Knowledge System (IKS) concept of
Ayurvedic Dosha classification to Computer Science concepts in
Artificial Intelligence and Expert Systems.

---

## Mapping Table

| Ayurvedic / IKS Concept | Computer Science Concept | Implementation |
|---|---|---|
| Ayurvedic knowledge | Knowledge Base | Dosha rules stored in the program |
| Physical / behavioural characteristics | Input Facts | Six user-provided characteristics |
| Vata, Pitta, Kapha characteristics | Classification Rules | Three rule groups |
| Ayurvedic principles | IF–THEN Production Rules | 18 rules total |
| Matching characteristics with rules | Pattern Matching | Comparing inputs to rule conditions |
| Application of rules | Inference Engine | `classify_dosha()` function |
| Dosha scores | Evidence Accumulation | Incrementing counters |
| Highest score | Decision / Classification | `max()` over score dictionary |
| Equal highest scores | Conflict Resolution | Multiple winners → Mixed |
| Explanation of classification | Explainable AI | Displays all three scores |

---

## System Architecture
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

## Knowledge Base Summary

| Dosha | Matching Values | Max Score |
|---|---|---|
| Vata | lean, irregular, high, light, cold, dry | 6 |
| Pitta | medium, strong, moderate, moderate, cool, sensitive | 6 |
| Kapha | large, steady, low, deep, neutral, oily | 6 |

---

## Formal Specification

Let the input fact tuple be:
F = (b, a, c, s, t, k)

text

Score for each Dosha:
Score(D) = Sum of R_i(F)

text

Final classification:
Class = argmax_D Score(D) if unique
Class = "Mixed / Equal" otherwise

text