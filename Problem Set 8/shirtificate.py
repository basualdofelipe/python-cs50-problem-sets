from fpdf import FPDF, Align

class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 50)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(None, 50, "CS50 Shirtificate", center=True)
        # Performing a line break:
        self.ln(20)


def main():
    shirtificate(input("Name: "))

def shirtificate(text):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("img/shirtificate.png", Align.C, 75, 175, 175)
    pdf.set_font("helvetica", "", 25)
    pdf.set_text_color(255,255,255)
    pdf.cell(None, 200, f"{text} took CS50", center=True)

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()