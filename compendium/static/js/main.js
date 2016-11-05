jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });
});

function loadStatBar(id, qty){
  var bar = new ProgressBar.Line( id, {
    strokeWidth: 4,
    easing: 'easeInOut',
    duration: 1000,
    color: '#73b246',
    trailColor: '#888888',
    trailWidth: 4,
    // svgStyle: {width: '300px', height: '100%'}
  });
  bar.animate(qty/200);
}

function loadHPBar(id, qty){
  var bar = new ProgressBar.Line( id, {
    strokeWidth: 4,
    easing: 'easeInOut',
    duration: 1000,
    color: '#FFEB39',
    trailColor: '#888888',
    trailWidth: 4,
    // svgStyle: {width: '300px', height: '100%'}
  });
  bar.animate(qty/200);
}

function loaBar(id, qty, color){
  var bar = new ProgressBar.Line( id, {
    strokeWidth: 4,
    easing: 'easeInOut',
    duration: 1000,
    color: color,
    trailColor: '#888888',
    trailWidth: 4,
    // svgStyle: {width: '300px', height: '100%'}
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
