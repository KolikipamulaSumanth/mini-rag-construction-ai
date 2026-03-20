export default function ContextPanel({ chunks }) {
  return (
    <div className="panel card">
      <h2>Retrieved Context</h2>
      {!chunks?.length && <p>No retrieved context yet.</p>}
      {chunks?.map((chunk) => (
        <div key={chunk.chunk_id} className="chunk-card">
          <div className="chunk-meta">
            <strong>{chunk.source}</strong> | {chunk.chunk_id} | score: {chunk.score.toFixed(4)}
          </div>
          <p>{chunk.text}</p>
        </div>
      ))}
    </div>
  )
}
