import dlt
from hubspot import hubspot

def load_crm_data() -> None:
    """
    Loads all selected resources from HubSpot CRM into Snowflake.

    Returns:
        None
    """

    pipeline = dlt.pipeline(
        pipeline_name="hubspot",
        dataset_name="hubspot_dataset",
        destination='snowflake',
        progress='log'
    )

    data = hubspot(include_custom_props=False)
    
    info = pipeline.run(
        data.with_resources("companies", "owners"), 
        write_disposition="replace"
    )

    print(info)


if __name__ == "__main__":
    load_crm_data()