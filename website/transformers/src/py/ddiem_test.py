import unittest
import os
import configparser

from pathlib import Path
from pyshex import ShExEvaluator
from pyshex.utils.schema_loader import SchemaLoader
from rdflib import Namespace
from rdflib import Graph
from rdflib.namespace import RDF

class TestDdiemRDF(unittest.TestCase):
    RDF_FILE = ""
    BASE = Namespace("http://ddiem.phenomebrowser.net/schema#")
    DDIEM = Namespace("http://ddiem.phenomebrowser.net/")
    OBO = Namespace("http://purl.obolibrary.org/obo/")

    def test_rdf(self):
        config_dir = os.path.expanduser("~") + "/.config"
        config_file = config_dir + "/ddiem-pipeline.ini"
        config = configparser.RawConfigParser()
        config.read(config_file)

        data_dir = config["data"]["dir"] 
        shex_file = data_dir + "/ddiem.shex"

        rdf = Graph()

        rdf.load(data_dir + "/" + self.RDF_FILE)
        shex = Path(shex_file).read_text()
        schema = SchemaLoader().loads(shex)

        total_failures = []
        for combination_procedure in rdf.subjects(RDF.type, self.OBO.DDIEM_0000023):
            failures  = self.evaluate(rdf, schema, combination_procedure, self.BASE.Combination_Procedure)
            if len(failures) > 0:
                total_failures = total_failures + failures

        for procedure in rdf.subjects(RDF.type, self.OBO.OGMS_0000112):
            if (procedure, RDF.type, self.OBO.DDIEM_0000023) in rdf:
                continue

            failures  = self.evaluate(rdf, schema, procedure, self.BASE.Procedure)
            if len(failures) > 0:
                total_failures = total_failures + failures

        for protien in rdf.subjects(RDF.type, self.DDIEM.ProtienOrEnzyme):
            failures  = self.evaluate(rdf, schema, protien, self.BASE.ProtienOrEnzyme)
            if len(failures) > 0:
                total_failures = total_failures + failures

        if len(total_failures) > 0:
            content = ""
            for reason in total_failures:
                content = content + reason + "\n"
            self.fail(f"FAIL: \n {content}")
            

    def evaluate(self, rdf, shex, resource, shex_type):
        results = ShExEvaluator().evaluate(rdf, shex, focus= resource, start=shex_type)
        failures = []
        for item in results:
            if item.result:
                print("PASS:", str(item.focus), str(item.start))
            else:
                failures.append(item.reason)
        
        return failures

if __name__ == "__main__":       
    TestDdiemRDF.RDF_FILE = "ddiem-data.2020-04-29.rdf"
    unittest.main()