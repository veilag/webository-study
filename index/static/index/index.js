anime({
    targets: '.animated',
    opacity: [0, 1],
    translateY: [20, 0],
    scale: [0.9, 1],
    delay: anime.stagger(100)
})

const content = document.querySelector(".markdown")
if (content) {
    content.innerHTML = content.textContent
}
