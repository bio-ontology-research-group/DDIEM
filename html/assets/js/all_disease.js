var diseaseinfo='<ul>';
$(document).ready(function() {
    $.ajax({
    url: 'http://localhost:9200/searchByID.groovy?term=all',
    dataType: "json",
    success: function(data) {
        $.each(data, function() {
            diseaseinfo = diseaseinfo+'<li><h5 class="media-heading"><u><a href="result.html?id=' + this.id + '" target="_blank">' + this.name + '</a></u></h5></li>';
        });
        diseaseinfo = diseaseinfo+'</ul>';
        $('#all_disease').append(diseaseinfo);
    },
    error: function(data) {
        console.log("error");

    }
});

});
$("#search").autocomplete({
    minLength: 0,
    source: function(request, response) {
        $.ajax({
            url: 'http://localhost:9200/autocomplete.groovy?term=' + request.term,
            dataType: "json",

            success: function(data) {
                response($.map(data, function(item) {
                    console.log(item)
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
        window.location.replace("result.html?id=" + element.item._data);
    }

}).autocomplete("instance")._renderItem = function(ul, item) {
    return $("<li>")
        .append(item.label)
        .appendTo(ul);
};
