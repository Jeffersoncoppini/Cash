$('.button-collapse').sideNav();

$('.collapsible').collapsible();

$('select').material_select();

$("#uf").bind('keyup', function (e) {
    $("#uf").val(($("#uf").val()).toUpperCase());
});
$("#rua").bind('keyup', function (e) {
    $("#rua").val(($("#rua").val()).toUpperCase());
});
$("#bairro").bind('keyup', function (e) {
    $("#bairro").val(($("#bairro").val()).toUpperCase());
});
$("#cidade").bind('keyup', function (e) {
    $("#cidade").val(($("#cidade").val()).toUpperCase());
});
$("#complemento").bind('keyup', function (e) {
    $("#complemento").val(($("#complemento").val()).toUpperCase());
});
$("#nome_categoria").bind('keyup', function (e) {
    $("#nome_categoria").val(($("#nome_categoria").val()).toUpperCase());
});
