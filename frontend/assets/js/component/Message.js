const main_endpoint = "http://127.0.0.1:8000"

function MessageBody(){
    return `
    <nav id="nav">
        <ul class="list-unstyled mt-4 d-flex justify-content-between container">
            <li class="list-img px-0 pt-3 pb-1 d-flex align-items-center">
                <div class="img-profile"></div>
                <p class="fs-4 fw-bold d-grid">
                    <span id="chat-with">Chat with mike</span>
                    <span class="fs-6 fw-light">3 messages</span>
                </p>
            </li>
            
        </ul>
    </nav>
    <div class="message-body container" id="message-body">           
        
        <ul class="list-unstyled mt-4" id="message-body-list">
            
        </ul>
    </div>

    <form class="message d-flex container p-4" id="message-submit">                    
        <input name="message" type="text" id="message" class="form-control bg-dark text-light border-0 container p-4 fs-4" placeholder="Type your message...">
        <button type="submit" class="btn btn-secondary px-5"><i class="fa fa-send"></i></button>
    </form>
    `
}

function messageBodyInner(main_endpoint, data, chatwith){
    let messageBodyList = document.querySelector('#message-body-list')
    for (let i=0; i<data.length; i++){
        let d = data[i]
        if (`${d.friend.username}` === `${chatwith}`){
            let friend_pix_url = main_endpoint+d.friend.picture
            let user_pix_url =main_endpoint+d.user.picture
            let obj;
            let sender = d.message_receiver
            for (let i=0; i<sender.length; i++){
                let friend = sender[i]
                if (`${friend.sender}` === `${chatwith}`){
                    let nav = document.querySelector('#nav')
                    nav.innerHTML = `
                        <ul class="list-unstyled mt-4 d-flex justify-content-between container">
                        <li class="list-img px-0 pt-3 pb-1 d-flex align-items-center">
                            <div style="background-image:url(${friend_pix_url});" class="img-profile"></div>
                            <p class="fs-4 fw-bold d-grid">
                                <span id="chat-with">Chat with ${chatwith}</span>
                                <span class="fs-6 fw-light">3 messages</span>
                            </p>
                        </li>
                        
                    </ul>
                    `
                    obj = `
                    <li class="receiver list-img px-0 pt-3 pb-1 pt-1 d-flex align-items-center">
                        <div style="background-image:url(${friend_pix_url});" class="img-profile"></div>
                        <div class="">
                            <p class="message-text-receiver shadow fs-4 fw-bold mb-0">${friend.message}</p>
                            <p class="fs-6 fw-light mt-0 px-2">30 Wed 15:12</p>
                        </div>
                        
                    </li>
                        `
                }
                if (`${friend.sender}` != `${chatwith}`){
                    obj = `
                    <li class="sender list-img px-0 pt-3 pb-1 pt-1 d-flex align-items-center">                            
                        <div class="">
                            <p class="message-text-sender shadow fs-4 fw-bold mb-0">${friend.message}</p>
                            <p class="fs-6 fw-light mt-0 px-2">30 Wed 15:12</p>
                        </div>
                        <div style="background-image:url(${user_pix_url});" class="img-profile"></div>
                        
                    </li>
                    `
                }
                messageBodyList.insertAdjacentHTML("afterbegin", obj)
                
            }
            
            
        }
    }
}

let options = {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "Authorization": `BEARER ${localStorage.getItem('access')}`
    }
}

function MessageSubmit(api_endpoint, user, chatwith){
    let a = document.querySelector("#message-submit")
    a.addEventListener("submit", event =>{
        event.preventDefault()
        let form = new FormData(a)
        let url_to = api_endpoint+"chat/message/"
        let formobj = Object.fromEntries(form)
        formobj.sender = user
        formobj.receiver = chatwith
        options.body = JSON.stringify(formobj)
        fetch(url_to, options).then(response =>{
            return response.json()
        }).then(data =>{
            console.log(data)
            let chatwith = "admin"
            messageBodyInner(main_endpoint, data, chatwith)
        }).catch(error =>{
            console.log(error)
        })
    })
}

export {MessageBody, messageBodyInner, MessageSubmit}