function Shortener() {
  const api_url = "" + "/create_url_id/";
  let url_field = document.getElementById("url").value;
  try {
    const url = new URL(url_field);
    fetch(api_url, {
      method: "POST",
      mode: "cors",
      body: JSON.stringify({ user_url: url.href }),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    })
      .then((Response) => {
        return Response.json();
      })
      .then((data) => {
        console.log(data);
      });
  } catch (e) {
    alert("Invalid URL");
  }
}
