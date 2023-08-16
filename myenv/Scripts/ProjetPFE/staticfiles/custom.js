// script.js
function openRegistration() {
  var registrationContainer = document.getElementById("registration-container");
  registrationContainer.style.display = "block";
}
$(document).ready(function() {
  $('#id_username').focus(function() {
    $('.username-requirements').show();
  });

  $('#id_username').blur(function() {
    $('.username-requirements').hide();
  });

  $('#id_confirm_password').focus(function() {
    $('.confirm-password-requirements').show();
  });

  $('#id_confirm_password').blur(function() {
    $('.confirm-password-requirements').hide();
  });
});
