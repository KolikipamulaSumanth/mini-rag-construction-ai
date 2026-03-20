export default function MessageBubble({ role, content }) {
  return (
    <div className={`message-bubble ${role}`}>
      <div className="message-role">{role === 'user' ? 'You' : 'Assistant'}</div>
      <div className="message-content">{content}</div>
    </div>
  )
}
