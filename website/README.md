# DDIEM Website

## Build

Run `npm install && npm run build:ssr` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Development server

Run `DATA_FOLDER='ddiem repository folder location on your system' npm run serve:ssr` for a dev server. Navigate to `http://localhost:4000/`. 

## Running DDIEM Data Transformations

DDIEM database is developed by curators in CSV format . Then It is transformed using scripts written in Python. The transformation at first step normalizes data and then maps data with entities in different databases including uniprot, expassy, kegg, omim and drugbank. At second step, it takes the normalized data, maps it to DDIEM data model and transform it into RDF format.

To run transformation from normalized DDIEM data, first install dependencies by running  the following command in *transformers* folder:

```sh
pip install -r .\requirements.txt
```
After installing the dependencies go to transformers/src/py and run the below command:
```sh
python collapsed_ddiem_csv_transformer.py
```
 It will create a ddiem-data-[date].rdf in *data* folder of the repository.
