"use strict";

// for voting records page
function showContactInfo(results) {
    $('#contactLegis').toggle();
    $('#phone').show();
}

function usingAjax(evt) {
    $.get('/votes-by-topic', showContactInfo);
}

$('#contactLegis').on('click', usingAjax);

// for contribution page
function showLegisInfo(results) {
    $('#reachLegis').hide();
    $('#phone-number').show();
}

function phoneAjax(evt) {
    $.get('/search', showLegisInfo);
}

$('#reachLegis').on('click', phoneAjax);







