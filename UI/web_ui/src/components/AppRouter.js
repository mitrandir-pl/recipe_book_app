import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Recipes from "../pages/recipe_list";
import Recipe from "../pages/recipe";
import AddRecipe from "../pages/add_recipe";
import MainPage from "../pages/main_page";
import Search from "../pages/search";
import Found from "../pages/found";

const AppRouter = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<MainPage />} />
                <Route path="recipes/search" element={<Search />} />
                <Route path="/recipes" element={<Recipes />} />
                <Route path="/recipes/add" element={<AddRecipe />} />
                <Route path="/recipes/:recipeId" element={<Recipe />} />
                <Route path="/found" element={<Found />} />
            </Routes>
        </Router>
    );
};

export default AppRouter;