import React from "react";
const style = {
  backgroundColor: "#fff",
  padding: "10px",
  borderRadius: "5px",
  margin: "10px 0",
  boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
};

const TaskList = ({ id, title, completed }) => {
  return (
    <div style={style}>
      <h4>
        {completed ? "✅" : ""}
        {title}
      </h4>
    </div>
  );
};

export default TaskList;
