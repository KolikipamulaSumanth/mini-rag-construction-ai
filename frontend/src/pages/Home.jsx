import ChatBox from '../components/ChatBox'
import ContextPanel from '../components/ContextPanel'
import { useChat } from '../hooks/useChat'

export default function Home() {
  const {
    loading,
    indexLoading,
    result,
    messages,
    error,
    setError,
    handleBuildIndex,
    handleAsk
  } = useChat()

  const onBuildIndex = async () => {
    try {
      const response = await handleBuildIndex()
      alert(`Index built. Documents: ${response.documents_processed}, Chunks: ${response.chunks_created}`)
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div className="layout">
      <ChatBox
        messages={messages}
        onAsk={handleAsk}
        onBuildIndex={onBuildIndex}
        loading={loading}
        indexLoading={indexLoading}
        error={error}
      />
      <ContextPanel chunks={result?.retrieved_context || []} />
    </div>
  )
}
