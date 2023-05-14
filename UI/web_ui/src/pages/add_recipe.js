import React, {useState} from 'react'
import {Link} from "react-router-dom";
import api from "../components/Axios";
import "../CSS/add_recipe.css"


function AddRecipe() {

    const [recipeName, setRecipeName] = useState("")
    const [ingredients, setIngredients] = useState("")
    const [category, setCategory] = useState("")
    const [cookingTime, setCookingTime] = useState(0)
    const [recipe, setRecipe] = useState("")
    const [selectedImage, setSelectedImage] = useState(null);

    const handleClick = (event) => {
        event.preventDefault();
        const ingredients_obj = ingredients.split("\n").reduce((acc, line) => {
            const [key, value] = line.split(" ");
            acc[key] = Number(value);
            return acc;
        }, {});

        api.post('/recipes_add', {
            "recipe_name": recipeName,
            "ingredients": ingredients_obj,
            "category": category,
            "cooking_time": Number(cookingTime),
            "recipe": recipe,
        }).then((response) => {
                setRecipe(response.data); console.log(response);
            }).catch((error) => console.error(error.response));
        let a;
    }

    const handleImageChange = (event) => {
        const file = event.target.files[0];
        setSelectedImage(file);
    };

    return(
        <body>
            <div className="container">
                <form className="form">
                    <h1>Add Recipe</h1>
                    <label htmlFor="name">Name:</label>
                    <input type="text" id="name" name="name" value={recipeName}
                           onChange={event => setRecipeName(event.target.value)} required />
                        <label htmlFor="ingredients">Ingredients(gramms):</label>
                        <textarea id="ingredients" name="ingredients" value={ingredients}
                           onChange={event => setIngredients(event.target.value)} required/>
                        <label htmlFor="category">Category:</label>
                        <select id="category" name="category" value={category}
                           onChange={event => setCategory(event.target.value)}>
                            <option value="breakfast">Breakfast</option>
                            <option value="lunch">Lunch</option>
                            <option value="dinner">Dinner</option>
                        </select>
                        <label htmlFor="time">Cooking Time:</label>
                        <input type="text" id="time" name="time" value={cookingTime}
                           onChange={event => setCookingTime(event.target.value)} required />
                        <label htmlFor="recipe">Image:</label>
                        <input type="file" accept=".png, .jpg, .jpeg" onChange={handleImageChange} />
                            <label htmlFor="recipe">Recipe:</label>
                            <textarea id="recipe" name="recipe" value={recipe}
                           onChange={event => setRecipe(event.target.value)} required/>
                            <button type="submit" onClick={handleClick}>Add Recipe</button>
                </form>
            </div>
        </body>
    );
}

export default AddRecipe
