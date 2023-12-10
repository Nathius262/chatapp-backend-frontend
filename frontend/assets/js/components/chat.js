function getUserFriend(){
    let friendlist = `
    <li>
        <div class="profile"><img src="{% static 'default.png' %}" alt=""></div>
        <div class="profile-name">random</div>
    </li>
    `
    
    return friendlist
}

function postFeed(){
    let postfeed = `
    <div class="post col-md-6">
        <div class="author d-flex justify-content-between align-items-center mt-4 pb-3 border-bottom">
            <div class="profile-name d-flex align-items-center">
                <div class="profile me-3 shadow"><img src="{% static 'default.png' %}" alt=""></div>
                <span class="fw-bold">username</span>
            </div>
            <div>
                <i class="fa-solid fa-ellipsis-vertical"></i>
            </div>
        </div>

        <div class="content mt-4">
            <p class="">This is indeed the best moment of my life! Never that it would be exiting...</p>
            <div class="content-img">
                <img class="container" src="{% static 'img/sample.png' %}" alt="sample image">
            </div>
        </div>
        <div class="content-footer mb-4 d-flex justify-content-between align-items-center mt-4">
            <div>
                <span class="me-4"><i class="fa-solid fa-heart"></i>1.42</span>
                <span><i class="fa-regular fa-comment"></i>124</span>
            </div>
            <div class="">
                2 hours ago
            </div>
        </div>
    </div>
    `
    return postfeed
}

function getRecentChat(){
    let chat = `
    <div class="author d-flex justify-content-between align-items-center mt-4 pb-3">
        <div class="profile-name d-flex align-items-center">
            <div style="border: none;" class="profile me-4 shadow"><img src="{% static 'default.png' %}" alt=""></div>
            <div class="d-grid justify-content-start align-items-center text-start">
                <span class="fs-4">username</span>
                <span class="fw-normal">some string of recent messages</span>  
            </div>
            
        </div>
        <div class="logo">
            <div class="fw-bold">2</div>
        </div>
    </div>
    `
    return chat
}

function chatWith(){
    let userFriend = `
    <div style="border: none;" class="profile me-4 shadow"><img src="{% static 'default.png' %}" alt=""></div>
    <div class="d-grid justify-content-start align-items-center text-start">
        <span class="fs-4" ></span>
        <span class="fw-normal">some string of recent messages</span>  
    </div>
    `
    return userFriend
}

function messageBox(){
    let messagebox = `
    <ul class="list-unstyled mt-4" id="message-body-list">
        <li class="receiver list-img px-0 pt-3 pb-1 pt-1 d-flex align-items-center">
            <div style="background-image:url('defaul.png');" class="img-profile"></div>
            <div class="">
                <p class="message-text-receiver shadow fs-4 fw-normal mb-0">hi! mike</p>
                <p class="fs-6 fw-light mt-0 px-2">30 Wed 15:12</p>
            </div>
            
        </li>

        <li class="sender list-img px-0 pt-3 pb-1 pt-1 d-flex align-items-center">                            
            <div class="">
                <p class="message-text-sender shadow fs-4 fw-normal mb-0">hi! racheal</p>
                <p class="fs-6 fw-light mt-0 px-2 text-end">30 Wed 15:12</p>
            </div>
            <div style="background-image:url('default.png});" class="img-profile"></div>
            
        </li>
        
    </ul>
    `
    return messagebox
}
export {getUserFriend, postFeed, messageBox, getRecentChat, chatWith}