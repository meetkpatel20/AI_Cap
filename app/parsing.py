from bs4 import BeautifulSoup


def parse_response(response):
    soup = BeautifulSoup(response, "html.parser")
    text_elements = soup.find_all(string=True)
    extracted_text = [element.strip() for element in text_elements if element.strip()]
    return extracted_text
