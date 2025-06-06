"""Hubspot source settings and constants"""
from dlt.common import pendulum

STARTDATE = pendulum.datetime(year=2024, month=2, day=10)

CRM_CONTACTS_ENDPOINT = (
    "/crm/v3/objects/contacts?associations=deals,products,tickets,quotes"
)
CRM_COMPANIES_ENDPOINT = (
    "/crm/v3/objects/companies?associations=contacts,deals,products,tickets,quotes"
)
CRM_DEALS_ENDPOINT = "/crm/v3/objects/deals"
CRM_PRODUCTS_ENDPOINT = "/crm/v3/objects/products"
CRM_TICKETS_ENDPOINT = "/crm/v3/objects/tickets"
CRM_QUOTES_ENDPOINT = "/crm/v3/objects/quotes"
CRM_OWNERS_ENDPOINT = "/crm/v3/owners/"
CRM_PROPERTIES_ENDPOINT = "/crm/v3/properties/{objectType}/{property_name}"
CRM_PIPELINES_ENDPOINT = "/crm/v3/pipelines/{objectType}"

CRM_OBJECT_ENDPOINTS = {
    "contact": CRM_CONTACTS_ENDPOINT,
    "company": CRM_COMPANIES_ENDPOINT,
    "deal": CRM_DEALS_ENDPOINT,
    "product": CRM_PRODUCTS_ENDPOINT,
    "ticket": CRM_TICKETS_ENDPOINT,
    "quote": CRM_QUOTES_ENDPOINT,
    "owner": CRM_OWNERS_ENDPOINT,
}

WEB_ANALYTICS_EVENTS_ENDPOINT = "/events/v3/events?objectType={objectType}&objectId={objectId}&occurredAfter={occurredAfter}&occurredBefore={occurredBefore}&sort=-occurredAt"

OBJECT_TYPE_SINGULAR = {
    "companies": "company",
    "contacts": "contact",
    "deals": "deal",
    "tickets": "ticket",
    "products": "product",
    "quotes": "quote",
}

OBJECT_TYPE_PLURAL = {v: k for k, v in OBJECT_TYPE_SINGULAR.items()}
ALL_OBJECTS = OBJECT_TYPE_PLURAL.keys()


DEFAULT_COMPANY_PROPS = [
    "createdate",
    "domain",
    "hs_lastmodifieddate",
    "hs_object_id",
    "name",
    "hubspot_owner_id",
    "random_custom_property_test",
    "another_random_custom_property"
]

DEFAULT_CONTACT_PROPS = [
    "createdate",
    "email",
    "firstname",
    "hs_object_id",
    "lastmodifieddate",
    "lastname",
]

DEFAULT_DEAL_PROPS = [
    "amount",
    "closedate",
    "createdate",
    "dealname",
    "dealstage",
    "hs_lastmodifieddate",
    "hs_object_id",
    "pipeline",
]

DEFAULT_TICKET_PROPS = [
    "createdate",
    "content",
    "hs_lastmodifieddate",
    "hs_object_id",
    "hs_pipeline",
    "hs_pipeline_stage",
    "hs_ticket_category",
    "hs_ticket_priority",
    "subject",
]

DEFAULT_PRODUCT_PROPS = [
    "createdate",
    "description",
    "hs_lastmodifieddate",
    "hs_object_id",
    "name",
    "price",
]

DEFAULT_QUOTE_PROPS = [
    "hs_createdate",
    "hs_expiration_date",
    "hs_lastmodifieddate",
    "hs_object_id",
    "hs_public_url_key",
    "hs_status",
    "hs_title",
]

ENTITY_PROPERTIES = {
    "company": DEFAULT_COMPANY_PROPS,
    "contact": DEFAULT_CONTACT_PROPS,
    "deal": DEFAULT_DEAL_PROPS,
    "ticket": DEFAULT_TICKET_PROPS,
    "product": DEFAULT_PRODUCT_PROPS,
    "quote": DEFAULT_QUOTE_PROPS,
}


# 'ALL' represents a list of all available properties for all types
ALL = "All"

PIPELINES_OBJECTS = ["companies", "contacts"]
SOFT_DELETE_KEY = "is_deleted"
ARCHIVED_PARAM = {"archived": True}
PREPROCESSING = {"split": ["hs_merged_object_ids"]}
STAGE_PROPERTY_PREFIX = "hs_date_entered_"
MAX_PROPS_LENGTH = 2000
PROPERTIES_WITH_CUSTOM_LABELS = ()
