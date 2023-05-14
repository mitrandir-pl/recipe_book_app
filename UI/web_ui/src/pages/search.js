import React, {useState} from "react";
import { useNavigate } from 'react-router-dom';
import "./css/page6_style.css";
import api from "../components/Axios";

function Search() {

    const [name, setName] = useState('');
    const [country, setCountry] = useState('');
    const [time, setTime] = useState('');
    const [recipes, setRecipes] = useState([]);
    const navigate = useNavigate();
    const handleClick = () => {
        if (name) {
            api.post("recipes_name", {"name": name}).then((response) => {
            localStorage.setItem("recipes", response.data);
            console.log(response.data)
        }).catch((error) => console.error(error))

        }
        navigate("/found")
    }

    return(
        <>
            <head>
                <meta charSet="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <link rel="stylesheet" href="css/page6_style.css" />
                <link rel="preconnect" href="https://fonts.googleapis.com" />
                <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin />
                <link
                href="https://fonts.googleapis.com/css2?family=MuseoModerno:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
                rel="stylesheet" />
                <link rel="preconnect" href="https://fonts.googleapis.com" />
                <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin />
                <link
                href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;800;900&family=Oswald:wght@200;300;400;500;600;700&display=swap"
                rel="stylesheet" />
                <title>Document</title>
            </head>
            <body>
            <main className="main">
                <section className="page6_content_wrap">
                    <h2 className="red_text">Recipe Book</h2>
                    <div className="page6_content">
                        <div className="content_top">
                            <form action="#" className="back_button_wrap">
                                <button className="back_button"> &lt;Back</button>
                            </form>
                        </div>
                        <div className="content_middle">
                            <p className="content_middle_text">Search recepies</p>
                        </div>
                        <div className="content_bottom">
                            <form action="" className="content_bottom_form">
                                <div className="left_inputs">
                                    <input type="text" placeholder="Enter name of the meal" className="input_no_1"
                                    value={name} onChange={event => setName(event.target.value)} />
                                        <input type="text" placeholder="Choose country" className="input_no_2"
                                        value={country} onChange={event => setCountry(event.target.value)} />
                                            <input type="text" placeholder="Choose time fot cook"
                                                   className="input_no_3"
                                            value={time} onChange={event => setTime(event.target.value)} />
                                </div>
                                <div className="right_inputs">
                                    <input type="text" placeholder="Amount of portions" className="input_no_4" />
                                        <button type="submit" className="submit_form" onClick={handleClick} >Search</button>
                                </div>
                            </form>
                        </div>

                    </div>
                </section>
            </main>

            </body>

        </>
    )

}

export default Search
