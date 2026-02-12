EXTRACTION_PROMPT = """
You are an AI extraction engine.

Extract structured observations from the following text.

Return ONLY JSON list format:

[
 { "area": "", "issue": "", "source": "", "evidence": "" }
]

Rules:
- Do NOT invent facts
- Use only provided content
- Keep language simple
"""

DDR_PROMPT = """
Generate a Detailed Diagnostic Report.

STRICT STRUCTURE:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

Rules:
- Do NOT invent facts
- Mention conflicts if present
- If data missing → write Not Available
- Client-friendly language only
"""
