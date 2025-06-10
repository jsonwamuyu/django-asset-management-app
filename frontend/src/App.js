import { useState } from "react";
import "./App.css";
import ConditionalRendering from "./components/ConditionalRendering";
import MapItems from "./components/MapItems";
import Count from "./components/Practice";
import CountTwo from "./components/PracticeFunction";
import TaskList from "./components/TaskList";
import ToggleButton from "./components/ToggleButton";
import UseEffectHook from "./components/UseEffectHook";
import UserCard from "./components/UserCard";
import Welcome from "./components/Welcome";
import CounterApp from "./components/CounterApp";

const tasks = [
  { id: 1, title: "Complete the project documentation", completed: true },
  { id: 2, title: "Review the code changes", completed: false },
  { id: 3, title: "Prepare for the team meeting", completed: true },
  { id: 4, title: "Update the project roadmap", completed: false },
  { id: 5, title: "Test the new features", completed: true },
];

function App() {
  // Lets pass down this state to child components so that they can share the same count value
  // this is extracting the state and storing it in a centralized place
  // so that we can use it in multiple components
  // this is a common pattern in React to manage state across components. its is called 'state lifting'
  // You can pass the count and setCount as props to child components
  // and they can use them to update the count value
  // This is useful when you have multiple components that need to access the same state

  const [count, setCount] = useState(0);

  const handleIncrement = () => {
    setCount((prevState) => prevState + 1);
  };


  return (
    <div className="container">
      <CounterApp count={count} handleIncrement={handleIncrement}/>
      <CounterApp count={count} handleIncrement={handleIncrement}/>
      <UseEffectHook />
      <div>
        <h3>Task List</h3>
        <div
          style={{ display: "flex", flexDirection: "column", gap: "0.25rem" }}
        >
          {tasks.length > 0 ? (
            tasks.map((task) => (
              <TaskList
                key={task.id}
                title={task.title}
                completed={task.completed}
              />
            ))
          ) : (
            <h4>No tasks available</h4>
          )}
        </div>
      </div>
      <ConditionalRendering />
      <MapItems />
      <ToggleButton />
      <div style={{ display: "flex", gap: "1rem" }}>
        <UserCard name="Grace Wamuyu" age={28} email="wamuyu@example.com" />
      </div>
      <Welcome fullname="Johnson Muchiri" />
      <Count />
      <CountTwo />
    </div>
  );
}

export default App;
