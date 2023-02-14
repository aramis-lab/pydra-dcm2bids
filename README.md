# pydra-dcm2bids

[![PyPI - Version][pypi-version]][pypi-project]
[![PyPI - Python Version][pypi-pyversions]][pypi-project]

---

Pydra tasks for dcm2bids.

[Pydra][pydra] is a dataflow engine which provides
a set of lightweight abstractions for DAG
construction, manipulation, and distributed execution.

[`dcm2bids`][dcm2bids] is a tool which facilitates
conversion from DICOM datasets to NIfTI files
organized as [BIDS][bids].

## Installation

```console
pip install pydra-dcm2bids
```

## Usage

```python
from pydra.tasks import dcm2bids

task = dcm2bids.Dcm2Bids(
    dicom_dir="/path/to/dicom/dir",
    output_dir="/path/to/bids/dir",
    config_file="/path/to/config/file.json",
    participant_id="sub-01",
)

result = task()
```

You may check the following example of a [configuration file][dcm2bids-config-file].

## Development

This project is managed with [Hatch][hatch]:

```console
pipx install hatch
```

To run the test suite:

```console
hatch run test:no-cov
```

To fix linting issues:

```console
hatch run lint:fix
```

To check the documentation:

```console
hatch run docs:serve --open-browser
```

## License

`pydra-dcm2bids` is distributed under the terms of the [Apache License 2.0][license] license.

[pypi-project]: https://pypi.org/project/pydra-dcm2bids
[pypi-version]: https://img.shields.io/pypi/v/pydra-dcm2bids.svg
[pypi-pyversions]: https://img.shields.io/pypi/pyversions/pydra-dcm2bids.svg
[pydra]: https://pydra.readthedocs.io/
[dcm2bids]: https://unfmontreal.github.io/Dcm2Bids/
[bids]: https://bids-specification.readthedocs.io/
[dcm2bids-config-file]: https://unfmontreal.github.io/Dcm2Bids/docs/how-to/create-config-file/
[hatch]: https://hatch.pypa.io/
[license]: https://spdx.org/licenses/Apache-2.0.html
