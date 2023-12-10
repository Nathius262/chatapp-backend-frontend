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
        let location
        if(i.dataset.action === "message"){
            location = '/chat/'
            if (window.location.pathname != location){                
                window.location.href = location
            }
        }else if (i.dataset.action === "profile"){
            location = '/api/profile/'
            if (window.location.pathname != location){                
                window.location.href = location
            }
            
        }else if (i.dataset.action === "home"){
            location = '/'
            if (window.location.pathname != location){                
                window.location.href = location
            }
        }

    })
}