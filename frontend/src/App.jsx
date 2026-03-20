import Home from './pages/Home'
import './styles/styles.css'

export default function App() {
  return (
    <div className="app-shell">
      <header className="app-header">
        <h1>Mini RAG Construction AI</h1>
        <p>Grounded answers from internal documents</p>
      </header>
      <Home />
    </div>
  )
}
