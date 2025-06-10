export default function CounterApp({count, handleIncrement}){
    return(
        <div>
            <h4>{count}</h4>
            <button onClick={handleIncrement}>Increment</button>
        </div>
    )
}