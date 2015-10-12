function animateServer(element){
  $('#'+element).animate ({
    opacity: 0.2
    }, 2000, 'linear', function() {
        animateServer(element);
    });
    $('#'+element).animate ({
      opacity: 1.0
      }, 2000, 'linear', function() {
          animateServer(element);
      });
}

function log_viewer(log){
  $.ajaxSetup({
      cache: false
  });
  $(document).ready(function(){
  setInterval(function(){
  $("#log").load("/static/logs/" + log + ".txt")
  window.scrollTo(0,document.body.scrollHeight);
  }, 5000);
  });
}

function load_monitor_data(){
  $.ajaxSetup({
      cache: false
  });
  $(document).ready(function(){
  setInterval(function(){
  $("#monitor").load("/dashboard/monitor_data")
  }, 3000);
  });
}
