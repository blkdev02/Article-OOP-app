import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import datetime

now = datetime.datetime.now()
date_format = now.strftime("%d-%m-%Y-%H-%M-%S")


def create_receipt(receipt_number, article_name, article_price):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    
    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=50, h=12, txt=f"Receipt No.{receipt_number}", ln=1)

    #  Add the date
    pdf.set_font(family="Times", style="B", size=20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=50, h=12, txt=f"Date: {date_format}", ln=1)

    # Add the article name 
    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=50, h=12, txt=f"Article: {article_name}", ln=1)

    # Add the price
    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=50, h=12, txt=f"Price: {article_price}", ln=1)

    # Add the quantity bought
    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=50, h=12, txt=f"Quantity: 1", ln=1)

    # output the pdf files to disk
    pdf.output(f"receipt-{receipt_number}.pdf")



