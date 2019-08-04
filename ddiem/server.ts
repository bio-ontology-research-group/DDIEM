import 'zone.js/dist/zone-node';
import 'reflect-metadata';
import {enableProdMode} from '@angular/core';
// Express Engine
import {ngExpressEngine} from '@nguniversal/express-engine';
// Import module map for lazy loading
import {provideModuleMap} from '@nguniversal/module-map-ngfactory-loader';

import {Request, Response} from "express";

import * as express from 'express';
import {join} from 'path';

import {JsonLdSerializer} from "jsonld-streaming-serializer";
import { Quad, Stream } from 'rdf-js';
import {SparqlEndpointFetcher} from "fetch-sparql-endpoint";


export class DiseaseDao {
  private fetcher:SparqlEndpointFetcher;

  constructor() { 
      this.fetcher = new SparqlEndpointFetcher();
  }
  
  async listDiseases() {
      const diseaseListQuery = `
          SELECT DISTINCT ?OMIM_ID ?disease_name ?OMIM_entry
          FROM
              <http://www.cbrc.kaust.edu.sa/DDIEM>
          WHERE
          {
              ?OMIM_entry <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_omim_id> ?OMIM_ID .
              ?OMIM_entry <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_disease_name> ?disease_name
          } ORDER BY ASC(?disease_name)`;
      return await this.fetcher.fetchBindings('http://ontolinator.kaust.edu.sa:8891/sparql', diseaseListQuery);
    
  }

  async getDiseases(iri: any) {
      console.log("diseaseId:" + iri);
      const diseaseQuery = `
          prefix ns0:    <http://www.cbrc.kaust.edu.sa/ddiem/terms/>
          prefix n1:     <http://purl.obolibrary.org/obo/>
          CONSTRUCT {
              <${iri}> ?prop ?value .
              ?gene ?geneProp ?geneValue .
              ?product ?productProp ?productValue .
              ?dataset ?dsProp ?obj.
              ?obj ?objProp ?objValue
          }
          WHERE {
              <${iri}> ?prop ?value .
              <${iri}> <http://purl.obolibrary.org/obo/RO_0004020> ?gene .
              ?gene ?geneProp ?geneValue .
              ?gene n1:RO_0002205 ?product .
              ?product ?productProp ?productValue .
              ?dataset ns0:has_omim_id <${iri}> .
              ?dataset ?dsProp ?obj .
              ?obj ?objProp ?objValue .
              MINUS { ?dataset ns0:regimen_mechanism_of_action__collection ?obj }
          }`;
    
      return await this.fetcher.fetchTriples('http://ontolinator.kaust.edu.sa:8891/sparql', diseaseQuery);
  }

  async getTreatmentDrug(iri: any) {
      console.log("treatment:" + iri);
      const diseaseQuery = `
          prefix ns0:    <http://www.cbrc.kaust.edu.sa/ddiem/regimen/>
          prefix n1:     <http://purl.obolibrary.org/obo/>
          CONSTRUCT {
              <${iri}> ?prop ?drug.
          ?drug ?drugProp ?drugObj .
          ?drugObj ?drugObjProp ?drugObjValue
          } WHERE {
          <${iri}> ?prop ?drug .
          ?drug ?drugProp ?drugObj .
          ?drugObj ?drugObjProp ?drugObjValue
          }`;
    
      return await this.fetcher.fetchTriples('http://ontolinator.kaust.edu.sa:8891/sparql', diseaseQuery);
  }
}


// Faster server renders w/ Prod mode (dev mode never needed)
enableProdMode();


// Express server
const app = express();
const diseaseDao = new DiseaseDao();
const PORT = process.env.PORT || 4000;
const DIST_FOLDER = join(process.cwd(), 'dist/browser');

// * NOTE :: leave this as require() since this file is built Dynamically from webpack
const {AppServerModuleNgFactory, LAZY_MODULE_MAP} = require('./dist/server/main');

// Our Universal express-engine (found @ https://github.com/angular/universal/tree/master/modules/express-engine)
app.engine('html', ngExpressEngine({
  bootstrap: AppServerModuleNgFactory,
  providers: [
    provideModuleMap(LAZY_MODULE_MAP)
  ]
}));

app.set('view engine', 'html');
app.set('views', DIST_FOLDER);

// Example Express Rest API endpoints
// app.get('/api/**', (req, res) => { });

app.get('/api/disease', async (req: Request, res:Response) => {
  const bindingsStream = await diseaseDao.listDiseases();
  let obs = [];
  bindingsStream.on('data', function(bindings) {
    obs.push(bindings);
  });
  bindingsStream.on('end', function() {
    res.json(obs);
  });
});

app.get('/api/disease/:id', async (req: Request, res:Response) => {
  var id = req.params.id;
  var rdfStream = await diseaseDao.getDiseases(id);
  jsonLd(res, rdfStream);
});

app.get('/api/treatment/:id/drug', async (req: Request, res:Response) => {
  var id = req.params.id;
  var rdfStream = await diseaseDao.getTreatmentDrug(id);
  jsonLd(res, rdfStream);
});

// Server static files from /browser
app.get('*.*', express.static(DIST_FOLDER, {
  maxAge: '1y'
}));

// All regular routes use the Universal engine
app.get('*', (req, res) => {
  res.render('index', { req });
});

// Start up the Node server
app.listen(PORT, () => {
  console.log(`Node Express server listening on http://localhost:${PORT}`);
});

const jsonLdSerializer = new JsonLdSerializer({
  context : {
    obo: 'http://purl.obolibrary.org/obo/',
    ddiem: 'http://www.cbrc.kaust.edu.sa/ddiem/terms/',
    ds: 'http://www.cbrc.kaust.edu.sa/ddiem/dataset/',
    n12: 'http://www.cbrc.kaust.edu.sa/ddiem/regimen_mechanism_of_action/Functional interaction(Mechanistic B)',
    n13: 'http://www.cbrc.kaust.edu.sa/ddiem/regimen_mechanism_of_action/Supportive (C)',
    pubmed: 'https://www.ncbi.nlm.nih.gov/pubmed/',
    rdf:	'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
  }
});

function jsonLd(res: Response, rdfStream: Stream<Quad>) {
  let responseStr = "";
  jsonLdSerializer.import(rdfStream)
  .on('data', (triples) => {responseStr += triples;})
  .on('error', console.error)
  .on('end', () => res.json(JSON.parse(responseStr)));
}
