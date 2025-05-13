import React, { useState, useEffect, useRef } from 'react';

const CELL_SIZE = 20;
const WIDTH = 400;
const HEIGHT = 400;

const getRandomFood = () => {
  const x = Math.floor((Math.random() * WIDTH) / CELL_SIZE) * CELL_SIZE;
  const y = Math.floor((Math.random() * HEIGHT) / CELL_SIZE) * CELL_SIZE;
  return { x, y };
};

function App() {
  const [snake, setSnake] = useState([{ x: 0, y: 0 }]);
  const [food, setFood] = useState(getRandomFood);
  const [dir, setDir] = useState({ x: CELL_SIZE, y: 0 });
  const [gameOver, setGameOver] = useState(false);

  const boardRef = useRef(null);

  useEffect(() => {
    const handleKey = (e) => {
      switch (e.key) {
        case 'ArrowUp':
          if (dir.y === 0) setDir({ x: 0, y: -CELL_SIZE });
          break;
        case 'ArrowDown':
          if (dir.y === 0) setDir({ x: 0, y: CELL_SIZE });
          break;
        case 'ArrowLeft':
          if (dir.x === 0) setDir({ x: -CELL_SIZE, y: 0 });
          break;
        case 'ArrowRight':
          if (dir.x === 0) setDir({ x: CELL_SIZE, y: 0 });
          break;
        default:
          break;
      }
    };

    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  }, [dir]);

  useEffect(() => {
    if (gameOver) return;

    const interval = setInterval(() => {
      setSnake((prev) => {
        const head = { ...prev[0] };
        head.x += dir.x;
        head.y += dir.y;

        // 벽 충돌
        if (
          head.x < 0 ||
          head.y < 0 ||
          head.x >= WIDTH ||
          head.y >= HEIGHT ||
          prev.some((cell) => cell.x === head.x && cell.y === head.y)
        ) {
          setGameOver(true);
          return prev;
        }

        const newSnake = [head, ...prev];

        // 먹이 먹음
        if (head.x === food.x && head.y === food.y) {
          setFood(getRandomFood());
        } else {
          newSnake.pop();
        }

        return newSnake;
      });
    }, 150);

    return () => clearInterval(interval);
  }, [dir, food, gameOver]);

  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        marginTop: '40px',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <h2>🐍 스네이크 게임</h2>
      {gameOver && <h3 style={{ color: 'red' }}>💀 Game Over!</h3>}
      <div
        ref={boardRef}
        style={{
          position: 'relative',
          width: WIDTH,
          height: HEIGHT,
          border: '2px solid #333',
          backgroundColor: '#111',
        }}
      >
        {snake.map((s, i) => (
          <div
            key={i}
            style={{
              position: 'absolute',
              width: CELL_SIZE,
              height: CELL_SIZE,
              left: s.x,
              top: s.y,
              backgroundColor: i === 0 ? '#0f0' : '#0c0',
            }}
          />
        ))}
        <div
          style={{
            position: 'absolute',
            width: CELL_SIZE,
            height: CELL_SIZE,
            left: food.x,
            top: food.y,
            backgroundColor: 'red',
          }}
        />
      </div>
    </div>
  );
}

export default App;