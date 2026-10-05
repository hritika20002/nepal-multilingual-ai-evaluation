import pandas as pd

file_path = "data/evaluation_template.csv"

df = pd.read_csv(file_path)

text_cols = [
    "ai_response",
    "hallucination",
    "error_category",
    "evaluator_notes"
]

for col in text_cols:
    df[col] = df[col].astype("object")


# =========================================================
# ROW 6 — Nepali summarization
# =========================================================

mask = df["id"] == 6

df.loc[mask, "ai_response"] = (
    "पर्यटनले विदेशी मुद्रा आर्जन गर्न, रोजगारी सिर्जना गर्न र होटल, "
    "यातायात, हस्तकला तथा स्थानीय व्यवसायलाई सहयोग गर्ने भएकाले नेपालको "
    "अर्थतन्त्रमा महत्त्वपूर्ण भूमिका खेल्छ। यसले पर्यटकीय क्षेत्रका स्थानीय "
    "समुदायको आम्दानी बढाउन र आर्थिक गतिविधि विस्तार गर्न पनि सहयोग गर्छ।"
)

df.loc[mask, "instruction_adherence"] = 5
df.loc[mask, "factual_consistency"] = 5
df.loc[mask, "language_quality"] = 5
df.loc[mask, "contextual_appropriateness"] = 5
df.loc[mask, "completeness"] = 5
df.loc[mask, "hallucination"] = "No"
df.loc[mask, "overall_quality"] = 5
df.loc[mask, "error_category"] = "none"
df.loc[mask, "evaluator_notes"] = (
    "Clear two-sentence Nepali summary covering employment, foreign currency, "
    "local businesses, and economic activity."
)


# =========================================================
# ROW 7 — Nepali instruction following
# Intentionally imperfect: gives four points instead of three
# =========================================================

mask = df["id"] == 7

df.loc[mask, "ai_response"] = (
    "- आवश्यक मात्रामा खाना किन्ने।\n"
    "- बाँकी खाना फ्रिजमा सुरक्षित राख्ने।\n"
    "- बाँकी खानालाई अर्को परिकारमा प्रयोग गर्ने।\n"
    "- आवश्यक नभएको खाना साथीहरूसँग बाँड्ने।"
)

df.loc[mask, "instruction_adherence"] = 3
df.loc[mask, "factual_consistency"] = 5
df.loc[mask, "language_quality"] = 5
df.loc[mask, "contextual_appropriateness"] = 5
df.loc[mask, "completeness"] = 4
df.loc[mask, "hallucination"] = "No"
df.loc[mask, "overall_quality"] = 4
df.loc[mask, "error_category"] = "instruction_failure"
df.loc[mask, "evaluator_notes"] = (
    "Suggestions are practical and clearly written, but the response gives "
    "four bullet points instead of the requested exactly three."
)


# =========================================================
# ROW 8 — Nepali to English translation
# =========================================================

mask = df["id"] == 8

df.loc[mask, "ai_response"] = (
    "The meeting has been postponed until next Monday."
)

df.loc[mask, "instruction_adherence"] = 5
df.loc[mask, "factual_consistency"] = 5
df.loc[mask, "language_quality"] = 5
df.loc[mask, "contextual_appropriateness"] = 5
df.loc[mask, "completeness"] = 5
df.loc[mask, "hallucination"] = "No"
df.loc[mask, "overall_quality"] = 5
df.loc[mask, "error_category"] = "none"
df.loc[mask, "evaluator_notes"] = (
    "Accurate and natural English translation preserving the original meaning."
)


# =========================================================
# ROW 9 — Nepali factual consistency
# =========================================================

mask = df["id"] == 9

df.loc[mask, "ai_response"] = (
    "मौसम भनेको कुनै स्थानमा छोटो समयका लागि देखिने तापक्रम, वर्षा, हावा "
    "जस्ता वायुमण्डलीय अवस्था हुन्। जलवायु भनेको त्यही क्षेत्रको लामो "
    "समयसम्म देखिने सामान्य मौसम ढाँचा हो।"
)

df.loc[mask, "instruction_adherence"] = 5
df.loc[mask, "factual_consistency"] = 5
df.loc[mask, "language_quality"] = 5
df.loc[mask, "contextual_appropriateness"] = 5
df.loc[mask, "completeness"] = 5
df.loc[mask, "hallucination"] = "No"
df.loc[mask, "overall_quality"] = 5
df.loc[mask, "error_category"] = "none"
df.loc[mask, "evaluator_notes"] = (
    "Accurately distinguishes short-term weather from long-term climate "
    "using concise and understandable Nepali."
)


# =========================================================
# ROW 10 — Nepali contextual reasoning
# Intentionally weaker: useful but incomplete
# =========================================================

mask = df["id"] == 10

df.loc[mask, "ai_response"] = (
    "1. छाता वा रेनकोट साथमा राख्नुहोस्।\n"
    "2. पानी नछिर्ने जुत्ता लगाउनुहोस्।\n"
    "3. मोबाइल र कागजातलाई सुरक्षित झोलामा राख्नुहोस्।"
)

df.loc[mask, "instruction_adherence"] = 3
df.loc[mask, "factual_consistency"] = 5
df.loc[mask, "language_quality"] = 5
df.loc[mask, "contextual_appropriateness"] = 5
df.loc[mask, "completeness"] = 3
df.loc[mask, "hallucination"] = "No"
df.loc[mask, "overall_quality"] = 4
df.loc[mask, "error_category"] = "incomplete_answer"
df.loc[mask, "evaluator_notes"] = (
    "The recommendations are relevant to monsoon travel, but only three "
    "preparation tips are provided when the prompt explicitly requests four."
)


# Save
df.to_csv(file_path, index=False, encoding="utf-8-sig")

print("Rows 6-10 completed and evaluated successfully.")