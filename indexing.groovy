def disease_csv= new File('./data/DDIEM_disease.csv')
def treatment_csv= new File('./data/treatment_disease.csv')
String [] ecc_data=new File('./data/ECC_num.txt')
def disease_with_ecc_csv= new File('./data/DDIEM_disease_ecc.csv')
String [] data=new File('./data/Final_version_under_modification31.csv')
class Disease{
	int Dis_pk
	String OMIM_no
	String Disease_Name
	String Gene_Affected
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
	String Treatment_link1
	String Type_of_link1
	String Treatment_links2
	String Type_of_link2
	String Treatment_links3
	String Type_of_link3
	String Treatment_links4
	String Type_of_link4
	String Treatment_links5
	String Type_of_link5
	String Treatment_links6
	String Type_of_link6
}
def header=data[0]
def diseases=[]
def l1,l2,l3,l4,l5,l6 
l1=l2=l3=l4=l5=l6=""
def t1,t2,t3,t4,t5,t6 
t1=t2=t3=t4=t5=t6=""
def rowNo=1
def dis=0
def tNo=1
data.each{
	//get disease info
	
	 if (it.split(",",-1)[17] != ""){
	 	l1=it.split(",",-1)[17]
	 	t1=it.split(",",-1)[18]
	 }
	 if (it.split(",",-1)[19] != ""){
	 	l2=it.split(",",-1)[19]
	 	t2=it.split(",",-1)[20]
	 }
	 if (it.split(",",-1)[21] != ""){
	 	l3=it.split(",",-1)[21]
	 	t3=it.split(",",-1)[22]
	 }
	 if (it.split(",",-1)[23] != ""){
	 	l4=it.split(",",-1)[23]
	 	t4=it.split(",",-1)[24]
	 }
	 if (it.split(",",-1)[25] != ""){
	 	l5=it.split(",",-1)[25]
	 	t5=it.split(",",-1)[26]
	 }
	 if (it.split(",",-1)[27] != ""){
	 	l6=it.split(",",-1)[27]
	 	t6=it.split(",",-1)[28]
	 }

	if(it.split(",",-1)[0]!=""){
		if(rowNo>1){
			l1=l2=l3=l4=l5=l6=""
			t1=t2=t3=t4=t5=t6=""
		}

		d=new Disease(Dis_pk:rowNo, OMIM_no:it.split(",",-1)[1],Disease_Name:it.split(",",-1)[2],Gene_Affected:it.split(",",-1)[3],Enzyme_Defected:it.split(",",-1)[4],EC_number:it.split(",",-1)[5])
		d.treatments.push(new Treatment(Drug_name:it.split(",",-1)[6], Drug_ID:it.split(",",-1)[7],Mutations_improved_by_treatment:it.split(",",-1)[8],Mutation_that_did_not_benefit_from_treatment:it.split(",",-1)[9],New_classification:it.split(",",-1)[10],Treatment_type:it.split(",",-1)[11],Treatment_status:it.split(",",-1)[12],Phenotypes_improved:it.split(",",-1)[13],Phenotypes_IDS:it.split(",",-1)[14],Rare_side_effects:it.split(",",-1)[15],Side_effects_phenotypes_IDS:it.split(",",-1)[16],Treatment_link1:l1,Type_of_link1:t1,Treatment_links2:l2,Type_of_link2:t2,Treatment_links3:l3,Type_of_link3:t3,Treatment_links4:l4,Type_of_link4:t4,Treatment_links5:l5,Type_of_link5:t5,Treatment_links6:l6,Type_of_link6:t6))
	 	
		println"get ECC number"
		if (d.EC_number==""){
			println "no ecc"
			ecc_id=""
			ecc_data.each{ 
				//println it.split()[1..-1].join()
				if(it.split('\t')[0]=="ID"){
					ecc_id=it.split('\t')[1]
				}
				if(it.split('\t')[0]=="DE"||it.split('\t')[0]=="AN"){
					if(it.split()[1..-1].join().equalsIgnoreCase(d.Enzyme_Defected)||it.split()[1..-1].join().equalsIgnoreCase(d.Enzyme_Defected+".")){
						d.EC_number=ecc_id
						println ecc_id
					}
				}
			}
		}
		if (d.EC_number!=""){
			//println "inside"
			ecc_id=""
			ecc_data.each{ 
				if(it.split('\t')[0]=="ID"){
					ecc_id=it.split()[1]
				}
				if(it.split('\t')[0]=="DE"||it.split('\t')[0]=="AN"){
					if(rowNo==150){println it.split('\t')[1]+"---------------"+d.Enzyme_Defected}
					//println it.split('\t')[1]+"---------------"+d.Enzyme_Defected
					if(it.split()[1..-1].join().equalsIgnoreCase(d.Enzyme_Defected)||it.split()[1..-1].join().equalsIgnoreCase(d.Enzyme_Defected+".")){
						 println d.EC_number+"-------------------"+ecc_id
					}
				}
			}
		}

	 	diseases.push(d)

	 	def row=[rowNo,"'"+d.OMIM_no+"'","'"+d.Disease_Name+"'","'"+d.Gene_Affected+"'","'"+d.Enzyme_Defected+"'","'"+d.EC_number+"'"]
    	disease_with_ecc_csv.append row.join(',')
    	disease_with_ecc_csv.append '\n'
	 	println rowNo
		rowNo++
	}
	else{
		diseases[-1].treatments.push(new Treatment(Drug_name:it.split(",",-1)[6], Drug_ID:it.split(",",-1)[7],Mutations_improved_by_treatment:it.split(",",-1)[8],Mutation_that_did_not_benefit_from_treatment:it.split(",",-1)[9],New_classification:it.split(",",-1)[10],	Treatment_type:it.split(",",-1)[1],Treatment_status:it.split(",",-1)[12],Phenotypes_improved:it.split(",",-1)[13],Phenotypes_IDS:it.split(",",-1)[14],Rare_side_effects:it.split(",",-1)[15],Side_effects_phenotypes_IDS:it.split(",",-1)[16],Treatment_link1:l1,Type_of_link1:t1,Treatment_links2:l2,Type_of_link2:t2,Treatment_links3:l3,Type_of_link3:t3,Treatment_links4:l4,Type_of_link4:t4,Treatment_links5:l5,Type_of_link5:t5,Treatment_links6:l6,Type_of_link6:t6))
		
	}
	
}

/*diseases.each{ d -> 
	d.treatments.each{ t ->
		def row=[tNo,d.Dis_pk,"'"+t.Drug_name+"'","'"+t.Drug_ID+"'","'"+t.Mutations_improved_by_treatment+"'","'"+t.Mutation_that_did_not_benefit_from_treatment+"'","'"+t.New_classification+"'","'"+t.Treatment_type+"'","'"+t.Treatment_status+"'","'"+t.Phenotypes_improved+"'","'"+t.Phenotypes_IDS+"'","'"+t.Rare_side_effects+"'","'"+t.Side_effects_phenotypes_IDS+"'","'"+t.Treatment_link1+"'","'"+t.Type_of_link1+"'","'"+t.Treatment_links2+"'","'"+t.Type_of_link2+"'","'"+t.Treatment_links3+"'","'"+t.Type_of_link3+"'","'"+t.Treatment_links4+"'","'"+t.Type_of_link4+"'","'"+t.Treatment_links5+"'","'"+t.Type_of_link5+"'","'"+t.Treatment_links6+"'","'"+t.Type_of_link6+"'"]
    	treatment_csv.append row.join(',')
    	treatment_csv.append '\n'
    	println tNo	
    	tNo++
		
	}
	println "********************###################################################################****************************"

}*/




