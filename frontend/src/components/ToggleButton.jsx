import React from 'react'
import {useState} from 'react'

const ToggleButton = () => {
    const [message, setMessage] = useState('OFF')

    const turnOffOn = () =>{
      setMessage(prevState => !prevState)
    }
  return (
    <div>
        <h3>{message? "ON": "OFF"}</h3>
        <button onClick={turnOffOn}>Turn OFF/ON</button>
    </div>
  )
}

export default ToggleButton