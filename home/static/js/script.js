const menu_icon = document.getElementById("menu");
const cross_icon = document.getElementById("cross");
const navbar = document.getElementById("navbar");

function toggleMenu() {
  menu_icon.classList.toggle("hidden");
  cross_icon.classList.toggle("hidden");
  console.log(navbar.style.display);
  if ((navbar.style.display == "none") | (navbar.style.display == "")) {
    navbar.style.display = "flex";
  } else {
    navbar.style.display = "none";
  }
}


