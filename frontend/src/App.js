import "./App.css";
import ConditionalRendering from "./components/ConditionalRendering";
import MapItems from "./components/MapItems";
import Count from "./components/Practice";
import CountTwo from "./components/PracticeFunction";
import ToggleButton from "./components/ToggleButton";
import UserCard from "./components/UserCard";
import Welcome from "./components/Welcome";

function App() {
  return (
    <div className="App">
      <ConditionalRendering/>
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
