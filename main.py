from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
for i in range(1, 51):
    calculate1 = i * 1
    calculate2 = i * 2
    calculate3 = i * 3
    calculate4 = i * 4
    calculate5 = i * 5
    dummy1 = '1 X ' + str(i) + ' = ' + str(calculate1)
    pdf.cell(40, 5, dummy1, ln=0, border=0, align='L')
    dummy2 = '2 X ' + str(i) + ' = ' + str(calculate2)
    pdf.cell(40, 5, dummy2, ln=0, border=0, align='L')
    dummy3 = '3 X ' + str(i) + ' = ' + str(calculate3)
    pdf.cell(40, 5, dummy3, ln=0, border=0, align='L')
    dummy4 = '4 X ' + str(i) + ' = ' + str(calculate4)
    pdf.cell(40, 5, dummy4, ln=0, border=0, align='L')
    dummy5 = '5 X ' + str(i) + ' = ' + str(calculate5)
    pdf.cell(40, 5, dummy5, ln=1, border=0, align='L')
pdf.output('tutorial_1_5.pdf', 'F')