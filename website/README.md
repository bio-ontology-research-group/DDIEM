# DDIEM Website

## Build

Run `npm install && npm run build:ssr` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Development server

Run `DATA_FOLDER='ddiem repository folder location on your system' npm run serve:ssr` for a dev server. Navigate to `http://localhost:4000/`. 

## Running DDIEM Data Transformations

DDIEM database is developed by curators in CSV format . Then It is transformed using scripts written in Python. The transformation at first step normalizes data and then maps data with entities in different databases including uniprot, expassy, kegg, omim and drugbank.

#### Normalizing clinical outcomes data and integrating supporting data.  
  
The clinical outcomes data are keyed into a CSV file by our resident physician.  These data are in tabular and are human reader friendly format. Each row of this document presents one distinct clinical outcome record.  
The records are ordered by disease name and treatment, the disease name along with other select fields are omitted if their values are identical to those of the immediate preceding record.  
The omission of field values explained above is done to ease data entry, reduce errors and help in making the document more human readable.  
  
Some of the fields of some of the columns would contain multiple values delineated by a forward slash or comma character.  
Some column contain fields having heterogeneous datatypes in that they may have more than one type of data value such as ec_number and uniprot_id in the same field.  
  
The transformation scripts transform these data for further computer processing and incorporate data from other sources and output a spreadsheet to be subsequently used in scripts that generate the RDF graph representation of the DDIEM clinical outcome data.  
  
The transformation and data integration script does the following.  
1) Cascades the non-empty values of fields of some columns to fields of the same columns having empty values in adjacent rows. In doing so, each record no longer depends on previous records for interpretation and can be processed independently.  
2) Splits columns designated as having heterogeneous datatypes into columns having only one type of data, for example the ec_number or uniprot_id column yields to columns one for ec_number and the other for uniprot_id.  
3) The values of fields having compound values are formatted into a comma separated list of values.  
4) Integrate data from other authority databases to argument the data in the DDIEM clinical outcomes dataset. For this data identifier values such as OMIM_id are used in fetching data and incorporating data such as disease_name from OMIM dataset.

#### Transforming Normalized data to RDF Format

On second step, it takes the normalized data, map it to DDIEM data model and transform it into RDF format.
To run transformation from normalized DDIEM data, first install dependencies by running the following command in transformers folder:

```sh
pip install -r .\requirements.txt
```
After installing the dependencies go to transformers/src/py and run the below command:
```sh
python collapsed_ddiem_csv_transformer.py
```
 It will create a ddiem-data-[date].rdf in data folder of the repository.
