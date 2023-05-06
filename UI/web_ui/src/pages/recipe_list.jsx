import React, {useState, useEffect} from 'react';
import {Link, useParams} from "react-router-dom";
import api from "../components/Axios";
import "../CSS/recipes.css";


function Recipes() {
    const [recipes, setRecipes] = useState([{ingredients: []}]);

    useEffect(() => {
        api.get("recipes").then((response) => {
            setRecipes(response.data);
        }).catch((error) => console.error(error))
    }, []);
    return (
        <div>
            <div>
                <button className="back-button">--Back</button>
            </div>
            <div className="recipe-list">
                <form className="recipe-form">
                    <div className="recipe-image">
                        <img src="https://example.com/recipe-image.jpg" alt="Recipe Image" />
                    </div>
                    <div className="recipe-details">
                        <h2 className="recipe-name">Recipe Name</h2>
                        <p className="recipe-time">Cooking Time: 30 minutes</p>
                        <p className="recipe-calories">Calories: 500</p>
                        <button className="recipe-button">Go to Recipe</button>
                    </div>
                </form>	  
        </div>
	  </div>
      );
}

export default Recipes
