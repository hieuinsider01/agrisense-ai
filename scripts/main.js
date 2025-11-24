let lastScroll = 0;
const header = document.querySelector("header");

window.addEventListener("scroll", handleScroll);
window.addEventListener("mousemove", handleMouseMove);

function handleScroll() {
  let current = window.pageYOffset;

  // If we're at the very top, restore header to normal flow
  if (current <= 0) {
    header.classList.remove("hide", "hover-show");
  }
  // Scrolling down: hide header when past threshold
  else if (current > lastScroll && current > 80) {
    header.classList.add("hide");
    header.classList.remove("hover-show");
  }
  // Scrolling up: reveal header *as a fixed overlay* instead of restoring it
  // back into the document flow (which creates the gap). Use the existing
  // `hover-show` class to bring it back into view while keeping it fixed.
  else if (current < lastScroll) {
    if (header.classList.contains("hide")) {
      header.classList.add("hover-show");
    } else {
      // If it wasn't hidden (edge cases), ensure hover-show is removed.
      header.classList.remove("hover-show");
    }
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
