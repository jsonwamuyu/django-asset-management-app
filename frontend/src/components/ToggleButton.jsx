import React from 'react'
import {useState} from 'react'

const ToggleButton = () => {
    const [message, setMessage] = useState('OFF')

    const turnOff = () =>{
      setMessage("OFF")
    }
  return (
    <div>
        <h3>{message}</h3>
        <button onClick={()=>setMessage("ON")}>Turn ON</button>
        <button onClick={turnOff}>Turn OFF</button>
    </div>
  )
}

export default ToggleButton