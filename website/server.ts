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
import {SparqlEndpointFetcher} from "fetch-sparql-endpoint";

// tslint:disable-next-line:no-var-requires
const n3 = require('n3');
const httpProxy = require('http-proxy');
const https = require('https')
const fs = require('fs')

export class DiseaseDao {
  private fetcher:SparqlEndpointFetcher;
  private serverUrl = "http://ontolinator.kaust.edu.sa:8891/sparql";

  constructor() { 
      this.fetcher = new SparqlEndpointFetcher();
  }

  async listLookupResources() {
      const diseaseListQuery = `
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX ddiem: <http://ddiem.phenomebrowser.net/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      
      SELECT ?resource ?label ?type 
      FROM <http://ddiem.phenomebrowser.net>
      WHERE {
        VALUES ?type { ddiem:Disease ddiem:Drug owl:Class} 
        ?resource rdf:type ?type . 
        ?resource rdfs:label ?label
      } ORDER BY ASC(?label) `;
      return await this.fetcher.fetchBindings(this.serverUrl, diseaseListQuery);
  }

  async listDiseasesByDrug(iri: any) {
    console.log("drugId:" + iri);
    const diseaseListQuery = `PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX ddiem: <http://ddiem.phenomebrowser.net/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    
    SELECT distinct ?resource ?label ?type ?drugLabel ?drugUrl 
    FROM <http://ddiem.phenomebrowser.net>
    WHERE {
      VALUES ?type { ddiem:Drug }
      <${iri}> rdf:type ?type;
          rdfs:label ?drugLabel;
          obo:RO_0000056 ?procedure .
      optional {<${iri}>   ddiem:url ?drugUrl . } .
      ?procedure obo:RO_0002599 ?resource .
      ?resource rdf:type ddiem:Disease; 
          rdfs:label ?label .
    } ORDER BY ASC(?label) `;
      return await this.fetcher.fetchBindings(this.serverUrl, diseaseListQuery);
    
  }

  async listDiseasesByMode(iri: any) {
    console.log("modeId:" + iri);
    const diseaseListQuery = `PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX ddiem: <http://ddiem.phenomebrowser.net/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    
    SELECT distinct ?resource ?label ?type ?modeLabel
    FROM <http://ddiem.phenomebrowser.net>
    WHERE {
      VALUES ?type { owl:Class }
      <${iri}> rdf:type ?type .
      OPTIONAL { <${iri}> rdfs:label ?modeLabel . } .
     
      OPTIONAL {
      { 
        ?transitiveTypes rdfs:subClassOf+  <${iri}>.
        ?procedure rdf:type ?transitiveTypes .
      } UNION { 
        ?procedure rdf:type <${iri}> .
      }
      ?procedure obo:RO_0002599 ?resource .
      ?resource rdf:type ddiem:Disease; 
          rdfs:label ?label .
      }
    } ORDER BY ASC(?label) `;
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
      }
      FROM <http://ddiem.phenomebrowser.net>
      WHERE {
        <${iri}> rdf:type ddiem:Disease .
        <${iri}> ?prop ?obj .

        <${iri}> obo:RO_0004020 ?gene .
        ?gene ?geneProp ?geneObj .

        ?protien obo:RO_0002204 ?gene .
        ?protien ?protienProp ?protienObj .
      }`;
    
    return await this.fetcher.fetchRawStream(this.serverUrl, diseaseQuery, SparqlEndpointFetcher.CONTENTTYPE_TURTLE);
  }

  async getDiseasePhenotypes(iri: any) {
      console.log("diseaseId:" + iri);
      const diseaseQuery = `
      PREFIX obo: <http://purl.obolibrary.org/obo/>
      
      CONSTRUCT {
        ?phenotype ?phenotypeProp ?phenotypeObj .
      }
      FROM <http://ddiem.phenomebrowser.net>
      WHERE {
        ?procedure obo:RO_0002599 <${iri}>  .
        ?procedure obo:RO_0002212 ?phenotype .
        ?phenotype ?phenotypeProp ?phenotypeObj .
      }`;
    
    return await this.fetcher.fetchRawStream(this.serverUrl, diseaseQuery, SparqlEndpointFetcher.CONTENTTYPE_TURTLE);
  }

  async getDiseaseDrugs(iri: any) {
    console.log("diseaseId:" + iri);
    const diseaseQuery = `
    PREFIX obo: <http://purl.obolibrary.org/obo/>
    PREFIX ddiem: <http://ddiem.phenomebrowser.net/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    
    CONSTRUCT {
      ?drugAlt ?drugAltProp ?drug .
      ?drug rdfs:label ?label;
            dc:identifier ?identifier;
            ddiem:url ?url .
    }
    FROM <http://ddiem.phenomebrowser.net>
    WHERE {
      ?procedure obo:RO_0002599 <${iri}>  .
      ?procedure obo:RO_0000057 ?drugAlt .
      ?drugAlt ?drugAltProp ?drug .
      ?drug rdfs:label ?label .
      optional { 
        ?drug dc:identifier ?identifier;
              ddiem:url ?url .
      } .
    }`;
  
    return await this.fetcher.fetchRawStream(this.serverUrl, diseaseQuery, SparqlEndpointFetcher.CONTENTTYPE_TURTLE);
}

async getDiseaseProcedures(iri: any) {
  console.log("diseaseId:" + iri);
  const query = `
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX obo: <http://purl.obolibrary.org/obo/>

  CONSTRUCT {
    ?procedure ?procedureProp ?procedureObj .
    ?type ?typeProp ?typeObj .
    ?evidence ?evidenceProp ?evidenceObj .
  }
  FROM <http://ddiem.phenomebrowser.net>
  WHERE {
    ?procedure obo:RO_0002599 <${iri}>.
    ?procedure ?procedureProp ?procedureObj .
    ?procedure rdf:type ?type .
    
    OPTIONAL { 
      ?type ?typeProp ?typeObj .
    }

    OPTIONAL { 
      ?procedure obo:RO_0002558 ?evidence .
      ?evidence ?evidenceProp ?evidenceObj .
    }
  }`;

  return await this.fetcher.fetchRawStream(this.serverUrl, query, SparqlEndpointFetcher.CONTENTTYPE_TURTLE);
}

}


// Faster server renders w/ Prod mode (dev mode never needed)
enableProdMode();


// Express server
const app = express();
const apiProxy = httpProxy.createProxyServer();
const sparqlEndpoint = 'http://ontolinator.kaust.edu.sa:8891';

const diseaseDao = new DiseaseDao();
const PORT = process.env.PORT || 4000;
const HTTPS_PORT = process.env.HTTPS_PORT;
const CERT_PATH = process.env.CERT_PATH;
const KEY_PATH = process.env.KEY_PATH;
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
app.use(function (err, req, res, next) {
  console.error(err.stack)
  res.status(500).send('Something broke!')
})

// Example Express Rest API endpoints
// app.get('/api/**', (req, res) => { });

// For resolving Resource URI to sparql endpoint
app.get('/(\\d+)|([a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})', async (req: Request, res:Response) => {
  var defaultGraphUri = "http://ddiem.phenomebrowser.net";
  var query = `describe <${req.protocol}://${req.get('host')}${req.originalUrl}> from <${defaultGraphUri}>`;
  var format = 'text/html';
  var queryString = `query=${encodeURIComponent(query)}&format=${encodeURIComponent(format)}&timeout=0&debug=on&run=${encodeURIComponent('Run Query')}`;
  req.url = `/sparql?${queryString}`;
  console.log('redirecting to ontolinator', req.url);
  apiProxy.web(req, res, {target: sparqlEndpoint});
});

app.get('/sparql', async (req: Request, res:Response) => {
  console.log('redirecting to ontolinator');
  apiProxy.web(req, res, {target: sparqlEndpoint});
});

app.get('/api/_list_lookup_resources', async (req: Request, res:Response) => {
  const bindingsStream = await diseaseDao.listLookupResources();
  let obs = [];
  bindingsStream.on('data', function(bindings) {
    obs.push(bindings);
  });
  bindingsStream.on('end', function() {
    res.json(obs);
  });
});

app.get('/api/disease', async (req: Request, res:Response) => {
  var drugId = req.query.drug_id;
  var modeId = req.query.mode_id;
  var bindingsStream;
  if (drugId) {
    bindingsStream = await diseaseDao.listDiseasesByDrug(drugId);
  } else {
    bindingsStream = await diseaseDao.listDiseasesByMode(modeId);
  }
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
  jsonLd(res, rdfStream[1]);
});

app.get('/api/disease/:id/phenotype', async (req: Request, res:Response) => {
  var id = req.params.id;
  var rdfStream = await diseaseDao.getDiseasePhenotypes(id);
  jsonLd(res, rdfStream[1]);
});

app.get('/api/disease/:id/drug', async (req: Request, res:Response) => {
  var id = req.params.id;
  var rdfStream = await diseaseDao.getDiseaseDrugs(id);
  jsonLd(res, rdfStream[1]);
});

app.get('/api/disease/:id/procedure', async (req: Request, res:Response) => {
  var id = req.params.id;
    var responseStr='';
    var rdfStream = await diseaseDao.getDiseaseProcedures(id);
    jsonLd(res, rdfStream[1])
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

// Start server on HTTPS
if (HTTPS_PORT && KEY_PATH && CERT_PATH) {
  https.createServer({
    key: fs.readFileSync(KEY_PATH),
    cert: fs.readFileSync(CERT_PATH)
  }, app).listen(HTTPS_PORT, function () {
    console.log(`Node Express server listening on https://localhost:${HTTPS_PORT}`);
  })
}

const jsonLdSerializer = new JsonLdSerializer({
  context : {
    obo: 'http://purl.obolibrary.org/obo/',
    dc: 'http://purl.org/dc/elements/1.1/',
    rdfs: 'http://www.w3.org/2000/01/rdf-schema#',
    ddiem: 'http://ddiem.phenomebrowser.net/',
    omim: 'https://www.omim.org/entry/',
    PMID: 'https://www.ncbi.nlm.nih.gov/pubmed/',
    PMIDs: 'http://www.ncbi.nlm.nih.gov/pubmed/',
    PMCID: 'https://www.ncbi.nlm.nih.gov/pmc/',
    ClinicalTrials: 'https://clinicaltrials.gov/ct2/show/',
    ClinicalTrial: 'http://clinicaltrials.gov/ct2/show/',
    ClinicalTrialswww: 'https://www.clinicaltrials.gov/ct2/show',
    semanticscholar: 'https://pdfs.semanticscholar.org',
    sciencedirect: 'https://www.sciencedirect.com',
    researchgate: 'https://www.researchgate.net',
    rdf:	'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
  }
});

function jsonLd(res: Response, rdfStream: NodeJS.ReadableStream) {
  let responseStr = "";
  let n3Stream = rdfStream.on('error', (err) => { 
                    console.error(err)
                    res.status(500).send('Something broke!')
                  })
                  .pipe(new n3.StreamParser({ format: SparqlEndpointFetcher.CONTENTTYPE_TURTLE }));
  
  jsonLdSerializer.import(n3Stream)
  .on('data', (triples) => {responseStr += triples;})
  .on('error', (err) => { 
    console.error(err.stack);  
    res.status(500).send('Something broke!')
  })
  .on('end', () => res.json(JSON.parse(responseStr)));
}
