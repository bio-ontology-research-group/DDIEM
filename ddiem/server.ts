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
  // res.status(200).send("hey")
});

// app.get('/api/disease/:id', async (req: Request, res:Response) => {
//   let query =`
//     DESCRIBE ?OMIM_entry 
//     FROM
//       <http://www.cbrc.kaust.edu.sa/DDIEM>
//     WHERE
//     {
//         ?OMIM_entry <http://www.cbrc.kaust.edu.sa/ddiem/terms/has_omim_id> ()
//   `
//   const bindingsStream = await fetcher.fetchBindings('http://ontolinator.kaust.edu.sa:8891/sparql', diseaseListQuery);
//   let obs = [];
//   bindingsStream.on('data', function(bindings) {
//     obs.push(bindings);
//   });
//   bindingsStream.on('end', function() {
//     res.json(obs);
//   });
//   // res.status(200).send("hey")
// });


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
