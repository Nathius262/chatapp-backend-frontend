function SidebarNavbar(data, main_endpoint){
    
    let html_rep;
    Array.from(data).forEach(obj =>{
        let picture_url = main_endpoint+obj.user.picture
        html_rep = `
            <div id="sidbar-nav">
                <ul class="list-unstyled mt-1 mb-3 d-flex justify-content-between align-items-center">
                    <li class="list-img px-0 pt-3 pb-1 d-inline-flex align-item-center justify-content-start">
                        <div style="background-image:url(${picture_url});" class="img-profile"></div>
                        <div class="fs-4 align-self-center">
                            ${obj.user.username}
                        </div>
                    </li>
                    <li id="navIcon" class="list-img">

                        <i class="fa fa-flash btn btn-light rounded-4 fs-4 mx-3"></i>
                        <i class="fa fa-ellipsis-v fs-4 align-self-center" id="dropdown04" data-bs-toggle="dropdown" aria-expanded="false"></i>

                        <div class="container" id="dropdown-container">
                            <div class="dropdown-menu" aria-labelledby="dropdown04" id="dropdown">
                                <p>testt</p>
                            </div>
                        </div>
                        
                    </li>
                    
                </ul><hr class="fs-3 text-light">
            </div>
            <div id="search" class="d-inline-flex align-items-center justify-content-center">
                <input id="search-input" class="form-control p-3 bg-dark text-light border-0 container" type="text" placeholder="Search...">
                <span class="text-secondary bg-dark"><i class="fa fa-search"></i></span>                    
            </div>

            <div id="list-profile">
                <ul class="list-unstyled mt-4 friend-list" id="friend-list">
                    
                </ul>
            </div>
        `
    })

    return html_rep
}

export { SidebarNavbar};