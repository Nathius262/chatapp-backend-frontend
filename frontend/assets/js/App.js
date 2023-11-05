let createPostModal = document.querySelector("#createpostBtn")

createPostModal.addEventListener("click", ()=>{
    let postModal = document.querySelector("#createpost")
    postModal.classList.toggle("show")
    postModal.setAttribute("style", "display:block")
})

let navIcon = document.querySelectorAll('.nav-icon')
for (let i of navIcon){
    i.addEventListener('click', ()=>{
        navIcon.forEach(icon =>{
            icon.classList.remove('active-icon')
        })
        i.classList.add('active-icon')
        if(i.dataset.action === "message"){
            window.location.href = 'chat/'
        }else if (i.dataset.action === "profile"){

        }else if (i.dataset.action === "home"){
            window.location.href = '/'
        }

    })
}