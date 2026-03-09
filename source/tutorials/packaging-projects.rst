# coding: utf-8
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('DejaVu', 'B', 10)
        self.cell(0, 10, 'История письменности: от пиктограмм до букв', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', 'I', 8)
        self.cell(0, 10, f'Страница {self.page_no()}', 0, 0, 'C')

def create_presentation():
    pdf = PDF()

    # Register font with Cyrillic support
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)

    # Slide 1: Title
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 24)
    pdf.ln(40)
    pdf.cell(0, 20, 'ИСТОРИЯ ПИСЬМЕННОСТИ', 0, 1, 'C')
    pdf.set_font('DejaVu', '', 16)
    pdf.cell(0, 15, 'от пиктограмм до алфавита', 0, 1, 'C')

    # Slide 2: What is pictogram
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 18)
    pdf.cell(0, 15, 'Что такое пиктограмма?', 0, 1, 'L')
    pdf.set_font('DejaVu', '', 12)
    pdf.ln(10)
    text = """Пиктограмма или пиктография - это передача образов,
впечатлений, событий, мыслей с помощью рисунка.

К ней относятся древние наскальные рисунки.

Пиктография была предвестницей письменности!"""
    pdf.multi_cell(0, 8, text)

    # Slide 3: Petroglyphs of Tamgaly
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 18)
    pdf.cell(0, 15, 'Петроглифы Тамгалы', 0, 1, 'L')
    pdf.set_font('DejaVu', '', 12)
    pdf.ln(10)
    text2 = """На территории Казахстана находится один из
наиболее древних памятников искусства Семиречья -
петроглифы Тамгалы.

Здесь в конце 1950-х годов было обнаружено
множество наскальных рисунков.

Общее количество рисунков в ущелье - 2000."""
    pdf.multi_cell(0, 8, text2)

    # Slide 4: Differences
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 18)
    pdf.cell(0, 15, 'Пиктограммы и петроглифы', 0, 1, 'L')
    pdf.set_font('DejaVu', '', 12)
    pdf.ln(10)
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 10, 'Сходство:', 0, 1, 'L')
    pdf.set_font('DejaVu', '', 12)
    pdf.cell(0, 8, '- оба вида используют рисунки', 0, 1, 'L')
    pdf.ln(5)
    pdf.set_font('DejaVu', 'B', 14)
    pdf.cell(0, 10, 'Различия:', 0, 1, 'L')
    pdf.set_font('DejaVu', '', 12)
    pdf.cell(0, 8, '- пиктограмма - только рисунки', 0, 1, 'L')
    pdf.cell(0, 8, '- петроглифы - рисунки и другие символы', 0, 1, 'L')

    # Slide 5: Ancient writing materials
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 18)
    pdf.cell(0, 15, 'Материалы для письма', 0, 1, 'L')
    pdf.set_font('DejaVu', '', 12)
    pdf.ln(10)
    text3 = """Древние люди писали на:

• Камнях (скалах)
• Глиняных дощечках
• Березовой коре
• Выделанной коже"""
    pdf.multi_cell(0, 8, text3)

    # Slide 6: Conclusion
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 18)
    pdf.cell(0, 15, 'Вывод', 0, 1, 'L')
    pdf.set_font('DejaVu', '', 12)
    pdf.ln(10)
    conclusion = """Рисунки были одним из способов
передачи ИНФОРМАЦИИ.

Слово "информация" на разных языках:

• Казахский: Ақпарат
• Английский: Information"""
    pdf.multi_cell(0, 8, conclusion)

    # Save PDF
    pdf.output('prezentaciya_istoriya_pismennosti.pdf')
    print("PDF создан успешно!")

if __name__ == '__main__':
    create_presentation()
