function Shortener(){
    const url = document.getElementById('')
    const response = fetch('api_url',{
        method: 'POST',
        mode: 'cors',
        credentials: "include",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify ({"url" : url})

      })
    
    console.log(response)

}
