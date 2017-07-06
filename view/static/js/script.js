$(document).ready(function(){
  $('.parallax').parallax();
  $('#modalLogin').modal();
  $('#modalRegister').modal();
  $('#modalatendimento').modal();
  $('#modalcadprod').modal();
  $('#modalcadcat').modal();
  $('.collapsible').collapsible();
  $('.fixed-action-btn').openFAB();
  $('.fixed-action-btn').closeFAB();
  $('.fixed-action-btn.toolbar').openToolbar();
  $('.fixed-action-btn.toolbar').closeToolbar();
  $(".button-collapse").sideNav();
 });

(function () {
    var menu = document.getElementById('menu'); // colocar em cache
    window.addEventListener('scroll', function () {
        if (window.scrollY > 20) menu.classList.add('paginaRolada'); // > 0 ou outro valor desejado
        else menu.classList.remove('paginaRolada');
    });
})();

$('.button-collapse').sideNav({
	  menuWidth: 275, // Default is 300
	  edge: 'left', // Choose the horizontal origin
	  closeOnClick: false, // Closes side-nav on <a> clicks, useful for Angular/Meteor
	  draggable: true // Choose whether you can drag to open on touch screens
	}
);
