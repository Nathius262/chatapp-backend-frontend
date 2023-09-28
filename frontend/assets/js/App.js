let createPostModal = document.querySelector("#createpostBtn")

createPostModal.addEventListener("click", ()=>{
    let postModal = document.querySelector("#createpost")
    postModal.classList.toggle("show")
    postModal.setAttribute("style", "display:block")
})