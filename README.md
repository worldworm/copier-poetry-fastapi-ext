<h1 align="center">📋 copier-poetry-fastapi-ext</h1>
<p align="center">
  <i><a href="https://github.com/copier-org/copier">Copier</a> extension template for <a href="https://github.com/tiangolo/fastapi">fastapi</a> projects.</i>
</p>


<!-- Place https://shields.io/ badges here -->


## Features
- Basic [fastapi](https://github.com/tiangolo/fastapi) setup
- API versioning using [fastapi-versionizer](https://github.com/alexschimpf/fastapi-versionizer)
- Pre-defined HTTP status code error models

## Requirements
First install copier:<br>
([from the official installation documentation](https://copier.readthedocs.io/en/stable/#installation))
```bash
pip install copier
```


## Usage

> [!NOTE]
> This is an [extension template](https://github.com/worldworm/copier-showcase/blob/main/types/extension.md) that cannot be used directly to create a project.
> Use this template after applying the appropriate meta template: [copier-poetry-meta](https://github.com/worldworm/copier-poetry-meta)


Make sure the requirements are met, then:
```bash
copier copy "https://github.com/worldworm/copier-poetry-fastapi-ext.git" /new/project/path
```

### Update
To update a template after creating a project, run:
```bash
copier update -a .project/.copier-answers.poetry-fastapi-ext.yml /some/project/path
```

## Explore more Copier templates
In addition to this template, there are a number of other Copier templates available. For an overview of all available templates, visit the [Templates Showcase repository](https://github.com/worldworm/copier-showcase).

---
<p align="center">
  <i>© <a href="https://github.com/worldworm">worldworm</a> 2023</i><br>
  <i>Licensed under <a href="https://github.com/worldworm/copier-poetry-fastapi-ext/blob/main/LICENSE">MIT</a></i><br>
</p>
