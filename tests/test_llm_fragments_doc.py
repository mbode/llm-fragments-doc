from fpdf import FPDF
from llm_fragments_doc import doc_loader


def test_fragment_is_loaded_from_pdf(tmp_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=10)
    content = "Hello world!"
    pdf.cell(text=content)

    file = tmp_path / "test.pdf"
    pdf.output(file)
    fragment = doc_loader(argument=file)
    assert str(fragment) == content
    assert fragment.source == f"doc:{file}"
