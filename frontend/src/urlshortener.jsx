import React, {useRef} from "react";
import './style/urlshortener.css';
import "bootstrap/dist/css/bootstrap.min.css";

function UrlShortener(){
    const url_field = useRef(null)
    console.log(url_field.current)

    const handleSubmit = () => {

        const shortener_url = ""
        // header content-type is required
        try {
            const url = new URL(url_field.current);
            console.log(url.href)
            fetch("/create_url_id", {
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
            }).catch((e) => {
                alert(e);
            });
        } catch (e) {
            alert("Invalid URL");
        }
    }
    return (
        <React.Fragment>
        <div className="Auth-form-container">
            <form className="Auth-form" onSubmit={handleSubmit}>
                <h3 className="Auth-form-title">Url Shortener</h3>
                <div className="Auth-form-content">
                    <input 
                        id="url" 
                        type="text" 
                        name="url" 
                        required
                        onChange={(e) => (url_field.current = e.target.value)}></input>
                    <button 
                        type="submit"
                        onClick={() => {handleSubmit}}>
                            OK
                    </button>
                </div>
            </form>
        </div>
        </React.Fragment>
    )
}
export default UrlShortener