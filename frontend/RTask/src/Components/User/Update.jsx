import axios from "axios";
import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Link } from "react-router-dom";
import { URL_USERS } from "../Path";
function Update() {
  const { id } = useParams();
  const [values, setValues] = useState({
    ismi: "",
    familiya: "",
    email: "",
  });

  const navigate = useNavigate();

  useEffect(() => {
    axios
      .get(`${URL_USERS}` + id)
      .then((res) => setValues(res.data))
      .catch((err) => console.log(err));
  },[]);

  const handelUpdate = (event) => {
    event.preventDefault();
    // console.log(values.data)
    axios
      .put(`${URL_USERS}` + id + '/', values)
      .then((res) => {
        console.log(res);
        navigate("/users");
      })
      .catch(res=> {
        console.log(res)
    });
  };

  return (
    <div className="d-flex w-100 vh-100 justify-content-center align-items-center bg-light ">
      <div className="w-150 border bg-white shadow px-5 pt-3 pb-5 rounded">
        <h1>Update User</h1>
        <form onSubmit={handelUpdate}>
          <div className="mb-2">
            <label htmlFor="name">Name: </label>
            <input
              type="text"
              name="ismi"
              value={values.ismi}
              onChange={(e) => setValues({ ...values, ismi: e.target.value })}
            />
          </div>
          <div className="mb-2">
            <label htmlFor="lastname">LastName: </label>
            <input
              type="text"
              name="familiya"
              value={values.familiya}
              onChange={(e) =>
                setValues({ ...values, familiya: e.target.value })
              }
            />
          </div>
          <div className="mb-2">
            <label htmlFor="email">Email: </label>
            <input
              type="text"
              name="email"
              value={values.email}
              onChange={(e) => setValues({ ...values, email: e.target.value })}
            />
          </div>
          <button type="submit" className="btn btn-primary">
            Submit
          </button>
          <Link to="/users" className="btn btn-info">
            Back
          </Link>
        </form>
      </div>
    </div>
  );
}

export default Update;
