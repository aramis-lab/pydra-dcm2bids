"""Pydra tasks for dcm2niix.

>>> from pydra.tasks.dcm2bids import Dcm2Bids

Examples
--------

>>> task = Dcm2Bids(
...     dicom_dir="/path/to/dicom/dir",
...     output_dir="/path/to/bids/dir",
...     participant_id="sub-01",
...     session_id="ses-baseline",
...     config_file="/path/to/config/file.json",
... )
>>> task.cmdline
'dcm2bids -d /path/to/dicom/dir -p sub-01 -s ses-baseline -c /path/to/config/file.json -o /path/to/bids/dir'
"""
import os
import typing as ty

import attrs

import pydra

__all__ = ["Dcm2Bids"]


@attrs.define(kw_only=True)
class Dcm2BidsSpec(pydra.specs.ShellSpec):
    """Specifications for dcm2bids."""

    dicom_dir: os.PathLike = attrs.field(
        metadata={
            "help_string": "DICOM directory",
            "mandatory": True,
            "argstr": "-d",
            "xor": {"dicom_dirs"},
        }
    )

    dicom_dirs: ty.Iterable[os.PathLike] = attrs.field(
        metadata={
            "help_string": "DICOM directories",
            "mandatory": True,
            "argstr": "-d...",
            "xor": {"dicom_dir"},
        }
    )

    participant_id: str = attrs.field(
        metadata={"help_string": "participant ID", "mandatory": True, "argstr": "-p"}
    )

    session_id: str = attrs.field(
        metadata={"help_string": "session ID", "argstr": "-s"}
    )

    config_file: os.PathLike = attrs.field(
        metadata={
            "help_string": "JSON configuration file",
            "mandatory": True,
            "argstr": "-c",
        }
    )

    output_dir: os.PathLike = attrs.field(
        metadata={"help_string": "output BIDS directory", "argstr": "-o"}
    )


class Dcm2Bids(pydra.engine.ShellCommandTask):
    """Task definition for dcm2bids."""

    input_spec = pydra.specs.SpecInfo(name="Dcm2BidsInput", bases=(Dcm2BidsSpec,))

    executable = "dcm2bids"
