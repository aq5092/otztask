import { useState } from "react";
import "./App.css";
import Users from "./Components/User/List";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./Components/Home";
import Create from "./Components/User/Create";
import Update from "./Components/User/Update";
import ListUsers from "./Components/User/List";
import Read from "./Components/User/Read";
import 'bootstrap/dist/css/bootstrap.min.css'
function App() {
  const [count, setCount] = useState(0);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/userr/:id" element={<Read/>} ></Route>
        <Route path="/users" element={<ListUsers/>}></Route>
        <Route path="/userc" element={<Create/>}></Route>
        <Route path="/useru/:id" element={<Update/>}></Route>
        
      </Routes>
    </BrowserRouter>
  );
}

export default App;
