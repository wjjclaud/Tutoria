$(document).ready(function () {
    $(".tutor-info").click(function () {
        window.location = "/booking/" + $(this).attr("tutor-id");
    });
    $("#tutor-table").tablesorter({ 
        headers: { 
            2: { sorter: false }, 
        } //disable third colomn for sorting
    }); 
    
});