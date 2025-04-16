# llm-fragments-doc

Load documents as fragments. Uses [docling](https://github.com/docling-project/docling) for parsing.

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```shell
llm install llm-fragments-doc
```
## Usage

Use `-f doc:/path/to/my/file.pdf` to include a markdown-converted version of your file as a fragment.

```shell
llm -f doc:https://pdfobject.com/pdf/sample.pdf 'What kind of document is this?'
```

## Development

### Local Setup

To set up this plugin locally, first checkout the code, then install:
```shell
cd llm-fragments-doc
uv run llm install -e .
```

### Linting & formatting via pre-commit

Install:

```shell
uv run pre-commit install
```

### Tests

Run tests:
```shell
uv run pytest
```
