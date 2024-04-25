function Shortener() {
  let url_field = document.getElementById("url").value;
  console.log(url_field)
  const shortener_url = "http://127.0.0.1:8000/"
  // header content-type is required
  try {
    const url = new URL(url_field);
    console.log(url.href)
    fetch("http://127.0.0.1:8000/create_url_id", {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({user_url: url.href}),
    })
      .then((data) => data.json())
      .then((data) => {
        window.confirm("Your short url is: " + shortener_url + data.url_id)
      });
  } catch (e) {
    alert("Invalid URL");
  }
}
