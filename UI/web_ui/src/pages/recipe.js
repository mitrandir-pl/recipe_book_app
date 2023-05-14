import React, {useState, useEffect} from 'react';
import {Link, useParams} from "react-router-dom";
import { Helmet } from 'react-helmet';
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
      <>
          <Helmet>
              <title>Document</title>
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
          </Helmet>
            <body>
            <button className="back-button"><Link to="/recipes">Go back</Link></button>

            <h1>{recipeId}</h1>
            <img src={require("../CSS/kan.jpg")} alt="Изображение блюда" />
            <h2>Ingredients</h2>
            <ul>
              {/*{recipe.ingredients.map(item => (*/}
              {/*  <li key={item.name}>{item.name} - {item.kcal} kcal</li>*/}
              {/*))}*/}
            </ul>
            <p> Время приготовления: {recipe.cooking_time_in_min} минут</p>
            <div className="steps">
              <div className="step">
                <p>{recipe.how_to_cook}</p>
              </div>
            </div>
          </body>
      </>
  );}


export default Recipe
