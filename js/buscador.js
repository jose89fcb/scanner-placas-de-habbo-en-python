$(document).ready(function () {
  $('#buscador').keyup(function () {
    var buscarHabbo = $('.buscarHabbo');
    var buscando = $(this).val();
    var item = '';
    for (var i = 0; i < buscarHabbo.length; i++) {if (window.CP.shouldStopExecution(0)) break;
      item = $(buscarHabbo[i]).html().toLowerCase();
      for (var x = 0; x < item.length; x++) {if (window.CP.shouldStopExecution(1)) break;
        if (buscando.length == 0 || item.indexOf(buscando) > -1) {
          $(buscarHabbo[i]).parents('.item').show();
        } else {
          $(buscarHabbo[i]).parents('.item').hide();
        }
      }window.CP.exitedLoop(1);
    }window.CP.exitedLoop(0);
  });
});
//# sourceURL=pen.js