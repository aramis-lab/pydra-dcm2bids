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

## License

`pydra-dcm2bids` is distributed under the terms of the [Apache License 2.0][license] license.

[pypi-project]: https://pypi.org/project/pydra-dcm2bids
[pypi-version]: https://img.shields.io/pypi/v/pydra-dcm2bids.svg
[pypi-pyversions]: https://img.shields.io/pypi/pyversions/pydra-dcm2bids.svg
[pydra]: https://pydra.readthedocs.io/
[dcm2bids]: https://unfmontreal.github.io/Dcm2Bids/
[bids]: https://bids-specification.readthedocs.io/
[hatch]: https://hatch.pypa.io/
[license]: https://spdx.org/licenses/Apache-2.0.html
