$(document).ready(function() {
    id = getUrlVars().id;
    showTreatments(id);

});

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
    $('#links').empty();
    $.ajax({
        url: 'http://ddiem.phenomebrowser.net/backend/getLinks.groovy?term=' + j,
        dataType: "json",
        success: function(data) {
            links = '<ul>';
            links_array = []
            $.each(data, function() {
                links_array.push(((this.Treatment_link1 != "") ? this.Treatment_link1 : ""));
                links_array.push(((this.Treatment_links2 != "") ? this.Treatment_links2 : ""));
                links_array.push(((this.Treatment_links3 != "") ? this.Treatment_links3 : ""));
                links_array.push(((this.Treatment_links4 != "") ? this.Treatment_links4 : ""));
                links_array.push(((this.Treatment_links5 != "") ? this.Treatment_links5 : ""));
                links_array.push(((this.Treatment_links6 != "") ? this.Treatment_links6 : ""));
                links_array.push(((this.Type_of_link1 != "") ? this.Type_of_link1 : ""));
                links_array.push(((this.Type_of_link2 != "") ? this.Type_of_link2 : ""));
                links_array.push(((this.Type_of_link3 != "") ? this.Type_of_link3 : ""));
                links_array.push(((this.Type_of_link4 != "") ? this.Type_of_link4 : ""));
                links_array.push(((this.Type_of_link5 != "") ? this.Type_of_link5 : ""));
                links_array.push(((this.Type_of_link6 != "") ? this.Type_of_link6 : ""));
            });
            $.each(links_array, function() {
                console.log(this.split('/')[this.split('/').length - 1]);
                console.log();
                if (this != "" && this != "done") {
                    if (this.includes("clinicaltrials") || this.includes("ClinicalTrials")) {
                        links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">Clinical Trials</a></li>';
                    } else if (this.includes("sciencedirect")) {
                        links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">Science Direct</a></li>';
                    } else if (/[0-9 -()+]+$/.test(this.split('/')[this.split('/').length - 1])) {
                        links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">' + this.split('/')[this.split('/').length - 1] + '</a></li>';
                    } else {
                        links = links + '<li style="padding-bottom: 5px;"><a href="' + this + '" target="_blank">link</a></li>';
                    }
                }
            });
            links = links + '</ul>';
            $('#links').append(links);
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