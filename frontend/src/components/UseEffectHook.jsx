import React from "react";
import { useEffect, useState } from "react";

const UseEffectHook = () => {
  const [posts, setPosts] = useState([]);
  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((response) => response.json())
      .then((data) => setPosts(data.slice(0,5)));
  }, []);

  return (
    <div>
      <h3>Recent Posts</h3>
      <ul>
        {posts.map((post)=>(
            <li key={post.id}>
                <h4>{post.title}</h4>
                <p>{post.body}</p>
            </li>
        ))}
      </ul>
    </div>
  );
};

export default UseEffectHook;
