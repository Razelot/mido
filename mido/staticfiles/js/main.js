jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });
});

function loadStatBar(id, qty, color){
  var bar = new ProgressBar.Line( id, {
    strokeWidth: 4,
    easing: 'easeInOut',
    duration: 1000,
    color: color,
    trailColor: '#888888',
    trailWidth: 4,
  });
  bar.animate(qty/200);
}

var calcDataTableHeight = function() {
  var offset = $('body').innerWidth() + $('.content').outerWidth();
  if($(window).width() > 768){
    return $(window).height() * 80/100;
  }else{
    return $(window).height();
  }
};
