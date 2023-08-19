let socket_protocol = "ws"
const socket_domain = "127.0.0.1:8000"

if(window.location.protocol === "https"){
    socket_protocol = "wss"
}
const socket_endpoint = `${socket_protocol}://${socket_domain}/chat/`

let socket = new WebSocket(socket_endpoint)

socket.onopen = async function(e){
    console.log('open', e)
}

socket.onmessage = async function(e){
    console.log('message', e)
}

socket.onerror = async function(e){
    console.log('error', e)
}

socket.onclose = async function(e){
    console.log('closed', e)
}