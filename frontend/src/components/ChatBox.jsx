import { useState } from 'react'
import Loader from './Loader'
import MessageBubble from './MessageBubble'

export default function ChatBox({ messages, onAsk, onBuildIndex, loading, indexLoading, error }) {
  const [question, setQuestion] = useState('')

  const submit = async (e) => {
    e.preventDefault()
    const trimmed = question.trim()
    if (!trimmed) return
    await onAsk(trimmed)
    setQuestion('')
  }

  return (
    <div className="panel card">
      <div className="toolbar">
        <h2>Construction Assistant</h2>
        <button onClick={onBuildIndex} disabled={indexLoading}>
          {indexLoading ? 'Building Index...' : 'Build Index'}
        </button>
      </div>

      <div className="chat-scroll">
        {!messages.length && <p>Ask a question about the uploaded internal documents.</p>}
        {messages.map((message, index) => (
          <MessageBubble key={`${message.role}-${index}`} role={message.role} content={message.content} />
        ))}
        {loading && <Loader label="Generating grounded answer..." />}
      </div>

      {error && <div className="error-box">{error}</div>}

      <form onSubmit={submit} className="query-form">
        <textarea
          rows="4"
          placeholder="What factors affect construction project delays?"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button type="submit" disabled={loading}>Ask</button>
      </form>
    </div>
  )
}
