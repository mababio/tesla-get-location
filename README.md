# tesla-get-location

# Summary
  Wrapped [TeslaPy](https://github.com/tdorssers/TeslaPy) python module intop a GCP Cloud Function that returns GPS Cordinates of Tesla vechile.
  Currently, this service is using GCP as compute, but the core logic can live anywhere.

# Setup For GCP
 - Set up GCP project, and IAM service accounts
 - Tesla Credential: Find out how to generate cache.json Tesla credential file [here](https://github.com/tdorssers/TeslaPy)


# Optional
- [Secret Manager](src/secret_manager.py): You can choose to store your cache.json file in GCP Secret manager or store it locally. You can use secret_manager.py script to assist with this.
- [Cloud Build](cloudbuild.yaml): can use [cloudbuild.yaml](cloudbuild.yaml) to build out the Cloud Function.
