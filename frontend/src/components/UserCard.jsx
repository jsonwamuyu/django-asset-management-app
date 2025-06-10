const style = {
    width:"400px",
    height:"200px",
    border:"1px solid black",
    borderRadius:"10px",
    display:"flex",
    flexDirection:"column",
    alignItems:"center",
    justifyContent:"center",
    backgroundColor:"#f0f0f0",
    boxShadow:"0 2px 5px rgba(0,0,0,0.1)",
    margin:"10px",
    padding:"10px",
    fontFamily:"Arial, sans-serif",
    color:"#333",
    fontSize:"16px",
    textAlign:"center",
    transition:"transform 0.2s",
    cursor:"pointer"
}
function UserCard({fullname,email, gender, age}){
    return(
        <div style={style}>
            <h4>NAME: {fullname}</h4>
            <p>EMAIL ADDRESS:{email}</p>
            <p>GENDER: {gender}</p>
            <p>AGE: {age}</p>
        </div>
    )
}

export default UserCard;