"""DataGovtNZSchoolsAPI tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_datagovtnzschoolsapi import streams


class TapDataGovtNZSchoolsAPI(Tap):
    """DataGovtNZSchoolsAPI tap class."""

    name = "tap-datagovtnzschoolsapi"

    # TODO: Update this section with the actual config values you expect:
    # config_jsonschema = th.PropertiesList(
    #     th.Property(
    #         "start_date",
    #         th.DateTimeType,
    #         description="The earliest record date to sync",
    #     ),
    # ).to_dict()

    def discover_streams(self) -> list[streams.DataGovtNZSchoolsAPIStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [streams.SchoolsStream(self)]

if __name__ == "__main__":
    TapDataGovtNZSchoolsAPI.cli()
