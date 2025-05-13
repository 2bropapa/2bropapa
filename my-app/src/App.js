import React, { useState } from 'react';

function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleTheme = () => setIsDarkMode(!isDarkMode);

  const containerStyle = {
    display: 'flex',
    minHeight: '100vh',
    backgroundColor: isDarkMode ? '#1e1e1e' : '#f0f0f0',
    color: isDarkMode ? '#fff' : '#000',
    transition: '0.3s',
  };

  const leftPanel = {
    width: '200px',
    padding: '20px',
    borderRight: '1px solid #ccc',
  };

  const rightPanel = {
    flex: 1,
    padding: '20px',
  };

  return (
    <div style={containerStyle}>
      <div style={leftPanel}>
        <h3>🛠️ 설정</h3>
        <button onClick={toggleTheme}>
          {isDarkMode ? '☀️ 라이트 모드' : '🌙 다크 모드'}
        </button>
      </div>
      <div style={rightPanel}>
        <h1>메인 콘텐츠</h1>
        <p>여기에 원하는 정보 넣으면 돼!</p>
      </div>
    </div>
  );
}

export default App;