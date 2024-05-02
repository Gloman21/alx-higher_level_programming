const $ = window.$;
$('#toggle_header').bind('click', function () {
  $('header').toggleClass('green').toggleClass('red');
});
