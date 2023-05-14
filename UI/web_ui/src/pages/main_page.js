import React from "react";
import "../CSS/main_page.css";
import {Link} from "react-router-dom";


function MainPage() {
    return(
        <>
            <body>
            <header>
                <div className="auth-buttons">
                    <button>Login</button>
                    <button>Register</button>
                </div>
            </header>
            <main>
                <div className="recipe-form">
                    <h1>Выберите действие:</h1>
                    <div className="button-container">
                        <button className="recipe-button"><Link to="/recipes">Все рецепты</Link></button>
                        <button className="recipe-button"><Link to="/recipes/add">Добавить рецепт</Link></button>
                        <button className="recipe-button"><Link to="/recipes/search">Поиск рецептов</Link></button>
                    </div>
                </div>
            </main>
            </body>
        </>
    )
}

export default MainPage
