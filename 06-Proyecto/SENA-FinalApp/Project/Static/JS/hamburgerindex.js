const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-menu");
const body = document.querySelector("body");

navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("nav-menu_visible");
});
