import { SidebarNavbar } from "./Navbar.js"

function Chat(data, main_endpoint){

    let chathtml = `
        <div class="row">
            <div class="col-md-4 container py-3" id="col1">
                ${SidebarNavbar(data, main_endpoint)}
            </div>
            <div class="col container p-0" id="col2">
                <div id="intro-chat" class="">
                <div>                
                    <h1 class="h1 fw-bolder">Glory Chat</h1>
                    <p class="fw-bold">chat with your friends and all your loved ones</p>
                </div>
            </div>
            </div>
        </div>
    `
    
    return chathtml
}

export {Chat}