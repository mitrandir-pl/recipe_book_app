import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Recipes from "../pages/recipe_list";
import Recipe from "../pages/recipe"


const AppRouter = () => {
    return (
        <Router>
            <Routes>
                <Route path="/recipes" element={<Recipes />} />
                <Route path="/recipes/:recipeId" element={<Recipe />} />
            </Routes>
        </Router>
    );
};

export default AppRouter;