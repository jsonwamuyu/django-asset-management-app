import React from "react";

class Count extends React.Component {
  constructor(props) {
    super();
    this.state = {
      posts: [],
      count: 0,
    };
  }

  componentDidMount() {
    console.log("componentDidMount");
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((response) => response.json())
      .then((data) => {
        this.setState({ posts: data.slice(0, 10) });
      });
  }

  increment = () => {
    this.setState((prev) => ({ count: prev.count + 1 }));
  };
  render() {
    return (
      <div>
        <h2>Posts</h2>
        <ul>
          {this.state.posts.map((post) => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
        <h3>Hello world</h3>
        <p>Welcome to class component.</p>
        <p>Count: {this.state.count}</p>
        <button onClick={this.increment}>Increase</button>
      </div>
    );
  }
}

export default Count;
