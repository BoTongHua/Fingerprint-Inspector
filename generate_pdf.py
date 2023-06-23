import jinja2
import pdfkit


def generate(data):
    """
    A method to generate pdf file based on specific dictionary data.

    example data: {
        "_id": 1,
        "name": "Kirby Siedler",
        "age": 25,
        "residence": "street 1",
        "characteristics": "arrogant, stubborn and conceited.",
        "fingerprint": "1__M_Right_thumb_finger.BMP"
        }
    """
    template_loader = jinja2.FileSystemLoader('./pdf_template/')
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template("template.html")
    output_text = template.render(data)

    config = pdfkit.configuration(
        wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_string(
        output_text, data['name'] + '_suspect.pdf', configuration=config)
