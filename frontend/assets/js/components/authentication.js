let formSigninEl = document.querySelector('#form-signin')
let formSignupEl = document.querySelector('#form-signup')
let option= {
    method:'post',
    headers:{"Content-Type":"application/json"},
}
let endpoint = 'api/auth/'
let url
formSigninEl.addEventListener('submit', (event)=>{
    event.preventDefault()
    if(formSigninEl.checkValidity()){
        let form_data = new FormData(formSigninEl)
        let json_form = Object.fromEntries(form_data)
        option['body']= JSON.stringify(json_form)
        url = endpoint+'login/'
        fetch(url, option)
        .then((response)=>{
            console.log(response)
            return response.json()
        })
        .then((data)=>{
            window.location.href = '/'
        })
        .catch((err)=>{
            alert(err)
        })
    }
    
})