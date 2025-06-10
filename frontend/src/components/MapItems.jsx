import UserCard from "./UserCard";

const users = [
  { id: 1, name: 'Alice', email: 'alice@example.com' },
  { id: 2, name: 'Bob', email: 'bob@example.com' },
  { id: 3, name: 'Charlie', email: 'charlie@example.com' }
];

const MapItems = () => {
    return (
        <div>
            {users.map((user)=>(
                <UserCard key={user.id} fullname={user.name} email={user.email}/>
            ))}
        </div>
    )
}

export default MapItems