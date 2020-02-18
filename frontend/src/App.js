import React, { useState } from "react";
import axios from "axios";

import "./App.css";

function App() {
  const [data, setData] = useState("no data");
  const [itemId, setItemId] = useState("");

  const getWishWithId5 = async () => {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/v1/wish/detail/${itemId}/`
    );
    if (response.status !== 200) {
      setData(
        `Error while trying to get item id=${itemId}: ${response.status} ${response.statusText}`
      );
    }
    setData(JSON.stringify(response.data));
  };

  const handleChange = event => {
    setItemId(event.target.value);
  };

  return (
    <div>
      <p>Your data: {data}</p>
      <label>
        Type item id:
        <input type="number" value={itemId} onChange={handleChange} />
      </label>
      <button onClick={() => getWishWithId5()}>Click me</button>
    </div>
  );
}

export default App;
