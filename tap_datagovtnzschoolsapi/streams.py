"""Stream type classes for tap-datagovtnzschoolsapi."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_datagovtnzschoolsapi.client import DataGovtNZSchoolsAPIStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


class SchoolsStream(DataGovtNZSchoolsAPIStream):
    """Returns stream of NZ school data."""

    name = "schools"
    path = ""
    primary_keys: t.ClassVar[list[str]] = ["_id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("_id", th.NumberType),
        th.Property("School_Id", th.StringType),
        th.Property("Telephone", th.StringType),
        th.Property("Fax", th.StringType),
        th.Property("Email", th.StringType),
        th.Property("Contact1_name", th.StringType),
        th.Property("URL", th.StringType),
        th.Property("Add1_Line1", th.StringType),
        th.Property("Add1_Suburb", th.StringType),
        th.Property("Add1_City", th.StringType),
        th.Property("Add2_Line1", th.StringType),
        th.Property("Add2_Suburb", th.StringType),
        th.Property("Add2_City", th.StringType),
        th.Property("Add2_Postal_Code", th.StringType),
        th.Property("Urban_Rural_Indicator", th.StringType),
        th.Property("Org_Type", th.StringType),
        th.Property("Definition", th.StringType),
        th.Property("Authority", th.StringType),
        th.Property("School_Donations", th.StringType),
        th.Property("CoEd_Status", th.StringType),
        th.Property("KMEPeakBody", th.StringType),
        th.Property("Takiwā", th.StringType),
        th.Property("Territorial_Authority", th.StringType),
        th.Property("Regional_Council", th.StringType),
        th.Property("Local_Office_Name", th.StringType),
        th.Property("Education_Region", th.StringType),
        th.Property("General_Electorate", th.StringType),
        th.Property("Māori_Electorate", th.StringType),
        th.Property("Statistical_Area_2_Code", th.StringType),
        th.Property("Statistical_Area_2_Description", th.StringType),
        th.Property("Ward", th.StringType),
        th.Property("Col_Id", th.StringType),
        th.Property("Col_Name", th.StringType),
        th.Property("Latitude", th.NumberType),
        th.Property("Longitude", th.NumberType),
        th.Property("Enrolment_Scheme", th.StringType),
        th.Property("EQi_Index", th.StringType),
        th.Property("Roll_Date", th.DateTimeType),
        th.Property("Total", th.NumberType),
        th.Property("European", th.NumberType),
        th.Property("Māori", th.NumberType),
        th.Property("Pacific", th.NumberType),
        th.Property("Asian", th.NumberType),
        th.Property("MELAA", th.NumberType),
        th.Property("Other", th.NumberType),
        th.Property("International", th.NumberType),
        th.Property("Isolation_Index", th.StringType),
        th.Property("Language_of_Instruction", th.StringType),
        th.Property("BoardingFacilities", th.StringType),
        th.Property("CohortEntry", th.StringType),
        th.Property("Status", th.StringType),
        th.Property("DataSchoolOpened", th.DateTimeType),
    ).to_dict()
