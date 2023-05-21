/* jshint esversion: 11 */

const datePicker = document.getElementById('date')
const date = new Date().toJSON().split("T")[0];

datePicker.min = date
        
        
$('.form-control').each(function () {
    floatedLabel($(this));
});

$('.form-control').on('input', function () {
    floatedLabel($(this));
});

function floatedLabel(input) {
    var $field = input.closest('.form-group');
    if (input.val()) {
        $field.addClass('input-not-empty');
    } else {
        $field.removeClass('input-not-empty');
    }
}
