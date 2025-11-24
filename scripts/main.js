let lastScroll = 0;
const header = document.querySelector("header");

window.addEventListener("scroll", handleScroll);
window.addEventListener("mousemove", handleMouseMove);

function handleScroll() {
  let current = window.pageYOffset;

  if (current < lastScroll || current <= 0) {
    header.classList.remove("hide", "hover-show");
  } else if (current > lastScroll && current > 80) {
    header.classList.add("hide");
    header.classList.remove("hover-show");
  }

  lastScroll = current;
}
function handleMouseMove(e) {
  if (e.clientY <= 30 && header.classList.contains("hide")) {
    header.classList.add("hover-show");
  } else if (e.clientY > 100) {
    header.classList.remove("hover-show");
  }
}
