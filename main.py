from pdf_loader import load_pdf
from extractor import extract_observations
from merger import merge_observations
from generator import generate_ddr

# Load documents
inspection_text = load_pdf("Sample Report.pdf")
thermal_text = load_pdf("Thermal Images.pdf")

print("Extracting inspection observations...")
inspection_obs = extract_observations(inspection_text, "inspection")

print("Extracting thermal observations...")
thermal_obs = extract_observations(thermal_text, "thermal")

print("Merging data...")
merged_obs = merge_observations(inspection_obs, thermal_obs)

print("Generating DDR...")
ddr_report = generate_ddr(merged_obs)

# Save output
with open("output/DDR_Report.txt", "w", encoding="utf-8") as f:
    f.write(ddr_report)

print("✅ DDR Report Generated Successfully")
