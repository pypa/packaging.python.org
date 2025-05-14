from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "SBI Safe Use Guide & Schemes (Uttarakhand)", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Section: Checklist
pdf.chapter_title("Safe Use Checklist:")
pdf.chapter_body("""1. Check account type (Regular / Jan Dhan / Salary / Pension) - different balance rules and benefits.
2. Check debit card charges - deactivate if not in use.
3. SMS alert fee: ₹15/quarter - keep only basic alerts.
4. Turn off International Usage unless needed.
5. Review Auto Debit / ECS Mandates - remove inactive ones.
6. Avoid Dormant status - make at least 1 transaction per year.""")

# Section: Services to Deactivate
pdf.chapter_title("Services to Deactivate:")
pdf.chapter_body("""- Unused insurance plans
- Extra ATM cards
- Old ECS/NACH mandates not in use
- Services activated without consent (like accidental cover)""")

# Section: SBI Schemes
pdf.chapter_title("Recommended SBI Schemes:")
pdf.chapter_body("""1. SBI Amrit Kalash FD - 400 days, ~7.10% interest
2. SBI Sarvottam Term Deposit - floating rate
3. SBI Annuity Deposit Scheme - monthly income like pension
4. SBI Tax Saver FD - 5 year lock-in, ₹1.5 lakh 80C tax benefit
5. SBI Recurring Deposit - monthly savings
6. SBI Floating Rate Bonds - 7.15% interest
7. SBI Mutual Funds - low to medium risk investment options""")

# Section: Uttarakhand Tips
pdf.chapter_title("Uttarakhand Specific Tips:")
pdf.chapter_body("""- Ask your branch about PM schemes (PM Kisan, PMJJBY, Ayushman)
- Use SBI Mitra or CSP agents for local services in villages
- Use YONO or Net Banking to manage services yourself""")

# Save PDF
pdf.output("sbi_safe_use_guide.pdf")
