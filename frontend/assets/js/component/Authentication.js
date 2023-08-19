function Login(){
    return `
    <div class="modal modal-tour py-5" tabindex="-1" role="dialog" id="modalLogin">
        <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
                <div class="modal-body p-5">
                <div class="d-grid text-center mb-3 align-items-center justify-content-center">
                    <h2>Glory Chat Login</h2><hr>
                    
                </div>
                <form class="needs-validation" id="loginForm" novalidate="">
                    <div class="row g-3">
        
                    <div class="col-12">
                        <label for="email" class="form-label">Email</label>
                        <input name="email" type="email" class="form-control" id="email" placeholder="you@example.com" required="" autocomplete="email">
                        <div class="invalid-feedback">
                        Please enter a valid email address.
                        </div>
                    </div>

                    <div class="col-12">
                        <label for="password" class="form-label">password</label>
                        <input name="password" type="password" class="form-control" id="password" placeholder="password" required="" autocomplete="password">
                        <div class="invalid-feedback">
                            Please enter a valid password.
                        </div>
                    </div>

                    <div class="text-danger" id="errormsg">
                    </div>
        
                    <hr class="my-4">
                    <button class="w-100 btn btn-dark btn-lg" type="submit">Login</button>
                </form>
                <a class="text-dark text-center fs-5" id="signupClick">Sign up</a>
                
                <!----<button type="button" class="btn btn-lg btn-primary mt-5 w-100" data-bs-dismiss="modal">Great, thanks!</button>----->
                </div>
            </div>
        </div>
    </div>
    `
}

function Signup(){
    return `
    <div class="modal modal-tour py-5" tabindex="-1" role="dialog" id="modalSign">
        <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
                <div class="modal-body p-5">
                <div class="d-grid text-center mb-3 align-items-center justify-content-center">
                    <h2>Glory Chat Signup</h2><hr>
                    
                </div>
                <form class="needs-validation" id="signupForm" novalidate="">
                    <div class="row g-3">
        
                    <div class="col-12">
                        <label for="email" class="form-label">Email</label>
                        <input name="email" type="email" class="form-control" id="email" placeholder="you@example.com" required="" >
                        <div class="invalid-feedback">
                        Please enter a valid email address.
                        </div>
                    </div>

                    <div class="col-12">
                        <label for="username" class="form-label">Username</label>
                        <input name="username" type="text" class="form-control" id="username" placeholder="username" required="" autocomplete="username">
                        <div class="invalid-feedback">
                            Please enter a valid username address.
                        </div>
                    </div>

                    <div class="col-12">
                        <label for="name" class="form-label">Name</label>
                        <input name="name" type="text" class="form-control" id="name" placeholder="Full Name" required="" autocomplete="name">
                        <div class="invalid-feedback">
                            Please enter a valid name address.
                        </div>
                    </div>

                    <div class="col-6">
                        <label for="password1" class="form-label">password</label>
                        <input name="password1" type="password" class="form-control" id="password1" placeholder="Enter password" required="" autocomplete="new-password">
                        <div class="invalid-feedback">
                            Please enter a valid password.
                        </div>
                    </div>

                    <div class="col-6">
                        <label for="password2" class="form-label">Confirm Password</label>
                        <input name="password2" type="password" class="form-control" id="password2" placeholder="confirm password" required="" autocomplete="new-password">
                        <div class="invalid-feedback">
                            Please enter a valid password.
                        </div>
                    </div>

                    <div class="text-danger" id="errormsg">
                    </div>
        
                    <hr class="my-4">
                    <button class="w-100 btn btn-dark btn-lg" type="submit">Sign up</button>
                </form>
                
                </div>
            </div>
        </div>
    </div>
    `
}

function MustAuthenticate(){
    return `
        <div>
            <p>please authenticate</p>
        </div>
    
    `
}

export {Login, Signup, MustAuthenticate}