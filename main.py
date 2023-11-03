from datetime import date

from fpdf import FPDF
from fpdf.fonts import FontFace

from get_data import get_data

class PDF(FPDF):
    def header(self):
        self.set_font("Roboto", "", 10)

        self.ln(20)
        self.cell(80)
        self.cell(30, 10, "Справка", align="C")
        
        self.ln(7)
        self.cell(80)
        self.cell(30, 10, "о принятии статьи к публикации", align="C")

        self.ln(15)

        
    def chapter_body(self, data):
        pdf.set_font("Roboto", "B", size=10)
        with pdf.table(width=150, headings_style=headings_style) as table:
            for data_row in data:
                row = table.row()
                for datum in data_row:
                    row.cell(datum, align="C", padding=(0, 0, 5, 0))
        self.ln(10)
    
    def chapter_footer(self):
        pdf.set_font("Roboto", "", size=9)

        self.cell(19)
        self.cell(30, 10, "Дата:", align="L")
        self.ln(5)
        self.cell(19)
        self.cell(30, 10, f"{date.today().strftime('%d.%m.%Y')} г.")
        self.ln(10)

        d = [["Представитель Научно-издательской платформы «Из уст»", "\n\n____________________________/Зарипов Ш.Р."]]
        with pdf.table(width=150, headings_style=headings_style) as table:
            for data_row in d:
                row = table.row()
                for datum in data_row:
                    row.cell(datum, align="l")
        self.ln(10)


pdf = PDF()
pdf.set_page_background("background.png")
pdf.add_font("Roboto", style="", fname="./fonts/Roboto-Medium.ttf")
pdf.add_font("Roboto", style="B", fname="./fonts/Roboto-Bold.ttf")
headings_style = FontFace()

pdf.add_page()

data = get_data('input.json')
pdf.chapter_body(data)

pdf.chapter_footer()

pdf.output("./outputs/output.pdf")