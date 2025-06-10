import { useState }  from 'react'

const ConditionalRendering = () =>{
const [isLoggedIn, setIsLoggedIn] = useState(false);
return(
    <div>
        <h3>Conditional Rendering</h3>
        
        <button onClick={()=> setIsLoggedIn(prevState => !prevState)}>Login</button>
        <p>{isLoggedIn ? 'Welcome Back': "Please login"}</p>
    </div>
)    
}

export default ConditionalRendering