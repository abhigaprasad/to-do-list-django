// static/js/main.js
document.addEventListener("DOMContentLoaded", () => {
  const sunflower = document.querySelector(".sunflower");
  sunflower.addEventListener("click", () => {
    sunflower.classList.add("spin");
    setTimeout(() => sunflower.classList.remove("spin"), 2000);
  });
});

