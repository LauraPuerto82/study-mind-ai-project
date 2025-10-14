import { useState } from 'react'

function App() {
  const [message, setMessage] = useState<string>('')

  const fetchMessage = async (role: 'student' | 'parent') => {
    const response = await fetch(`http://127.0.0.1:8000/api/v1/hello/${role}`)
    const data = await response.json()
    setMessage(data.message)
  }

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>🎓 StudyMind AI</h1>
      <p>Select who you are:</p>
      <button onClick={() => fetchMessage('student')}>👩‍🎓 I'm a student</button>
      <button onClick={() => fetchMessage('parent')} style={{ marginLeft: '10px' }}>
        👨‍👧 I'm a parent
      </button>

      {message && (
        <p style={{ marginTop: '30px', fontSize: '18px', color: '#ffffff' }}>{message}</p>
      )}
    </div>
  )
}

export default App
