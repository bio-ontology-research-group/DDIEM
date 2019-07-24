var treatments_type = ["Direct interaction (Mechanistic A)", "Functional interaction ( Mechanistic B)", "Symptomatic/Supportive (C)"]
var treatments_grouped={}
$(document).ready(function() {
    id = getUrlVars().id;
    showTreatments(id);

});
$("#search").autocomplete({
    minLength: 0,
    source: function(request, response) {
        $.ajax({
            url: 'http://ddiem.phenomebrowser.net/backend/autocomplete.groovy?term=' + request.term,
            dataType: "json",
            success: function(data) {
                response($.map(data, function(item) {
                    return {
                        label: "<div style='padding-bottom: 20px'><b>" + item.name +((item.OMIM_id == "") ? "" :   '</b>- OMIM-ID:' + item.OMIM_id +'</b>')+ "</div>",
                        value: item.name,
                        _data: item.id
                    }
                }));
            }
        });
    },
    select: function(event, element) {
        showTreatments(element.item._data);

    }

}).autocomplete("instance")._renderItem = function(ul, item) {
    return $("<li>")
        .append(item.label)
        .appendTo(ul);
};

function getUrlVars() {
    var vars = [],
        hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for (var i = 0; i < hashes.length; i++) {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }

    return vars;
}

function showTreatments(j) {
    $('#disease').empty();
    $('#treatment').empty();
    $.ajax({
        url: 'http://ddiem.phenomebrowser.net/backend/searchByID.groovy?term=' + j,
        dataType: "json",
        success: function(data) {
            $.each(data, function() {
                gene_affected='';
                if(this.Gene_Affected.includes("/")){
                    gene_affected='<ul class="menu">'
                    var i=0;
                    gene_affected_id=this.Gene_Affected_ID.split('/');
                    gene_array =this.Gene_Affected.split('/');
                    $.each(gene_array, function() {
                        gene_affected=gene_affected+ '<li class="menu-li"><u><a href="https://www.ncbi.nlm.nih.gov/gene/' + gene_affected_id[i] + '" target="_blank">' + this + '</a></u></li>';
                        i++;
                    });
                    gene_affected=gene_affected+'</ul>';
                }
                else {
                    gene_affected=((this.Gene_Affected_ID == "") ? this.Gene_Affected : '<u><a href="https://www.ncbi.nlm.nih.gov/gene/' + this.Gene_Affected_ID + '" target="_blank">' + this.Gene_Affected + '</a></u>')
                }
                diseaseinfo = '<div class="flex-1"><h5 class="media-heading">Disease name:  <small>' + ((this.OMIM_id == "") ? this.name : '<u><a href="https://www.omim.org/entry/' + this.OMIM_id + '" target="_blank">' + this.name + '</a></u>') + '</small></h5>\
                    <h5 class="media-heading">Gene affected:  <small>'+gene_affected+'</small></h5>\
                    <h5 class="media-heading">Enzyme/ protein affected:  <small>' + this.Enzyme_Defected + '</small></h5>\
                    <h5 class="media-heading">EC_number:  <small>' + this.EC_number + '</small></h5></div>\
                    <div class="text-left"><h4 class="mb-1 font-strong "><u>Treatment types</u></h4></br><ul class="text-left font-strong">\
                    <li id="1" class="text-Mechanistic-A">Direct interaction (Mechanistic A)</li>\
                    <li id="2" class="text-Mechanistic-B">Functional interaction ( Mechanistic B)</li>\
                    <li id="3" class="text-Symptomatic">Symptomatic/Supportive (C)</li>\
                    </ul></div>';
            });
            $('#disease').append(diseaseinfo);
            showDrugs();
        },
        error: function(data) {
            console.log("error");

        }
    });
function showDrugs(){
    $.ajax({
        url: 'http://ddiem.phenomebrowser.net/backend/getTreatment.groovy?term=' + j,
        dataType: "json",
        success: function(data) {
            Mutation_did_not_benefit='';
            Mutation_did_benefit='';
            treatment_found=false;
            $.each(data, function() {
                links = '<ul>';
                if(this.Drug_name!=''){
                    treatment_found=true;
                }
                if(this.Treatment_links==',,,,,,,,,,,'){
                    links='';
                }
                else{
                    links_array =this.Treatment_links.split(',');
                    $.each(links_array, function() {
                        if (this != "" && this != "done") {
                            if (this.includes("clinicaltrials") || this.includes("ClinicalTrials")) {
                                links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">Clinical trials</a></li>';
                            } else if (this.includes("sciencedirect")) {
                            links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">Science direct</a></li>';
                        } else if (this.includes("pubmed")) {
                            links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank"> pubmed/' + this.split('/')[this.split('/').length - 1] + '</a></li>';
                        } 
                        else if(this.includes("/pmc/")){
                            links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">'+ this.split('/')[this.split('/').length - 2] +'</a></li>';
                        }
                        else if(this.includes("www.orpha.net")){
                            links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">Orpha</a></li>';
                        }
                        else if(this.includes("semanticscholar")){
                            links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">Semantic scholar</a></li>';
                        }
                        else if(this.includes("academic.oup.com")){
                            links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">Academic</a></li>';                            
                        }
                        else if(this.includes("emedicine.medscape.com")){
                            links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">Medscape</a></li>';                            
                        }
                        else if(this.includes("rarediseases.info.nih.gov")){
                            links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">NIH</a></li>';                            
                        }
                        else if(this.includes("link.springer.com")){
                            links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">Springer</a></li>';                            
                        }
                        else {
                            links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">link</a></li>';
                        }
                    }
                });
                links = links + '</ul>';
                }
                
                if(this.Drug_ID=='NA'){this_Drug_ID="";}
                else{this_Drug_ID=this.Drug_ID;}
                drugs='';
                if(this.Drug_name.includes("+")){
                    drugs=''
                    drugs_array =this.Drug_name.split('+');
                    drugs_id_array =this.Drug_ID.split('+');
                    var i=0;
                    $.each(drugs_array, function() {
                        drugs=drugs+ '<u><a href="https://www.drugbank.ca/drugs/' + drugs_id_array[i]+ '" target="_blank">' + this + '</a></u>  ';
                        i++;
                        if(i!=drugs_array.length){
                            drugs=drugs+' + ';
                        }

                    });
                    
                }
                else {
                    drugs=((this_Drug_ID == "") ? this.Drug_name :'<u><a href="https://www.drugbank.ca/drugs/' + this_Drug_ID + '" target="_blank">' + this.Drug_name + '</a></u>');
                }
                classification='';
                if (this.New_classification.includes("Symptomatic") || this.New_classification.includes("Supportive")) {
                    classification='class="Symptomatic"';
                    $("#3").css({
                        "font-size": "18px",
                        "font-weight": "bolder"
                    });
                } else if (this.New_classification.includes("Direct interaction")) {
                    classification='class="Mechanistic-A"';
                    $("#1").css({
                        "font-size": "18px",
                        "font-weight": "bolder"
                    });
                } else if (this.New_classification.includes("Functional interaction")) {
                    classification='class="Mechanistic-B"';
                    $("#2").css({
                        "font-size": "18px",
                        "font-weight": "bolder"
                    });
                } else {
                    classification='';
                }


                if(this.Mutations_improved_by_treatment!=''){
                    Mutation_did_benefit=this.Mutations_improved_by_treatment;
                }
                if(this.Mutation_that_did_not_benefit_from_treatment!=''){
                    Mutation_did_not_benefit=this.Mutation_that_did_not_benefit_from_treatment;
                }
                if(treatments_grouped[drugs]){
                    tr_value=treatments_grouped[drugs];
                    tr_value.push([this.Phenotypes_IDS,this.Phenotypes_improved,this.Mutations_improved_by_treatment,this.Mutation_that_did_not_benefit_from_treatment,classification,links]);
                    treatments_grouped[drugs]=tr_value;
                }
                else{
                    treatments_grouped[drugs]=[]
                    tr_value=treatments_grouped[drugs];
                    tr_value.push([this.Phenotypes_IDS,this.Phenotypes_improved,this.Mutations_improved_by_treatment,this.Mutation_that_did_not_benefit_from_treatment,classification,links]);
                }
            });
            console.log(Mutation_did_benefit);
            console.log(Mutation_did_not_benefit);
            treatment = '<table class="table"><thead><tr><th>Drug Names</th><th>Phenotypes corrected</th>';
            if(Mutation_did_benefit!=''){
                treatment = treatment+'<th>Mutations improved by treatment</th>';
            }
            if(Mutation_did_not_benefit!=''){
                treatment = treatment+'<th>Mutation that did not benefit from treatment</th>';
            }
            treatment = treatment+'<th></th></tr></thead><tbody>'; 
            var rowno = 1;
            if(treatment_found){
                for (var key in treatments_grouped) {
                    console.log(key);
                    tr_values=treatments_grouped[key];
                    var rownum = tr_values.length>1 ? tr_values.length-1 : tr_values.length;
                    treatment = treatment+'<tr '+tr_values[0][4]+'> <th rowspan='+rownum+'>'+key+'</th><td>'+((tr_values[0][0] == "") ? tr_values[0][1] :'<u><a href="http://www.ontobee.org/ontology/HP?iri=http://purl.obolibrary.org/obo/' + tr_values[0][0].replace(":", "_") + '" target="_blank">' + tr_values[0][1] + '</a></u>')+'</td>'+((Mutation_did_benefit == '') ? '' :'<td>'+tr_values[0][2]+'</td>')+((Mutation_did_not_benefit == '') ? '' :'<td>'+tr_values[0][3]+'</td>')+' <td class="ref">'+((tr_values[0][5] == '') ? '' :'<a data-toggle="collapse" href="#faq' + rowno + '">References<i class="fa fa-angle-down"></i></a><div class="collapse hide" id="faq' + rowno + '">' + tr_values[0][5] + '</div>')+'</td></tr>';
                    console.log(tr_values.length);
                    rowno++;
                    $.each(tr_values.slice(1,tr_values.length-1), function() {
                        treatment = treatment+'<tr '+this[4]+'> <td>'+((this[0] == "") ? this[1] :'<u><a href="http://www.ontobee.org/ontology/HP?iri=http://purl.obolibrary.org/obo/' + this[0].replace(":", "_") + '" target="_blank">' + this[1] + '</a></u>')+((Mutation_did_benefit == '') ? '' :'<td>'+this[2]+'</td>')+((Mutation_did_not_benefit == '') ? '' :'<td>'+this[3]+'</td>')+'</td> <td class="ref">'+((this[5] == '') ? '' :'<a data-toggle="collapse" href="#faq' + rowno + '">References<i class="fa fa-angle-down"></i></a><div class="collapse hide" id="faq' + rowno + '">' + this[5] + '</div>')+'</td></tr>';
                        console.log(treatment);
                        console.log("*******************")
                        rowno++;
                    });
                }
            }
            else{
                treatment = treatment+'<tr><td><b> No treatment found</b></td><td></td><td></td></tr>'
            }
            
            treatment = treatment+'</tbody></table>';
            $('#treatment').append(treatment);
        },
        error: function(data) {
            console.log("error");

        }
    });
}
}

function unique(list) {
    var result = [];
    $.each(list, function(i, e) {
        if ($.inArray(e, result) == -1) result.push(e);
    });
    return result;
}