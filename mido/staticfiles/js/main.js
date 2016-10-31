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
