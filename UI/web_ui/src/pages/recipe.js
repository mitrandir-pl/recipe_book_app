import React, {useState, useEffect} from 'react';
import {Link, useParams} from "react-router-dom";
import api from "../components/Axios";
import "../CSS/recipe.css";


function Recipe() {

    const {recipeId} = useParams();
    const [recipe, setRecipe] = useState({ ingredients: [] });

    useEffect(() => {
        api.post('recipes_name', {"name": `${recipeId}`}
            ).then((response) => {
                setRecipe(response.data); console.log(response.data);
            }).catch((error) => console.error(error))
        }, []);
  return (
    <body>
    <h1>{recipeId}</h1>
    <img src={require("../CSS/kan.jpg")} alt="Изображение блюда" />
    <h2>Ingredients</h2>
    <ul>
      {recipe.ingredients.map(item => (
        <li key={item.name}>{item.name} - {item.kcal} kcal</li>
      ))}
    </ul>
    <p> Время приготовления: {recipe.cooking_time_in_min} минут</p>
    <div className="steps">
      <div className="step">
        <p>Шаг 1: Куриное филе отварить и разделить на волокна или нарезать мелкими кубиками. Огурец порезать соломкой, яйца сварить вкрутую и мелко порубить.Салатник лучше взять прямоугольной формы, чтобы слои получились равными.</p>
      </div>
      <div className="step">
        <p>Шаг 2: Выложить ингредиенты слоями, промазывая майонезом, в такой последовательности: курица, ананасы, огурцы. Отставить на 15–20 минут, потом сверху выложить слои яйца и кукурузы.</p>
      </div>
    </div>
  </body>
  );}


export default Recipe
