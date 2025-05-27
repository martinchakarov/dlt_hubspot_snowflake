import dlt
from hubspot import hubspot


def load_crm_data() -> None:
    """
    Loads all resources from HubSpot CRM into Snowflake.

    Returns:
        None
    """

    p = dlt.pipeline(
        pipeline_name="hubspot",
        dataset_name="hubspot_dataset",
        destination='snowflake',
        progress='log'
    )

    info = p.run(
        hubspot(include_custom_props=True), 
        write_disposition="replace"
    )

    print(info)


if __name__ == "__main__":
    load_crm_data()