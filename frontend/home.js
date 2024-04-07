function Login(){
    const user = document.getElementById("unamefield").value
    const pw = document.getElementById("pwfield").value
    const response = fetch('api_url',{
        method: 'POST',
        mode: 'cors',
        credentials: "include",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify ({"username" : user, "password" : pw})

      })
    
    console.log(response)

}