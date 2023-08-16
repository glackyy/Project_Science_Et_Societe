document.addEventListener("DOMContentLoaded", function () {
  const registerLink = document.querySelector(".register-link");
  const registrationContainer = document.querySelector("#registration-container");

  registerLink.addEventListener("click", function (event) {
    event.preventDefault();
    registrationContainer.style.display = "block";
  });
});
