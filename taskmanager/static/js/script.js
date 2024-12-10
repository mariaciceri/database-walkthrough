$(document).ready(function(){
    $('.sidenav').sidenav();
  });

$(document).ready(function(){
    $('.modal').modal();
  });

$(document).ready(function(){
  $('.datepicker').datepicker({
    format: 'yyyy-mm-dd',
    i18n: {done: 'Select'},
    autoClose: true
  });
});

$(document).ready(function(){
  $('select').formSelect();
});