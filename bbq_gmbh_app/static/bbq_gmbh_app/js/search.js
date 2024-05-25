document.addEventListener('DOMContentLoaded', function() {
    var rows = document.querySelectorAll('tr[data-href]');
    rows.forEach(function(row) {
        row.addEventListener('click', function() {
            window.location.href = row.getAttribute('data-href');
        });
    });
});

$(document).ready(function(){
  $("input[type='search']").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("table tbody tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});