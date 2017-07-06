$(document).ready(function(){
  $(".button-collapse").sideNav();
});

$('.button-collapse').sideNav({
	  menuWidth: 300, // Default is 300
	  edge: 'left', // Choose the horizontal origin
	  closeOnClick: false, // Closes side-nav on <a> clicks, useful for Angular/Meteor
	  draggable: true // Choose whether you can drag to open on touch screens
	}
);
$("#razao_social").bind('keyup', function (e) {
    $("#razao_social").val(($("#razao_social").val()).toUpperCase());
});
$("#nome_fantasia").bind('keyup', function (e) {
    $("#nome_fantasia").val(($("#nome_fantasia").val()).toUpperCase());
});
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
