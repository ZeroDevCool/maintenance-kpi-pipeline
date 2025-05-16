provider "google" {
  project = "maintenance-kpi-demo"
  region  = "us-central1"
}

resource "google_storage_bucket" "maintenance_data_bucket" {
  name     = "bucket-maintenance-kpi"
  location = "US"
}

resource "google_bigquery_dataset" "maintenance_dataset" {
  dataset_id                  = "maintenance_kpis"
  location                    = "US"
  delete_contents_on_destroy = true
}

resource "google_bigquery_dataset" "maintenance_assertions" {
  dataset_id                  = "maintenance_kpis_assertions"
  location                    = "US"
  delete_contents_on_destroy = true
}