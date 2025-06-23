from datetime import datetime
from fpdf import FPDF
import os


class User:
    def __init__(self, name, email, education, experience, skills):
        self.name = name
        self.email = email
        self.education = education
        self.experience = experience
        self.skills = skills
        self.created_at = datetime.now().strftime('%Y-%m-%d')

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Document:
    def __init__(self, user):
        self.user = user

    def save_to_txt(self, content, filename):
        with open(f"output/{filename}", "w", encoding="utf-8") as f:
            f.write(content)

    def save_to_pdf(self, content, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('EBGaramond','','fonts/EBGaramond-Italic-VariableFont_wght.ttf',uni=True)
        pdf.set_font("EBGaramond", size=12)
        for line in content.split("\n"):
            pdf.multi_cell(0,10,line)
        pdf.output(f"output/{filename}")


class CV(Document):
    def __init__(self, user):
        super().__init__(user)

    def generate_cv(self):
        content = f"""
        CV
        Imię i nazwisko: {self.user.name}
        Email: {self.user.email}
        Wykształcenie: {self.user.education}
        Doświadczenie: {self.user.experience}
        Umiejętności: {', '.join(self.user.skills)}
        """
        self.save_to_txt(content, f"cv_{self.user.email}.txt")
        self.save_to_pdf(content, f"cv_{self.user.email}.pdf")


class CoverLetter(Document):
    def __init__(self, user, company, position):
        super().__init__(user)
        self.company = company
        self.position = position

    def generate_cover_letter(self):
        content = f"""
        List motywacyjny
        Szanowni Państwo,
        Zwracam się z uprzejmą prośbą o rozważenie mojej kandydatury na stanowisko {self.position} w firmie {self.company}.
        Imię i nazwisko: {self.user.name}
        Email: {self.user.email}
        Wykształcenie: {self.user.education}
        Doświadczenie: {self.user.experience}
        Umiejętności: {', '.join(self.user.skills)}
        Z poważaniem,
        {self.user.name}
        """
        self.save_to_txt(content, f"cover_letter_{self.user.email}.txt")
        self.save_to_pdf(content, f"cover_letter_{self.user.email}.pdf")