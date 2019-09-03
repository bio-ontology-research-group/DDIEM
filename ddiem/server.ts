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
  private serverUrl = "http://ontolinator.kaust.edu.sa:8891/sparql";

  constructor() { 
      this.fetcher = new SparqlEndpointFetcher();
  }
  
  async listDiseases() {
      const diseaseListQuery = `
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX ddiem: <http://ddiem.phenomebrowser.net/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      
      SELECT ?disease ?label
      FROM <http://www.cbrc.kaust.edu.sa/DDIEM>
      WHERE {
        ?disease rdf:type ddiem:Disease . 
        ?disease rdfs:label ?label
      }`;
      return await this.fetcher.fetchBindings(this.serverUrl, diseaseListQuery);
    
  }

  async getDiseases(iri: any) {
      console.log("diseaseId:" + iri);
      const diseaseQuery = `
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX ddiem: <http://ddiem.phenomebrowser.net/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX obo: <http://purl.obolibrary.org/obo/>

      CONSTRUCT {
        <${iri}> ?prop ?obj .
        ?gene ?geneProp ?geneObj.
        ?protien ?protienProp ?protienObj .
        ?procedure ?procedureProp ?procedureObj .
        ?type ?typeProp ?typeObj .
      }
      FROM <http://www.cbrc.kaust.edu.sa/DDIEM>
      WHERE {
        <${iri}> rdf:type ddiem:Disease .
        <${iri}> ?prop ?obj .

        <${iri}> obo:RO_0004020 ?gene .
        ?gene ?geneProp ?geneObj .

        ?protien obo:RO_0002204 ?gene .
        ?protien ?protienProp ?protienObj .

        ?procedure obo:RO_0002606 <${iri}> .
        ?procedure ?procedureProp ?procedureObj .

        OPTIONAL { 
          ?procedure rdfs:subClassOf ?type .
          ?type ?typeProp ?typeObj .
        }
      }`;
    
      return await this.fetcher.fetchTriples(this.serverUrl, diseaseQuery);
  }

  async getDiseasePhenotypes(iri: any) {
      console.log("diseaseId:" + iri);
      const diseaseQuery = `
      PREFIX obo: <http://purl.obolibrary.org/obo/>
      
      CONSTRUCT {
        ?phenotype ?phenotypeProp ?phenotypeObj .
      }
      FROM <http://www.cbrc.kaust.edu.sa/DDIEM>
      WHERE {
        ?procedure obo:RO_0002606 <${iri}>  .
        ?procedure obo:RO_0002212 ?phenotype .
        ?phenotype ?phenotypeProp ?phenotypeObj .
      }`;
    
      return await this.fetcher.fetchTriples(this.serverUrl, diseaseQuery);
  }

  async getDiseaseDrugs(iri: any) {
    console.log("diseaseId:" + iri);
    const diseaseQuery = `
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    
    CONSTRUCT {
      ?drugAlt ?drugAltProp ?drug .
      ?drug ?drugProp ?drugObj .
    }
    FROM <http://www.cbrc.kaust.edu.sa/DDIEM>
    WHERE {
      ?procedure obo:RO_0002606 <${iri}>  .
      ?procedure obo:RO_0000057 ?drugAlt .
      ?drugAlt ?drugAltProp ?drug .
      ?drug ?drugProp ?drugObj .
    }`;
  
    return await this.fetcher.fetchTriples(this.serverUrl, diseaseQuery);
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

app.get('/api/disease/:id/phenotype', async (req: Request, res:Response) => {
  var id = req.params.id;
  var rdfStream = await diseaseDao.getDiseasePhenotypes(id);
  jsonLd(res, rdfStream);
});

app.get('/api/disease/:id/drug', async (req: Request, res:Response) => {
  var id = req.params.id;
  var rdfStream = await diseaseDao.getDiseaseDrugs(id);
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
    dc: 'http://purl.org/dc/elements/1.1/',
    rdfs: 'http://www.w3.org/2000/01/rdf-schema#',
    ddiem: 'http://ddiem.phenomebrowser.net/',
    omim: 'https://www.omim.org/entry/',
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
