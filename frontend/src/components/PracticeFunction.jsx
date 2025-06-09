import { useState, useEffect } from "react";
import {flushSync} from 'react-dom';


function CountTwo() {
  const [count, setCount] = useState(0);
  const [fullname, setFullname] = useState("John Doe");

  const increment = () => {
    setCount(() => count + 1);
    setFullname("Jane Doe");
    console.log(
      "Render not triggered yet. Wait to useEffect lifecycle method to see the change."
    );
  };

  const decrement = () => {
    flushSync(()=> setCount(() => count - 1));
    console.log("Decrement is unbatched, so the render is triggered immediately.");
  flushSync(()=>setFullname("John Smith"));
  };

  useEffect(() => {
    console.log(
      "Now the render is triggered. Count:",
      count,
      "Fullname:",
      fullname
    );
  }, [count, fullname]);

  return (
    <div>
      <h3>Count</h3>
      <p>Welcome to functional components.</p>
      <p>Count: {count}</p>

      <button onClick={increment}>Increment 🔁 Batched Update</button>
      <button onClick={decrement}>Decrement 🚫 Unbatched (flushSync)</button>

      <h5>Hello, {fullname}</h5>
    </div>
  );
}

export default CountTwo;
