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

import {SparqlEndpointFetcher} from "fetch-sparql-endpoint";
import {JsonLdSerializer} from "jsonld-streaming-serializer";
import {RdfXmlParser} from "rdfxml-streaming-parser";

const rdfXmlParser = new RdfXmlParser();
const jsonLdSerializer = new JsonLdSerializer({
  context : {
    obo: 'http://purl.obolibrary.org/obo/',
    ddiem: 'http://www.cbrc.kaust.edu.sa/ddiem/terms/',
    n12: 'http://www.cbrc.kaust.edu.sa/ddiem/regimen_mechanism_of_action/Functional interaction(Mechanistic B)',
    n13: 'http://www.cbrc.kaust.edu.sa/ddiem/regimen_mechanism_of_action/Supportive (C)',
  }
});

const diseaseListQuery = `
          SELECT DISTINCT ?OMIM_ID ?disease_name 
          FROM
             <http://www.cbrc.kaust.edu.sa/DDIEM>
          WHERE
          {
              ?OMIM_entry <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_omim_id> ?OMIM_ID .
              ?OMIM_entry <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_disease_name> ?disease_name
          } ORDER BY ASC(?disease_name)`;


// Faster server renders w/ Prod mode (dev mode never needed)
enableProdMode();

// Express server
const app = express();
const fetcher = new SparqlEndpointFetcher();

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
  const bindingsStream = await fetcher.fetchBindings('http://ontolinator.kaust.edu.sa:8891/sparql', diseaseListQuery);
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
  console.log("diseaseId:" + id);
  const diseaseQuery = `
                prefix ns0:	<http://www.cbrc.kaust.edu.sa/ddiem/terms/>

                Describe ${id} ?drug ?dataset ?phenotypeIdCol ?phenotypeTreatment ?reginmenMachanism ?studyTypeEvidence ?treatmentManuscript
                WHERE {
                  ${id} <http://purl.obolibrary.org/obo/RO_0004020> ?drug .
                  ?dataset ns0:has_omim_id ${id} .
                  ?dataset ns0:has_phenotype_ID__collection ?phenotypeIdCol .
                  ?dataset ns0:has_phenotype_improved_by_treatment__bag ?phenotypeTreatment .
                  ?dataset ns0:regimen_mechanism_of_action__collection ?reginmenMachanism .
                  ?dataset ns0:study_type_evidence_code__collection ?studyTypeEvidence .
                  ?dataset ns0:treatment_manuscript_reference__collection ?treatmentManuscript 
                }`;

  const rdfStream = await fetcher.fetchRawStream(
    'http://ontolinator.kaust.edu.sa:8891/sparql', diseaseQuery, 'application/rdf+xml');

  let obs = [];
  rdfStream[1]
  .pipe(rdfXmlParser)
  .pipe(jsonLdSerializer)
  .on('data', obs.push)
  .on('error', console.error)
  .on('end', () => res.json(obs));
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
