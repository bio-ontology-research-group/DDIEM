def disease_csv= new File('./data/DDIEM_disease.csv')
def treatment_csv= new File('./data/treatment_disease.csv')
def remaining_OMIM= new File('./data/remaining_OMIM.csv')
def remaining_gene= new File('./data/remaining_gene.txt')
def remaining_ECC= new File('./data/remaining_ECC.txt')


String [] data=new File('./data/Final_version_under_modification_25_11.csv')
String [] disease=new File('./data/disease_names.txt')
String [] hgene=new File('./data/hgene.txt')

class Disease{
	int Dis_pk
	String OMIM_no
	String Disease_Name
	String Gene_Affected 
	String Gene_Affected_ID=""
	String Enzyme_Defected
	String EC_number
	def treatments=[]
}
class Treatment{
	String Drug_name
	String Drug_ID
	String Mutations_improved_by_treatment
	String Mutation_that_did_not_benefit_from_treatment
	String New_classification
	String Treatment_type
	String Treatment_status
	String Phenotypes_improved
	String Phenotypes_IDS
	String Rare_side_effects
	String Side_effects_phenotypes_IDS
	String Treatment_links
}
def header=data[0]
def diseases=[]
def l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l12,l11,drug,classification,drug_id
l1=l2=l3=l4=l5=l6=l7=l8=l9=l10=l12=l11=drug=classification=""
def rowNo=1
def dis=0
def tNo=1
data.each{
	//drug
	if (it.split(",",-1)[6] != ""){
		drug=it.split(",",-1)[6]
		drug_id=it.split(",",-1)[7]
	}
	if (it.split(",",-1)[10] != ""){
		classification=it.split(",",-1)[10]
	}
	//get links info
	if (it.split(",",-1)[17] != ""){
		l1=it.split(",",-1)[17]
	}
	if (it.split(",",-1)[18] != ""){
		l2=it.split(",",-1)[18]
	}
	if (it.split(",",-1)[19] != ""){
	 	l3=it.split(",",-1)[19]
	}
	if (it.split(",",-1)[20] != ""){
		l4=it.split(",",-1)[20]
	}
	if (it.split(",",-1)[21] != ""){
		l5=it.split(",",-1)[21]
	}
	if (it.split(",",-1)[22] != ""){
		l6=it.split(",",-1)[22]
	}
	if (it.split(",",-1)[23] != ""){
		l7=it.split(",",-1)[23]
	}
	if (it.split(",",-1)[24] != ""){
		l8=it.split(",",-1)[24]
	}
	if (it.split(",",-1)[25] != ""){
		l9=it.split(",",-1)[25]
	}
	if (it.split(",",-1)[26] != ""){
		l10=it.split(",",-1)[26]
	}
	if (it.split(",",-1)[27] != ""){
		l11=it.split(",",-1)[27]
	}
	if (it.split(",",-1)[28] != ""){
		l12=it.split(",",-1)[28]
	}
	if(it.split(",",-1)[0]!=""){
		l1=l2=l3=l4=l5=l6=l7=l8=l9=l10=l12=l11=drug=""
			//drug
		if (it.split(",",-1)[6] != ""){
			drug=it.split(",",-1)[6]
			drug_id=it.split(",",-1)[7]
		}
		if (it.split(",",-1)[10] != ""){
			classification=it.split(",",-1)[10]
		}
		//get links info
		if (it.split(",",-1)[17] != ""){
			l1=it.split(",",-1)[17]
		}
		if (it.split(",",-1)[18] != ""){
			l2=it.split(",",-1)[18]
		}
		if (it.split(",",-1)[19] != ""){
	 		l3=it.split(",",-1)[19]
		}
		if (it.split(",",-1)[20] != ""){
			l4=it.split(",",-1)[20]
		}
		if (it.split(",",-1)[21] != ""){
			l5=it.split(",",-1)[21]
		}
		if (it.split(",",-1)[22] != ""){
			l6=it.split(",",-1)[22]
		}
		if (it.split(",",-1)[23] != ""){
			l7=it.split(",",-1)[23]
		}
		if (it.split(",",-1)[24] != ""){
			l8=it.split(",",-1)[24]
		}
		if (it.split(",",-1)[25] != ""){
			l9=it.split(",",-1)[25]
		}
		if (it.split(",",-1)[26] != ""){
			l10=it.split(",",-1)[26]
		}
		if (it.split(",",-1)[27] != ""){
			l11=it.split(",",-1)[27]
		}
		if (it.split(",",-1)[28] != ""){
			l12=it.split(",",-1)[28]
		}
		d=new Disease(Dis_pk:rowNo, OMIM_no:it.split(",",-1)[1],Disease_Name:it.split(",",-1)[2],Gene_Affected:it.split(",",-1)[3],Enzyme_Defected:it.split(",",-1)[4],EC_number:it.split(",",-1)[5])
		d.treatments.push(new Treatment(Drug_name:drug, Drug_ID:drug_id,Mutations_improved_by_treatment:it.split(",",-1)[8],Mutation_that_did_not_benefit_from_treatment:it.split(",",-1)[9],New_classification:classification,Treatment_type:it.split(",",-1)[11],Treatment_status:it.split(",",-1)[12],Phenotypes_improved:it.split(",",-1)[13],Phenotypes_IDS:it.split(",",-1)[14],Rare_side_effects:it.split(",",-1)[15],Side_effects_phenotypes_IDS:it.split(",",-1)[16],Treatment_links:l1+","+l2+","+l3+","+l4+","+l5+","+l6+","+l7+","+l8+","+l9+","+l10+","+l11+","+l12))
	 	if(d.OMIM_no==""){
	 		disease.each {
	 			omim=it.split('\t',-1)[0]
	 			it.split('\t',-1)[1..-1].join().split(',').each {
	 				if((it.trim()).equalsIgnoreCase(d.Disease_Name.trim().minus("�"))){
	 					d.OMIM_no=omim
	 				}
	 			}
	 		}
	 	}

	 	genes=d.Gene_Affected.minus(" gene").minus("gene").minus("�").split('/')
	 	hgene.each{ gene ->
	 		gno=0
	 		genes.each{
	 			if((gene.split('\t',-1)[1].trim()).equalsIgnoreCase(it.trim())){
	 				if(gno==0){
	 					d.Gene_Affected_ID=gene.split('\t',-1)[0].trim()
	 				}
	 				else{
	 					d.Gene_Affected_ID=d.Gene_Affected_ID+"/"+gene.split('\t',-1)[0].trim()
	 				}
	 			}
	 			gno+=gno+1
	 			
	 		}
	 	}
	 	if(d.Gene_Affected_ID==""){
    		//remaining_gene.append d.Disease_Name.minus("�")+"\t"+(d.Gene_Affected.minus("�")).trim()
	 		//remaining_gene.append '\n'
    	}
    	if(d.OMIM_no==""){
    		//remaining_OMIM.append d.Disease_Name.minus("�")
    		//remaining_OMIM.append '\n'
    	}
    	if(d.EC_number==""){
    		//remaining_ECC.append d.Disease_Name.minus("�")
    		//remaining_ECC.append '\n'
    	}
	 	diseases.push(d) 
	 	def row=[rowNo,"'"+d.OMIM_no+"'","'"+d.Disease_Name.minus("�")+"'","'"+d.Gene_Affected.minus("�").minus("gene")+"'","'"+d.Gene_Affected_ID.minus("�")+"'","'"+d.Enzyme_Defected.minus("�")+"'","'"+d.EC_number.minus("�")+"'"]
    	//disease_csv.append row.join(',')
    	//disease_csv.append '\n'
	 	println rowNo
		rowNo++
	}
	else{
		diseases[-1].treatments.push(new Treatment(Drug_name:drug, Drug_ID:drug_id,Mutations_improved_by_treatment:it.split(",",-1)[8],Mutation_that_did_not_benefit_from_treatment:it.split(",",-1)[9],New_classification:classification,Treatment_type:it.split(",",-1)[1],Treatment_status:it.split(",",-1)[12],Phenotypes_improved:it.split(",",-1)[13],Phenotypes_IDS:it.split(",",-1)[14],Rare_side_effects:it.split(",",-1)[15],Side_effects_phenotypes_IDS:it.split(",",-1)[16],Treatment_links:l1+","+l2+","+l3+","+l4+","+l5+","+l6+","+l7+","+l8+","+l9+","+l10+","+l11+","+l12))
			}	
}

diseases.each{ d -> 

	d.treatments.each{ t ->
		def row=[tNo,d.Dis_pk,"'"+t.Drug_name.minus("�")+"'","'"+t.Drug_ID.minus("�")+"'","'"+t.Mutations_improved_by_treatment.minus("�")+"'","'"+t.Mutation_that_did_not_benefit_from_treatment.minus("�")+"'","'"+t.New_classification.minus("�")+"'","'"+t.Treatment_type.minus("�")+"'","'"+t.Treatment_status.minus("�")+"'","'"+t.Phenotypes_improved.minus("�")+"'","'"+t.Phenotypes_IDS.minus("�")+"'","'"+t.Rare_side_effects.minus("�")+"'","'"+t.Side_effects_phenotypes_IDS.minus("�")+"'","'"+t.Treatment_links.minus("�")+"'"]
		treatment_csv.append row.join(',')
    	treatment_csv.append '\n'
    	println tNo	
    	tNo++
		
	}
	println "********************#########################****************************"

}
