$(document).ready(function() {
  var clipboard = new Clipboard(".comment-area");

  clipboard.on("success", function(e) {
    alert(e.text);
    e.clearSelection();
  });
});
