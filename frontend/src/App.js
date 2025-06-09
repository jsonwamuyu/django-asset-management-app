import './App.css';
import Count from './components/Practice';
import CountTwo from './components/PracticeFunction'
import Welcome from './components/Welcome';


function App() {
  return (
    <div className="App">
      <Welcome fullname="Johnson Muchiri"/>
        <Count />
        <CountTwo />
    </div>
  );
}

export default App;
