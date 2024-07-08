"""DataGovtNZSchoolsAPI entry point."""

from __future__ import annotations

from tap_datagovtnzschoolsapi.tap import TapDataGovtNZSchoolsAPI

TapDataGovtNZSchoolsAPI.cli()
