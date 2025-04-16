from docling.document_converter import DocumentConverter
import llm

_PREFIX = "doc"


@llm.hookimpl
def register_fragment_loaders(register):
    register(_PREFIX, doc_loader)


def doc_loader(argument: str) -> llm.Fragment:
    content = DocumentConverter().convert(argument).document.export_to_markdown()
    return llm.Fragment(content=content, source=f"{_PREFIX}:{argument}")
