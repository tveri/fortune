import { useEffect, useState } from 'react';
import './App.css';
import FortuneWheel from './components/fortuneWheel/fortuneWheel';
import PostService from './API/PostService';


function App() {
  const [winnerIndex, setWinnerIndex] = useState(0)
  const [playerList, setPlayerList] = useState([])
  
  useEffect(() => {
    PostService.getUsersByGroupName('asdasdasd', setPlayerList)
  }, [])
  

  return (
    <div>
      <button onClick={(e) => {
        setWinnerIndex(playerList.length * 3 + 2)
      }}>spin</button>
      {playerList.length && <FortuneWheel playerList={playerList} playerCount={playerList.length} center={[300, 300]} radius={300} winnerIndex={winnerIndex} />}
    </div>
  );
}

export default App;
