export default function CounterApp({count, handleIncrement}){
    return(
        <div>
            <h4>{count}</h4>
            <button className="btn" onClick={handleIncrement}>Clicked {count} times</button>
        </div>
    )
}