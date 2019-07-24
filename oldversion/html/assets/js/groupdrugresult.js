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
        },
        error: function(data) {
            console.log("error");

        }
    });
    $.ajax({
        url: 'http://ddiem.phenomebrowser.net/backend/getTreatment.groovy?term=' + j,
        dataType: "json",
        success: function(data) {
            treatment = '<table class="table"><thead><tr><th>Drug Names</th><th>Phenotypes corrected</th><th>Mutations improved by treatment</th><th>Mutation that did not benefit from treatment</th><th></th></tr></thead><tbody>'
            var rowno = 1;
            $.each(data, function() {
                if(treatments_grouped[this.Drug_name]){
                    treatments_grouped[this.Drug_name].push([[this.Drug_ID,this.Drug_name,this.New_classification,this.Phenotypes_IDS,this.Phenotypes_improved,this.Mutation_that_did_not_benefit_from_treatment ,this.Mutations_improved_by_treatment,this.Treatment_links]]);
                }
                else{
                    treatments_grouped[this.Drug_name]=[[this.Drug_ID,this.Drug_name,this.New_classification,this.Phenotypes_IDS,this.Phenotypes_improved,this.Mutation_that_did_not_benefit_from_treatment ,this.Mutations_improved_by_treatment,this.Treatment_links]];
                }

                 });
            
            //console.log(treatments_grouped);
            for (var key in treatments_grouped) {
                console.log(key);
                drug_rows=treatments_grouped[key];
                $.each(drug_rows, function() {
                    console.log(this[this.length-1]);
                     console.log('******************************************************');
            });
               
                
            }
            $('#treatment').append(treatment);
        },
        error: function(data) {
            console.log("error");

        }
    });
}

function unique(list) {
    var result = [];
    $.each(list, function(i, e) {
        if ($.inArray(e, result) == -1) result.push(e);
    });
    return result;
}