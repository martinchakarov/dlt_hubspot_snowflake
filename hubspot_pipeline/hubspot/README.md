# Hubspot > Snowflake dlt pipeline

HubSpot is a customer relationship management (CRM) software and inbound marketing platform that helps businesses attract visitors, engage customers, and close leads.

The `dlt` HubSpot verified source allows you to automatically load data from HubSpot into a Snowflake. It loads data to the following resources:

| resource                   | data                                                                     |
|----------------------------|--------------------------------------------------------------------------|
| contacts                   | visitors, potential customers, leads                                     |
| contacts_property_history  | information about historical changes in contacts properties              |
| companies                  | information about organizations                                          |
| companies_property_history | information about historical changes in companies properties             |
| deals                      | deal records, deal tracking                                              |
| deals_property_history     | information about historical changes in deals properties                 |
| products                   | goods, services                                                          |
| products_property_history  | information about historical changes in products properties              |
| tickets                    | requests for help from customers or users                                |
| tickets_property_history   | information about historical changes in tickets properties               |
| quotes                     | pricing information of a product                                         |
| quotes_property_history    | information about historical changes in quotes properties                |
| Web analytics              | events                                                                   |
| owners                     | information about account managers or users                              |
| pipelines_deals            | stages and progress tracking for deals                                   |
| stages_timing_deals            | history of entering and exiting different stages for the deals pipelines |
| pipelines_tickets          | stages and progress tracking for tickets                                 |
| stages_timing_tickets            | history of entering and exiting different stages for the tickets pipelines |
| properties                 | custom labels for properties with multiple choice                        |

## Installing Dependencies

1. Clone this repository and install Pipenv:
```
git clone https://github.com/martinchakarov/dlt_hubspot_snowflake.git
cd dlt_hubspot_snowflake
pip install pipenv
pipenv install
```
2. Install dependencies:
```
cd hubspot_pipeline
pipenv install -r requirements.txt
```
3. Enter your credentials - navigate to the `.dlt` folder and rename `secrets.toml.sample` to `secrets.toml`. In `secrets.toml`:

    * Enter your private app access token from HubSpot ([instructions](https://dlthub.com/docs/dlt-ecosystem/verified-sources/hubspot#setup-guide)).
    * Enter your [Snowflake credentials](https://dlthub.com/docs/dlt-ecosystem/destinations/snowflake#setup-guide). Make sure to use a user with [Key-Pair Authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth) set up.

4. Navigate back to the `hubspot_pipeline` folder and execute the pipeline:
```
pipenv run python hubspot_pipeline.py
```